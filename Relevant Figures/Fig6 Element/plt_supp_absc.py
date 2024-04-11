#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:00:51 2023

@author: aliciaglenda
"""

import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns  
import matplotlib.ticker as ticker

N_index=np.load("N_index.npy")
DN = len(N_index)
CC = np.load("CC.npy")
DD = np.load("DD.npy")    

D2 = np.load("D.npy")


C = CC #|c|
D2 = np.load("D.npy")
D1 = D2/4
D = np.array(list(zip(D1,D2)))


clis = plt.cm.rainbow_r(np.linspace(0,1,10))

fig,ax=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)
sns.set(style="darkgrid") 



plt.errorbar(N_index, C[9,:], xerr=None, yerr=D[9,:,:],capsize=2,fmt='.', label='g=0.1', color = clis[9,:])
plt.errorbar(N_index, C[8,:], xerr=None, yerr=D[8,:,:],capsize=2,fmt='.', label='g=0.2', color = clis[8,:])
plt.errorbar(N_index, C[7,:], xerr=None, yerr=D[7,:,:],capsize=2,fmt='.', label='g=0.3', color = clis[7,:])
plt.errorbar(N_index, C[6,:], xerr=None, yerr=D[6,:,:],capsize=2,fmt='.', label='g=0.4', color = clis[6,:])
plt.errorbar(N_index, C[5,:], xerr=None, yerr=D[5,:,:],capsize=2,fmt='.', label='g=0.5', color = clis[5,:])
plt.errorbar(N_index, C[4,:], xerr=None, yerr=D[4,:,:],capsize=2,fmt='.', label='g=0.6', color = clis[4,:])
plt.errorbar(N_index, C[3,:], xerr=None, yerr=D[3,:,:],capsize=2,fmt='.', label='g=0.7', color = clis[3,:])
plt.errorbar(N_index, C[2,:], xerr=None, yerr=D[2,:,:],capsize=2,fmt='.', label='g=0.8', color = clis[2,:])
plt.errorbar(N_index, C[1,:], xerr=None, yerr=D[1,:,:],capsize=2,fmt='.', label='g=0.9', color = clis[1,:])
plt.errorbar(N_index, C[0,:], xerr=None, yerr=D[0,:,:],capsize=2,fmt='.', label='g=1', color = clis[0,:])
sns.set_context("poster", font_scale = 3/4 , rc={"grid.linewidth": 3})


ax.set_xlabel('N' + r' ($\times 10^{}$)'.format(int(np.log10(np.max(N_index)))))
ax.set_ylabel('$1/\delta^2$' )
#plt.ylim(-1, 1.25)#C
plt.ylim(0, 1.1)#|C|
#plt.ylim(-0.3, 0.75)#a
#plt.ylim(-0.3, 0.65)#b
#plt.legend(loc='best', ncol=4, prop = {'size':7}, frameon=False)
plt.savefig('EB_absC.png',dpi=400,bbox_inches ='tight')

plt.show()
