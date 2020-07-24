#!/bin/bash
#
# Saketh Mynampati 2020
# Batch Effect Correction Benchmarking
# Pipeline to Process Data
#
# 1) Normalize Single Cell Data
# 2) Select Features

set -e

# Step 0: Convert all notebooks to scripts and create CSVs of the data using R
jupyter nbconvert --to=script \
        --FilesWriter.build_directory=scripts/nbconverted \
        *.ipynb

jupyter nbconvert --to=html \
        --FilesWriter.build_directory=scripts/html \
        --ExecutePreprocessor.kernel_name=python3 \
        --ExecutePreprocessor.timeout=10000000 \
        --execute 0.Create-csvs.ipynb 

# Step 1, 2, and 3: Normalize Data and Remove Features With Low Variance or Missing Values

jupyter nbconvert --to=html \
        --FilesWriter.build_directory=scripts/html \
        --ExecutePreprocessor.kernel_name=python3 \
        --ExecutePreprocessor.timeout=10000000 \
        --execute 1.Cell-Data-Normalization.ipynb

jupyter nbconvert --to=html \
        --FilesWriter.build_directory=scripts/html \
        --ExecutePreprocessor.kernel_name=python3 \
        --ExecutePreprocessor.timeout=10000000 \
        --execute 2.Cell-Data-Normalization.ipynb       

jupyter nbconvert --to=html \
        --FilesWriter.build_directory=scripts/html \
        --ExecutePreprocessor.kernel_name=python3 \
        --ExecutePreprocessor.timeout=10000000 \
        --execute 3.Cell-Data-Normalization.ipynb       


