#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pycytominer


# In[8]:


import numpy as np
import math 
import pandas as pd
import os
from os import path
import sqlite3


# In[9]:


cytoplasm_df = pd.read_csv('../data/Unnormalized_Batch2_Cytoplasm.csv')


# In[10]:


import gc
gc.collect()


# In[11]:


####### Normalize each file with the entire file as the sample to fit based on. #######
cytoplasm_df_norm = pycytominer.normalize(
    pycytominer.feature_select(
        cytoplasm_df
        )
    )


# In[12]:


cytoplasm_df_norm.shape


# In[13]:


cytoplasm_df_norm.to_csv("../data/Normalized_Cytoplasm_Batch2.csv", index=False)

