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
import matplotlib.image as mpimg

from matplotlib import colors  
from matplotlib import rc
import matplotlib.patches as mpatches

#plt.rcdefaults()
mpl.rcParams['font.family']= 'sans-serif'
mpl.rcParams['font.serif'] = 'Computer Modern Roman'
mpl.rcParams['font.sans-serif']= 'Computer Modern Sans Serif'
mpl.rcParams['mathtext.fontset']='stix'
mpl.rcParams['mathtext.rm'] = 'sans'
mpl.rcParams['mathtext.it'] = 'sans:italic'
mpl.rcParams['mathtext.default']='it'
mpl.rcParams['mathtext.bf']= 'sans:bold'

sns.set(style="darkgrid")
sns.set_context("poster", font_scale = 0.35 , rc={"grid.linewidth": 1})

fig,axs=plt.subplots( 2, 3, figsize=(6.772, 5))
plt.subplots_adjust(hspace=0.02,wspace=0.05)

axs[0, 0].imshow(mpimg.imread('K0.png'))
axs[0, 1].imshow(mpimg.imread('K1.png'))
axs[0, 2].imshow(mpimg.imread('K2.png'))
axs[1, 0].imshow(mpimg.imread('K3.png'))
axs[1, 1].imshow(mpimg.imread('K4.png'))
axs[1, 2].imshow(mpimg.imread('K5.png'))
[ax.set_axis_off() for ax in axs.ravel()]
axs[1,2].text(1950, -2200, '$g$')

axs[0,0].text(800, -80, '$N=5$')
axs[0,1].text(800, -80, '$N=50$')
axs[0,2].text(800, -80, '$N=500$')
axs[1,0].text(800, -80, '$N=5000$')

cmap = mpl.cm.rainbow
norm = mpl.colors.Normalize(vmin=0.1, vmax=1)
cax = axs[0,2].inset_axes([1.06, -0.88, 0.09, 1.865])
cbar=fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax, ax=axs[:], pad=0.03,orientation='vertical',ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
cbar.ax.tick_params(width=0.5,length=3)


plt.savefig('Fig2.png',dpi=400,bbox_inches ='tight')
plt.show() 
