#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:58:18 2023

@author: aliciaglenda
"""

import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import seaborn as sns  

from matplotlib import colors  
from matplotlib import rc
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
sns.set_context("poster", font_scale = 0.25 , rc={"grid.linewidth": 1})

T = np.load("T.npy")
T_index = np.load("t_.npy")



TV = np.load("TV.npy")
WV = np.load("WV.npy")
G_indexr = np.load("G_index.npy")
T_indexr = np.load("T_index.npy")
#Real and Imag Separation
ar = TV.real
br = TV.imag
mr = abs(TV)
Ar = WV.real
Br = WV.imag
Mr = abs(WV)

Omg = qload('gs')
Teta = qload('Teta')
b_wm = np.load('b_wm.npy')
a_wm = np.load('a_wm.npy')
Rw_wm = a_wm+1j*b_wm
GF_wm = Rw_wm*0
for i in range(T):
    GF_wm[:,i] = (Teta[i].dag()*Omg)[0,0] * Rw_wm[:,i]

A = GF_wm.real
#A = np.roll(A,3,axis=1)
B = GF_wm.imag
#B = np.roll(B,3,axis=1)
M = abs(GF_wm)
#M = np.roll(M,3,axis=1)
GF = np.load("GF.npy")
#GF = np.roll(GF,3,axis=0)
b = GF.imag
a = GF.real
m = abs(GF) 
#T_index=np.arange(0,5,1)

clis = plt.cm.rainbow_r(np.linspace(0,1,10))

#Plt real
fig,axs=plt.subplots( 2, 3, figsize=(6.772, 2), sharey=False, sharex=False)#,layout='constrained')#,gridspec_kw={'height_ratios': [1, 1, 1, 0.12]})
plt.subplots_adjust(hspace=0.55,wspace=0.5)


axs[0,0].plot(T_index, A[9,:],   linewidth=0.5,linestyle='-' , color=clis[9,:]) 
axs[0,0].plot(T_index, A[8,:],   linewidth=0.5,linestyle='-' , color=clis[8,:]) 
axs[0,0].plot(T_index, A[7,:],   linewidth=0.5,linestyle='-' , color=clis[7,:]) 
axs[0,0].plot(T_index, A[6,:],   linewidth=0.5,linestyle='-' , color=clis[6,:]) 
axs[0,0].plot(T_index, A[5,:],   linewidth=0.5,linestyle='-' , color=clis[5,:]) 
axs[0,0].plot(T_index, A[4,:],   linewidth=0.5,linestyle='-' , color=clis[4,:])  
axs[0,0].plot(T_index, A[3,:],   linewidth=0.5,linestyle='-' , color = clis[3,:]) 
axs[0,0].plot(T_index, A[2,:],   linewidth=0.5,linestyle='-' , color = clis[2,:]) 
axs[0,0].plot(T_index, A[1,:],   linewidth=0.5,linestyle='-' , color = clis[1,:]) 
axs[0,0].plot(T_index, A[0,:],   linewidth=0.5,linestyle='-' , color = clis[0,:]) 
axs[0,0].plot(T_index, a ,color='#4a488e',linewidth=1,linestyle='-', label='true value') 
axs[0,0].plot([], [], color='grey', label='g', linestyle='-', linewidth=0.5) 
axs[0,0].set(xlabel='$t$', ylabel='Re$G_w^{\mathrm{QFT}}$',ylim=(-0.54,0.54))
axs[0,0].text(-4.6, 0.54, '(a)')


axs[0,1].plot(T_index, B[9,:],   linewidth=0.5,linestyle='-' ,  color=clis[9,:])  
axs[0,1].plot(T_index, B[8,:],   linewidth=0.5,linestyle='-' , color=clis[8,:]) 
axs[0,1].plot(T_index, B[7,:],   linewidth=0.5,linestyle='-' , color=clis[7,:]) 
axs[0,1].plot(T_index, B[6,:],   linewidth=0.5,linestyle='-' , color=clis[6,:]) 
axs[0,1].plot(T_index, B[5,:],   linewidth=0.5,linestyle='-' ,  color=clis[5,:]) 
axs[0,1].plot(T_index, B[4,:],   linewidth=0.5,linestyle='-' , color=clis[4,:])  
axs[0,1].plot(T_index, B[3,:],   linewidth=0.5,linestyle='-' ,  color = clis[3,:]) 
axs[0,1].plot(T_index, B[2,:],   linewidth=0.5,linestyle='-' , color = clis[2,:]) 
axs[0,1].plot(T_index, B[1,:],   linewidth=0.5,linestyle='-' , color = clis[1,:]) 
axs[0,1].plot(T_index, B[0,:],   linewidth=0.5,linestyle='-' , color = clis[0,:]) 
axs[0,1].plot(T_index, b ,color='#4a488e',linewidth=1,linestyle='-', label='true value') 
axs[0,1].set(xlabel='$t$', ylabel='Im$G_w^{\mathrm{QFT}}$',ylim=(-0.54,0.54))
axs[0,1].text(-4.6, 0.54, '(b)')


axs[0,2].plot(T_index, M[9,:],   linewidth=0.5,linestyle='-' ,   color=clis[9,:])  
axs[0,2].plot(T_index, M[8,:],   linewidth=0.5,linestyle='-' ,   color=clis[8,:]) 
axs[0,2].plot(T_index, M[7,:],   linewidth=0.5,linestyle='-' ,   color=clis[7,:]) 
axs[0,2].plot(T_index, M[6,:],   linewidth=0.5,linestyle='-' ,   color=clis[6,:]) 
axs[0,2].plot(T_index, M[5,:],   linewidth=0.5,linestyle='-' ,   color=clis[5,:]) 
axs[0,2].plot(T_index, M[4,:],   linewidth=0.5,linestyle='-' ,   color=clis[4,:])  
axs[0,2].plot(T_index, M[3,:],   linewidth=0.5,linestyle='-' ,   color = clis[3,:]) 
axs[0,2].plot(T_index, M[2,:],   linewidth=0.5,linestyle='-' ,   color = clis[2,:]) 
axs[0,2].plot(T_index, M[1,:],   linewidth=0.5,linestyle='-' ,   color = clis[1,:]) 
axs[0,2].plot(T_index, M[0,:],   linewidth=0.5,linestyle='-' ,   color = clis[0,:]) 
axs[0,2].plot(T_index, m ,color='#4a488e',linewidth=1,linestyle='-', label='true value'  ) 
axs[0,2].set(xlabel='$t$', ylabel='$|G_w^{\mathrm{QFT}}|$',ylim=(0.1,0.53))
axs[0,2].legend(loc='upper right', ncol=1, prop = {'size':5},bbox_to_anchor=(1.05, 1.2))
axs[0,2].text(12.1, 0.56, '$g$')
axs[0,2].text(-4.6, 0.53, '(c)')


axs[1,0].plot(T_indexr, Ar[9,:],   linewidth=0.5,linestyle='-', color=clis[9,:]) 
axs[1,0].plot(T_indexr, Ar[8,:],   linewidth=0.5,linestyle='-', color=clis[8,:]  )
axs[1,0].plot(T_indexr, Ar[7,:],   linewidth=0.5,linestyle='-', color=clis[7,:]  )
axs[1,0].plot(T_indexr, Ar[6,:],   linewidth=0.5,linestyle='-', color=clis[6,:]  )
axs[1,0].plot(T_indexr, Ar[5,:],   linewidth=0.5,linestyle='-', color=clis[5,:]  )
axs[1,0].plot(T_indexr, Ar[4,:],   linewidth=0.5,linestyle='-', color=clis[4,:]  ) 
axs[1,0].plot(T_indexr, Ar[3,:],   linewidth=0.5,linestyle='-', color = clis[3,:]  )
axs[1,0].plot(T_indexr, Ar[2,:],   linewidth=0.5,linestyle='-', color = clis[2,:]  )
axs[1,0].plot(T_indexr, Ar[1,:],   linewidth=0.5,linestyle='-', color = clis[1,:]  )
axs[1,0].plot(T_indexr, Ar[0,:],   linewidth=0.5,linestyle='-', color = clis[0,:]  )
axs[1,0].plot(T_indexr, ar ,color='#4a488e',linewidth=1,linestyle='-', label='true value'  )
axs[1,0].set(xlabel='$t$', ylabel='Re$G_w^{\mathrm{QM}}$',ylim=(-0.53,0.53))
axs[1,0].text(-4.6, 0.53, '(d)')
#axs[1,0].legend(loc='best', ncol=1, prop = {'size':11})


axs[1,1].plot(T_indexr, Br[9,:],   linewidth=0.5,linestyle='-'  , color=clis[9,:])  
axs[1,1].plot(T_indexr, Br[8,:],   linewidth=0.5,linestyle='-' , color=clis[8,:]) 
axs[1,1].plot(T_indexr, Br[7,:],   linewidth=0.5,linestyle='-' , color=clis[7,:]) 
axs[1,1].plot(T_indexr, Br[6,:],   linewidth=0.5,linestyle='-' , color=clis[6,:]) 
axs[1,1].plot(T_indexr, Br[5,:],   linewidth=0.5,linestyle='-' ,  color=clis[5,:]) 
axs[1,1].plot(T_indexr, Br[4,:],   linewidth=0.5,linestyle='-' , color=clis[4,:]) 
axs[1,1].plot(T_indexr, Br[3,:],   linewidth=0.5,linestyle='-' ,  color = clis[3,:]) 
axs[1,1].plot(T_indexr, Br[2,:],   linewidth=0.5,linestyle='-' , color = clis[2,:]) 
axs[1,1].plot(T_indexr, Br[1,:],   linewidth=0.5,linestyle='-' , color = clis[1,:]) 
axs[1,1].plot(T_indexr, Br[0,:],   linewidth=0.5,linestyle='-' , color = clis[0,:]) 
axs[1,1].plot(T_indexr, br ,color='#4a488e',linewidth=1,linestyle='-', label='true value') 
axs[1,1].set(xlabel='$t$', ylabel='Im$G_w^{\mathrm{QM}}$',ylim=(-0.53,0.6))
axs[1,1].text(-4.6, 0.6, '(e)')

axs[1,2].plot(T_indexr, Mr[9,:],   linewidth=0.5,linestyle='-' ,   color=clis[9,:])  
axs[1,2].plot(T_indexr, Mr[8,:],   linewidth=0.5,linestyle='-' ,   color=clis[8,:]) 
axs[1,2].plot(T_indexr, Mr[7,:],   linewidth=0.5,linestyle='-' ,   color=clis[7,:]) 
axs[1,2].plot(T_indexr, Mr[6,:],   linewidth=0.5,linestyle='-' ,   color=clis[6,:]) 
axs[1,2].plot(T_indexr, Mr[5,:],   linewidth=0.5,linestyle='-' ,   color=clis[5,:]) 
axs[1,2].plot(T_indexr, Mr[4,:],   linewidth=0.5,linestyle='-' ,   color=clis[4,:])  
axs[1,2].plot(T_indexr, Mr[3,:],   linewidth=0.5,linestyle='-' ,   color = clis[3,:]) 
axs[1,2].plot(T_indexr, Mr[2,:],   linewidth=0.5,linestyle='-' ,   color = clis[2,:]) 
axs[1,2].plot(T_indexr, Mr[1,:],   linewidth=0.5,linestyle='-' ,   color = clis[1,:]) 
axs[1,2].plot(T_indexr, Mr[0,:],   linewidth=0.5,linestyle='-' ,   color = clis[0,:]) 
axs[1,2].plot(T_indexr, mr ,color='#4a488e',linewidth=1,linestyle='-', label='true value') 
#axs[1,2].plot([], [], color='grey', label='g', linestyle='-', linewidth=0.5   ) 
axs[1,2].set(xlabel='$t$', ylabel='$|G_w^{\mathrm{QM}}|$',ylim=(0.3,0.52))
axs[1,2].text(-4.6, 0.52, '(f)')

for i in [0,1]:
    for j in [0,1,2]:
        axs[i,j].tick_params(pad=-8)
    
cmap = mpl.cm.rainbow
norm = mpl.colors.Normalize(vmin=0.1, vmax=1)
cbar=fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=axs[:], pad=0.03,orientation='vertical',ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
cbar.ax.tick_params(width=0.5,length=3)
plt.savefig('Fig7.pdf',dpi=400,bbox_inches ='tight')
plt.show() 
