#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pycytominer


# In[2]:


import numpy as np
import math 
import pandas as pd
import os
from os import path
import sqlite3


# In[3]:


nuclei_df = pd.read_csv('../data/Unnormalized_Batch2_Nuclei.csv')


# In[4]:


import gc
gc.collect()


# In[5]:


####### Normalize each file with the entire file as the sample to fit based on. #######
nuclei_df_norm = pycytominer.normalize(
    pycytominer.feature_select(
        nuclei_df
        )
    )


# In[13]:


print(nuclei_df_norm.shape)


# In[14]:


nuclei_df_norm.to_csv("../data/Normalized_Nuclei_Batch2.csv", index=False)

