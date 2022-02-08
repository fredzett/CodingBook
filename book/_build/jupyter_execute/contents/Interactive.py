#!/usr/bin/env python
# coding: utf-8

# # Lineare Regression
# 
# Dies ist nur ein Beispiel...nicht als Inhalt im Buch gedacht!

# ## Importieren wichtiger Module

# In[1]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import scipy.stats as stats
import statsmodels.formula.api as smf

# Modules for interactivity
from ipywidgets import interact
import ipywidgets as widgets

colors = plt.cycler(color=["#557A95",   "#957055", "#559570"]) 
sns.set_context('paper', font_scale=1.4)
plt.rcParams['figure.figsize'] = [9,6]
plt.rcParams['savefig.dpi'] = 300
plt.rc("legend", frameon=False)
plt.rc("axes.spines", top=False, right=False)
plt.rcParams['axes.prop_cycle'] = colors
mycolors = colors.by_key()["color"]


# ## Daten simulieren

# In[2]:


n = 100
x = np.linspace(-4,4, num=n) # make x data
eps = stats.norm().rvs(n) # create randomness
ytrue = 3 + 4*x + eps*5 # make y data


# ## Interaktive Elemente bauen

# In[3]:


box = widgets.Checkbox(False, description="show errors")
b0 = widgets.FloatSlider(value=0, min=-10,max=10)
b1 = widgets.FloatSlider(value=0, min=-10,max=10)
def lreg(b0,b1, changed):
    fig, ax = plt.subplots(figsize=(12,7))
    sns.scatterplot(x=x, y=ytrue)
    plt.xlabel("x")
    plt.ylabel("y")
    alpha = 0 if b0==b1==0 else 1
    yhat = b0 + b1*x
    sns.lineplot(x=x, y=yhat, color="red", alpha=alpha,lw=3)
    ax.set_title("Relation y and X")
    error = ytrue - yhat
    if changed:
        rss = np.round(np.sum(error**2)/n, 2)
        ax.vlines(x=x, ymin=yhat, ymax=yhat+error, ls="--", color="gray")
        _, ymax = ax.get_ylim()
        xmin, _ = ax.get_xlim()
        ax.annotate(f"RSS: {rss}", xy=(xmin*0.98,ymax))
    
    sns.despine()

grid = widgets.GridspecLayout(10,6)
grid[0,:] = widgets.HBox([b0,b1,box])
grid[1:10,:] = widgets.interactive_output(lreg, {"b0":b0, "b1": b1, "changed":box})

