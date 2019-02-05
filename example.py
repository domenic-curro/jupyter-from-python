#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import numpy as np


# In[ ]:


from matplotlib import pyplot


# ## Helper Functions

# In[ ]:


'''read dataset'''
def function(filepath):
    with open(filepath, 'rb') as handle:
        data = pickle.load(handle)
    return data

'''save data to disk'''
def save_results(out_data, outpath):
    with open(outpath, 'wb') as handle:
        pickle.dump(out_data, handle, protocol=pickle.HIGHEST_PROTOCOL)


# ## Setup

# In[ ]:


# a comment
x = 5


# In[ ]:


print ('Hello')
print ('World!')


# ## Followup code

# In[ ]:


# load test exampples
print ('Hello')
print ('World!')


# In[ ]:


# evaluate stuff
print ('Hello')
print ('World!')


# ## Save results to disk

# In[ ]:


# save results to disk
print ('Hello')
print ('World!')
# were they saved?


# ## Load results from disk

# In[ ]:


# load results from disk
print ('Hello')
print ('World!')


# ## Display results

# In[ ]:


## display stats
print ('\t ---------------- Hello World -----------------')


# In[ ]:


# display it in an image
# send it to a printer

