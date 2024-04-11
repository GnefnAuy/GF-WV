#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 14:38:47 2022

@author: aliciaglen
"""

import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import seaborn as sns  

N_index=np.load("N_index.npy")/1000
DN = len(N_index)
CC = np.load("CC.npy")
DD = np.load("DD.npy") /1000

clis = plt.cm.rainbow_r(np.linspace(0,1,10))

fig,ax=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)
sns.set(style="darkgrid") 
sns.set_context("poster", font_scale = 3/4 , rc={"grid.linewidth": 3})


plt.scatter(N_index, DD[0,:], s=10, color = clis[0,:],marker='*' )
plt.scatter(N_index, DD[1,:], s=10, color = clis[1,:],  marker='x' )
plt.scatter(N_index, DD[2,:], s=10, color = clis[2,:], marker='^' )
plt.scatter(N_index, DD[3,:], s=10, color = clis[3,:], marker='s' )
plt.scatter(N_index, DD[4,:], s=10, color=clis[4,:],  marker='h' ) 
plt.scatter(N_index, DD[5,:], s=10, color=clis[5,:],marker='o' )
plt.scatter(N_index, DD[6,:], s=10, color=clis[6,:],  marker='d' )
plt.scatter(N_index, DD[7,:], s=10, color=clis[7,:], marker='<' )
plt.scatter(N_index, DD[8,:], s=10, color=clis[8,:], marker='p' )
plt.scatter(N_index, DD[9,:], s=10, color=clis[9,:],  marker='1' ) 
#ax.set_xlabel('N' + r' ($\times 10^{}$)'.format(int(np.log10(np.max(N_index)))))
#ax.set_ylabel('$1/\delta^2$' + r' ($\times 10^{}$)'.format(int(np.log10(np.max(N_index)))))

#plt.yticks([0,1000, 2000 ])#C
#plt.yticks([0,1000, 2000 ,3000])#|C|
#plt.yticks([0,4000, 8000])#A
#plt.xticks([0, 2000, 4000])
#plt.xlabel('N')
#plt.ylabel('$1/\delta^2$')
#plt.legend(loc='best', ncol=1, prop = {'size':7}, frameon=False)
plt.savefig('C_B.png',dpi=400,bbox_inches ='tight')
plt.show()







    
    