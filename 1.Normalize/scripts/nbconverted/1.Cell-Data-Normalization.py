#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pycytominer


# In[21]:


import numpy as np
import math 
import pandas as pd
import os
from os import path
import sqlite3


# In[22]:


## """conn = sqlite3.connect("/home/ubuntu/bucket/projects/2018_05_30_ResistanceMechanisms_Kapoor/workspace/backend/2019_03_20_Batch2/207106_exposure320/207106_exposure320_copy.sqlite")
## 
## c1 = conn.cursor()

## def load_sc_profiles(connection, compartment = "Cells"):
##     
##     query = f"select * from {compartment} where ImageNumber == 1" ##change this.
##     print('hi')
##     return pd.read_sql_query(query, connection)
##     
##     
##     '''
##     Load an sqlite file's table into a dataframe.
##     
##     @Params:
##     connection - the SQLite connection to the desired database.
##     compartment - The specific table to be opened, equal to "Cells," "Cytoplasm," "Image," or "Nuclei."
##     '''
## """


# In[23]:


##cells = load_sc_profiles(conn)
##nuclei = load_sc_profiles(conn, "Nuclei")
##cytoplasm = load_sc_profiles(conn, "Cytoplasm")
##image_metadata = load_sc_profiles(conn, "Image")


# In[24]:


##for row in c1.execute('SELECT * from Cells where ImageNumber == 1'):
##    print(row)


# In[25]:


cells_df = pd.read_csv('../data/Unnormalized_Batch2_Cells.csv')


# In[26]:


import gc
gc.collect()


# In[27]:


####### Normalize each file with the entire file as the sample to fit based on. #######
cells_df_norm = pycytominer.normalize(
    pycytominer.feature_select(
        cells_df
        )
    )


# In[28]:


cells_df_norm.shape


# In[29]:


cells_df_norm.to_csv("../data/Normalized_Cells_Batch2.csv", index = False)


# In[ ]:




