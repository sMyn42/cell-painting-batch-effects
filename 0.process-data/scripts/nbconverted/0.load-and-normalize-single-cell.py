#!/usr/bin/env python
# coding: utf-8

# # Load and Process Single Cell Data
# 
# This notebook will load, normalize, and perform feature selection on a single plate of data from the Resistance Mechanisms project. The data are single cell morphology profiles.
# 
# This data represent the first data type input into the technical artifacts experiment.

# In[1]:


import sys
import pathlib
import sqlite3
import pandas as pd

from pycytominer import normalize, feature_select
from pycytominer.cyto_utils import output


# In[2]:


# Load functions modified from:
# https://github.com/broadinstitute/profiling-resistance-mechanisms/blob/5f0ab0035705836af0438e84dd7c336fc566a015/4.single-cell/utils/single_cell_utils.py
def load_compartment(compartment, connection):
    query = f"select * from {compartment}"
    df = pd.read_sql_query(query, connection)
    return df


def prefilter_features(df, flags):
    remove_cols = []
    for filter_feature in flags:
        remove_cols += [x for x in df.columns if filter_feature in x]
    remove_cols = list(set(remove_cols))
    return remove_cols


# In[3]:


project_tag = "2018_05_30_ResistanceMechanisms_Kapoor"
workspace_dir = f"/home/ubuntu/bucket/projects/{project_tag}/workspace/"

batch = "2019_02_15_Batch1_20X"
plate = "HCT116bortezomib"

sqlite_file = pathlib.Path(f"{workspace_dir}/backend/{batch}/{plate}/{plate}.sqlite")


# In[4]:


feature_select_opts = [
    "variance_threshold",
    "drop_na_columns",
    "blacklist",
    "drop_outliers",
]
corr_threshold = 0.8
na_cutoff = 0


# In[5]:


batch_dir = pathlib.Path(workspace_dir, "backend", batch)
metadata_dir = pathlib.Path(workspace_dir, "metadata", batch)

barcode_plate_map_file = pathlib.Path(metadata_dir, "barcode_platemap.csv")
barcode_plate_map_df = pd.read_csv(barcode_plate_map_file)

barcode_plate_map_df


# In[6]:


plate_map_name = (
    barcode_plate_map_df
    .query("Assay_Plate_Barcode == @plate")
    .Plate_Map_Name
    .values[0]
)

plate_map_file = pathlib.Path(metadata_dir, "platemap", f"{plate_map_name}.txt")
plate_map_df = pd.read_csv(plate_map_file, sep="\t")
plate_map_df.columns = [x if x.startswith("Metadata_") else f"Metadata_{x}" for x in plate_map_df.columns]
plate_map_df.head()


# ## Setup Connection to SQlite file

# In[7]:


conn = sqlite3.connect(sqlite_file)


# In[8]:


image_cols = f"TableNumber, ImageNumber, Metadata_Plate, Metadata_Well"
image_query = f"select {image_cols} from image"
image_df = (
    pd.read_sql_query(image_query, conn)
    .merge(
        plate_map_df,
        left_on="Metadata_Well",
        right_on="Metadata_well_position"
    )
    .drop(["Metadata_well_position"], axis="columns")
)

print(image_df.shape)
image_df.head()


# ## Load compartment data

# In[9]:


cells_df = load_compartment("cells", conn)
cytoplasm_df = load_compartment("cytoplasm", conn)
nuclei_df = load_compartment("nuclei", conn)


# ## Merge compartment data

# In[10]:


# Merge tables
merged_df = cells_df.merge(
    cytoplasm_df,
    left_on=["TableNumber", "ImageNumber", "ObjectNumber"],
    right_on=["TableNumber", "ImageNumber", "Cytoplasm_Parent_Cells"],
    how="inner",
).merge(
    nuclei_df,
    left_on=["TableNumber", "ImageNumber", "Cytoplasm_Parent_Nuclei"],
    right_on=["TableNumber", "ImageNumber", "ObjectNumber"],
    how="inner",
)


# ## Filter features

# In[11]:


feature_filter_flags = ["Object", "Location", "Count", "Parent"]
drop_features = prefilter_features(merged_df, feature_filter_flags)

merged_df = merged_df.drop(drop_features, axis="columns")

# Merge with the image information
merged_df = image_df.merge(
    merged_df, on=["TableNumber", "ImageNumber"], how="right"
)

print(merged_df.shape)
merged_df.head()


# ## Apply normalization, feature select, and output data

# In[12]:


normalized_df = normalize(
    merged_df,
    features="infer",
    meta_features="infer",
    samples="all",
    method="standardize"
)


# In[13]:


feature_select_df = feature_select(
    normalized_df,
    features="infer",
    operation=feature_select_opts,
    output_file="none",
    na_cutoff=na_cutoff,
    corr_threshold=corr_threshold,
)

print(feature_select_df.shape)
feature_select_df.head()


# In[14]:


output_filename = pathlib.Path(
    f"data/{batch}/{plate}_singlecell_normalized_feature_select.csv.gz"
)
output(normalized_df, output_filename, compression="gzip", float_format="%.5g" )

