#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:03:44 2022

@author: aliciaglenda
"""

import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from collections import Counter
from matplotlib import cm
from matplotlib import colors  
import seaborn as sns  
import pandas as pd
from pandas import Series, DataFrame
sns.set(style="darkgrid") 

#Import
TV=np.load("TV.npy")
WV=np.load("WV.npy")
MD=np.load("MD3.npy")
G_index = np.load("G_index.npy")
N_index=np.load("N_index.npy")
M=np.load("M.npy")
DN=len(N_index)
DG=len(G_index)
#Radial Vector
RV = (MD-TV)
RRV = RV/abs(TV)
VV = (WV-TV)/abs(TV)
#Plot
a = RRV.real
b = RRV.imag


c = np.column_stack((a[0,:],b[0,:]))
d = np.ones(M)*G_index[0]
data = np.insert(c, 2, d, axis=1 )

for j in range(DG):
    c = np.column_stack((a[j,:],b[j,:]))
    d = np.ones(M)*G_index[j]
    data1 = np.insert(c, 2, d, axis=1 )
    data = np.append(data, data1, axis=0)
Trafdata = DataFrame(data, columns=['Re','Im','g_merit'])

#font_scale = 1.2 for FIG wide= 8.6cm
sns.set(style="darkgrid") 
pal2 = sns.color_palette("rainbow", as_cmap=True)
sns.set_context("poster", font_scale = 0.8225 , rc={"grid.linewidth": 5})
g = sns.JointGrid(x='Re', y='Im', data= Trafdata, 
              hue='g_merit',
              #kind="kde",
              #joint_kws=dict(alpha =1, shade = True,),
              #marginal_kws=dict(shade=True),
              palette=pal2, marginal_ticks= False,
              xlim=(-0.15, 0.21), ylim=(-0.1, 0.65)
)
g.fig.set_size_inches(5, 5)
g.set_axis_labels(' ', ' ', fontsize=0)
ax1 = g.ax_marg_x
ax1.set_xticks([0,0.2])
ax2 = g.ax_marg_y
ax2.set_yticks([0.2, 0.5])
#g.ax_joint.tick_params(axis='y', labelrotation=90)

g.plot_joint(sns.kdeplot, fill=True, legend= False)
g.plot_marginals(sns.kdeplot, fill=True)
#g.plot_marginals(sns.histplot, kde=True)
plt.savefig('K3.png',dpi=400,bbox_inches ='tight')
plt.show()



