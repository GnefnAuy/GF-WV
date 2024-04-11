#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:17:32 2023

@author: aliciaglenda
"""

import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
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
sns.set_context("poster", font_scale = 0.38 , rc={"grid.linewidth": 2})

#import
TV = np.load("TV.npy")
T_index = np.load("T_index.npy")
TVs_1000 = np.load("TVs_1000.npy")
TVs_500 = np.load("TVs_500.npy")
TVs_100 = np.load("TVs_100.npy")
TVs_50 = np.load("TVs_50.npy")
TVs_10 = np.load("TVs_10.npy")
TVs_9 = np.load("TVs_9.npy")
TVs_8 = np.load("TVs_8.npy")
TVs_7 = np.load("TVs_7.npy")
TVs_6 = np.load("TVs_6.npy")
TVs_5 = np.load("TVs_5.npy")
#Real and Imag Separation
a1000 = TVs_1000.real
b1000 = TVs_1000.imag
a500 = TVs_500.real
b500 = TVs_500.imag
a100 = TVs_100.real
b100 = TVs_100.imag
a50 = TVs_50.real
b50 = TVs_50.imag
a10 = TVs_10.real
b10 = TVs_10.imag
a9 = TVs_9.real
b9 = TVs_9.imag
a8 = TVs_8.real
b8 = TVs_8.imag
a7 = TVs_7.real
b7 = TVs_7.imag
a6 = TVs_6.real
b6 = TVs_6.imag
a5 = TVs_5.real
b5 = TVs_5.imag
a = TV.real
b = TV.imag

clis = plt.cm.rainbow_r(np.linspace(0,1,10))

#Plt real
fig,axs=plt.subplots( 2, 1, figsize=(3.386, 4.8), sharey=False, sharex=False)#,gridspec_kw={'height_ratios': [1, 1, 0.12]})
fig.tight_layout(pad=2.5)

axs[0].plot(T_index, a ,color='k',linewidth=2,linestyle='-' )

axs[0].plot(T_index, a10 ,color=clis[7,:],linewidth=2,linestyle='-' )
axs[0].plot(T_index, a50 ,color=clis[6,:],linewidth=2,linestyle='-' )
axs[0].plot(T_index, a100 ,color=clis[5,:],linewidth=2,linestyle='-' )
axs[0].plot(T_index, a500 ,color=clis[4,:],linewidth=2,linestyle='-' )
axs[0].plot(T_index, a1000 ,color=clis[4,:],linewidth=2,linestyle='-'  )
axs[0].plot(T_index, a6 ,color=clis[8,:],linewidth=2,linestyle='-' )
axs[0].plot(T_index, a5 ,color=clis[0,:],linewidth=2,linestyle='-',label='$N_{\mathrm{cutoff}}=5$')
axs[0].plot([], [], color='grey', label='$N_{\mathrm{cutoff}}\geq6$',   linewidth=1.5,linestyle='--')
#plt.ylim(-0.55, 0.45)
#plt.yticks([-0.4,-0.2,0.0,0.2,0.4])
#axs[0].legend(loc='lower left', ncol=2, prop = {'size':7})
axs[0].set(xlabel='$t$', ylabel='Re$G_w$',ylim=(-0.6,0.65))
axs[0].text(-10.46, 0.55, '(a)')
axs[0].tick_params(pad=-3)


axs[1].plot(T_index, b ,color='k',linewidth=2,linestyle='-' )

axs[1].plot(T_index, b10 ,color=clis[7,:],linewidth=2,linestyle='-')
axs[1].plot(T_index, b50 ,color=clis[6,:],linewidth=2,linestyle='-' )
axs[1].plot(T_index, b100 ,color=clis[5,:],linewidth=2,linestyle='-' )
axs[1].plot(T_index, b500 ,color=clis[4,:],linewidth=2,linestyle='-' )
axs[1].plot(T_index, b1000 ,color=clis[4,:],linewidth=2,linestyle='-' )
axs[1].plot(T_index, b6 ,color=clis[8,:],linewidth=2,linestyle='-' )
axs[1].plot(T_index, b5 ,color=clis[0,:],linewidth=2,linestyle='-',label='$N_{\mathrm{cutoff}}=5$')
#axs[1].plot([], [], color='grey', label='$N_{\mathrm{cutoff}}\geq6$',   linewidth=1.5,linestyle='--')
#plt.ylim(-0.55, 0.45)
axs[1].legend(loc='best', ncol=1, prop = {'size':10},bbox_to_anchor=(1.1, 2.6))
axs[1].set(xlabel='$t$', ylabel='Im$G_w$',ylim=(-0.55,0.6))
axs[1].text(-10.46, 0.55,  '(b)')
axs[1].tick_params(pad=-3)

clis = plt.cm.rainbow_r(np.linspace(0,1,10))
cmap = (mpl.colors.ListedColormap([clis[8],clis[7],clis[6],clis[5],clis[4]]))
bounds = [6,10,50,100,500,1000]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

cbar=fig.colorbar(
    mpl.cm.ScalarMappable(cmap=cmap, norm=norm),ax=axs[:],
     orientation='horizontal',pad=0.13)
cbar.ax.tick_params(width=1,length=4)
#cbar.outline.set_linewidth(1)
axs[1].text(-8, -1.16, '$N_{\mathrm{cutoff}}$')#,fontfamily=['Times'])
#plt.subplots_adjust(hspace=0.5,wspace=0.1)
plt.savefig('Fig5.pdf',dpi=400,bbox_inches ='tight')
plt.show() 
