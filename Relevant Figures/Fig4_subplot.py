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
sns.set_context("poster", font_scale = 0.3 , rc={"grid.linewidth": 1})

T = np.load("T.npy")
T_index = np.load("t_.npy")


#import
Br = np.load("b_wm_.npy").real
Ar = np.load("a_wm_.npy").real
Mr = np.sqrt (abs(Ar)**2 + abs(Br)**2)
Rw = np.load("Rw.npy")
br = Rw.imag
ar = Rw.real
mr = abs(Rw)
G_index = np.load("G_.npy")

Omg = qload('gs')
Teta = qload('Teta')
b_wm = np.load('b_wm_.npy')
a_wm = np.load('a_wm_.npy')
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
fig,axs=plt.subplots( 2, 3, figsize=(6.772, 2.5), sharey=False, sharex=False)#,layout='constrained')#,gridspec_kw={'height_ratios': [1, 1, 1, 0.12]})
plt.subplots_adjust(hspace=0.55,wspace=0.5)

axs[0,0].plot(T_index, Ar[9,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[9,:],markersize=3,mew=0.9) 
axs[0,0].plot(T_index, Ar[8,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[8,:],markersize=3,mew=0.9)
axs[0,0].plot(T_index, Ar[7,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[7,:],markersize=3,mew=0.9)
axs[0,0].plot(T_index, Ar[6,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[6,:],markersize=3,mew=0.9)
axs[0,0].plot(T_index, Ar[5,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[5,:],markersize=3,mew=0.9)
axs[0,0].plot(T_index, Ar[4,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[4,:],markersize=3,mew=0.9) 
axs[0,0].plot(T_index, Ar[3,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[3,:],markersize=3,mew=0.9)
axs[0,0].plot(T_index, Ar[2,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[2,:],markersize=3,mew=0.9)
axs[0,0].plot(T_index, Ar[1,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[1,:],markersize=3,mew=0.9)
axs[0,0].plot(T_index, Ar[0,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[0,:],markersize=3,mew=0.9)
axs[0,0].plot(T_index, ar ,color='#4a488e',linewidth=0.8,linestyle='-', marker='.',label='true value',markersize=3,mew=1)
axs[0,0].set(xlabel='$t$', ylabel='Re$R_w$',xticks=T_index,ylim=(0.1,0.43))
axs[0,0].text(-3.8, 0.43, '(a)')
#axs[0,0].legend(loc='best', ncol=1, prop = {'size':11})


axs[0,1].plot(T_index, Br[9,:],   linewidth=0.6,linestyle='--', marker='x' , color=clis[9,:],markersize=3,mew=0.9)  
axs[0,1].plot(T_index, Br[8,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[8,:],markersize=3,mew=0.9) 
axs[0,1].plot(T_index, Br[7,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[7,:],markersize=3,mew=0.9) 
axs[0,1].plot(T_index, Br[6,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[6,:],markersize=3,mew=0.9) 
axs[0,1].plot(T_index, Br[5,:],   linewidth=0.6,linestyle='--', marker='x',  color=clis[5,:],markersize=3,mew=0.9) 
axs[0,1].plot(T_index, Br[4,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[4,:],markersize=3,mew=0.9) 
axs[0,1].plot(T_index, Br[3,:],   linewidth=0.6,linestyle='--', marker='x',  color = clis[3,:],markersize=3,mew=0.9) 
axs[0,1].plot(T_index, Br[2,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[2,:],markersize=3,mew=0.9) 
axs[0,1].plot(T_index, Br[1,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[1,:],markersize=3,mew=0.9) 
axs[0,1].plot(T_index, Br[0,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[0,:],markersize=3,mew=0.9) 
axs[0,1].plot(T_index, br ,color='#4a488e',linewidth=0.8,linestyle='-', marker='.', label='true value',markersize=3,mew=1) 
axs[0,1].set(xlabel='$t$', ylabel='Im$R_w$',xticks=T_index,ylim=(-0.16,0.02))
axs[0,1].text(-3.8, 0.02, '(b)')

axs[0,2].plot(T_index, Mr[9,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[9,:],markersize=3,mew=0.9)  
axs[0,2].plot(T_index, Mr[8,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[8,:],markersize=3,mew=0.9) 
axs[0,2].plot(T_index, Mr[7,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[7,:],markersize=3,mew=0.9) 
axs[0,2].plot(T_index, Mr[6,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[6,:],markersize=3,mew=0.9) 
axs[0,2].plot(T_index, Mr[5,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[5,:],markersize=3,mew=0.9) 
axs[0,2].plot(T_index, Mr[4,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[4,:],markersize=3,mew=0.9)  
axs[0,2].plot(T_index, Mr[3,:],   linewidth=0.6,linestyle='--', marker='x',   color = clis[3,:],markersize=3,mew=0.9) 
axs[0,2].plot(T_index, Mr[2,:],   linewidth=0.6,linestyle='--', marker='x',   color = clis[2,:],markersize=3,mew=0.9) 
axs[0,2].plot(T_index, Mr[1,:],   linewidth=0.6,linestyle='--', marker='x',   color = clis[1,:],markersize=3,mew=0.9) 
axs[0,2].plot(T_index, Mr[0,:],   linewidth=0.6,linestyle='--', marker='x',   color = clis[0,:],markersize=3,mew=0.9) 
axs[0,2].plot(T_index, mr ,color='#4a488e',linewidth=0.8,linestyle='-',marker='.', label='true value',markersize=3,mew=1) 
axs[0,2].set(xlabel='$t$', ylabel='$|R_w|$',xticks=T_index,ylim=(0.15,0.43))
axs[0,2].text(-3.8, 0.43, '(c)')
axs[0,2].legend(loc='upper right', ncol=1, prop = {'size':7},bbox_to_anchor=(1.05, 1.27))
axs[0,2].text(2.88, 0.45, '$g$')

axs[1,0].plot(T_index, A[9,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[9,:],markersize=3,mew=0.9) 
axs[1,0].plot(T_index, A[8,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[8,:],markersize=3,mew=0.9) 
axs[1,0].plot(T_index, A[7,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[7,:],markersize=3,mew=0.9) 
axs[1,0].plot(T_index, A[6,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[6,:],markersize=3,mew=0.9) 
axs[1,0].plot(T_index, A[5,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[5,:],markersize=3,mew=0.9) 
axs[1,0].plot(T_index, A[4,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[4,:],markersize=3,mew=0.9)  
axs[1,0].plot(T_index, A[3,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[3,:],markersize=3,mew=0.9) 
axs[1,0].plot(T_index, A[2,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[2,:],markersize=3,mew=0.9) 
axs[1,0].plot(T_index, A[1,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[1,:],markersize=3,mew=0.9) 
axs[1,0].plot(T_index, A[0,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[0,:],markersize=3,mew=0.9) 
axs[1,0].plot(T_index, a ,color='#4a488e',linewidth=0.8,linestyle='-', marker='.',label='true value',markersize=3,mew=1) 
axs[1,0].set(xlabel='$t$', ylabel='Re$G_w$',xticks=T_index,ylim=(-0.15,0.35))
axs[1,0].text(-3.8, 0.35, '(d)')



axs[1,1].plot(T_index, B[9,:],   linewidth=0.6,linestyle='--', marker='x',  color=clis[9,:],markersize=3,mew=0.9)  
axs[1,1].plot(T_index, B[8,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[8,:],markersize=3,mew=0.9) 
axs[1,1].plot(T_index, B[7,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[7,:],markersize=3,mew=0.9) 
axs[1,1].plot(T_index, B[6,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[6,:],markersize=3,mew=0.9) 
axs[1,1].plot(T_index, B[5,:],   linewidth=0.6,linestyle='--', marker='x',  color=clis[5,:],markersize=3,mew=0.9) 
axs[1,1].plot(T_index, B[4,:],   linewidth=0.6,linestyle='--', marker='x', color=clis[4,:],markersize=3,mew=0.9)  
axs[1,1].plot(T_index, B[3,:],   linewidth=0.6,linestyle='--', marker='x',  color = clis[3,:],markersize=3,mew=0.9) 
axs[1,1].plot(T_index, B[2,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[2,:],markersize=3,mew=0.9) 
axs[1,1].plot(T_index, B[1,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[1,:],markersize=3,mew=0.9) 
axs[1,1].plot(T_index, B[0,:],   linewidth=0.6,linestyle='--', marker='x', color = clis[0,:],markersize=3,mew=0.9) 
axs[1,1].plot(T_index, b ,color='#4a488e',linewidth=0.8,linestyle='-', marker='.', label='true value',markersize=3,mew=1) 
axs[1,1].set(xlabel='$t$', ylabel='Im$G_w$',xticks=T_index,ylim=(-0.26,0.03))
axs[1,1].text(-3.8, 0.03, '(e)')


axs[1,2].plot(T_index, M[9,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[9,:],markersize=3,mew=0.9)  
axs[1,2].plot(T_index, M[8,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[8,:],markersize=3,mew=0.9) 
axs[1,2].plot(T_index, M[7,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[7,:],markersize=3,mew=0.9) 
axs[1,2].plot(T_index, M[6,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[6,:],markersize=3,mew=0.9) 
axs[1,2].plot(T_index, M[5,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[5,:],markersize=3,mew=0.9) 
axs[1,2].plot(T_index, M[4,:],   linewidth=0.6,linestyle='--', marker='x',   color=clis[4,:],markersize=3,mew=0.9)  
axs[1,2].plot(T_index, M[3,:],   linewidth=0.6,linestyle='--', marker='x',   color = clis[3,:],markersize=3,mew=0.9) 
axs[1,2].plot(T_index, M[2,:],   linewidth=0.6,linestyle='--', marker='x',   color = clis[2,:],markersize=3,mew=0.9) 
axs[1,2].plot(T_index, M[1,:],   linewidth=0.6,linestyle='--', marker='x',   color = clis[1,:],markersize=3,mew=0.9) 
axs[1,2].plot(T_index, M[0,:],   linewidth=0.6,linestyle='--', marker='x',   color = clis[0,:],markersize=3,mew=0.9) 
axs[1,2].plot(T_index, m ,color='#4a488e',linewidth=0.8,linestyle='-',marker='.', label='true value',markersize=3,mew=1) 
axs[1,2].set(xlabel='$t$', ylabel='$|G_w|$',xticks=T_index,ylim=(0.05,0.33))
axs[1,2].text(-3.8, 0.33, '(f)')
for i in [0,1]:
    for j in [0,1,2]:
        axs[i,j].tick_params(pad=-8)
    
cmap = mpl.cm.rainbow
norm = mpl.colors.Normalize(vmin=0.1, vmax=1)
cbar=fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=axs[:], pad=0.03,orientation='vertical',ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
cbar.ax.tick_params(width=0.5,length=3)
plt.savefig('Fig4.pdf',dpi=400,bbox_inches ='tight')
plt.show() 
