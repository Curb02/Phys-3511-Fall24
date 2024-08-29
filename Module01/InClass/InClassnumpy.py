#!/usr/bin/env python
# coding: utf-8

# In[22]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

new_list = np.random.randn(1000)

def MakeHist(random,thebins,horiz,verti):
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    ax.set_xlabel(horiz)
    ax.set_ylabel(verti)
    ax.set_title('nbins = ' + str(thebins) )
    ax.hist(random,bins=thebins);
MakeHist(new_list,10,"x","counts")
MakeHist(new_list,100,"x","counts")
MakeHist(new_list,1000,"x","counts")


# In[ ]:




