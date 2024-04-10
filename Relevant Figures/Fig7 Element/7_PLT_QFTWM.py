#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:32:50 2023

@author: aliciaglenda
"""


import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import seaborn as sns  
sns.set(style="darkgrid")
sns.set_context("poster", font_scale = 3/4 , rc={"grid.linewidth": 9/4})

#import
B = np.load("b_wm.npy")
A = np.load("a_wm.npy")
M = np.sqrt (abs(A)**2 + abs(B)**2)
Rw = np.load("Rw.npy")
b = Rw.imag
a = Rw.real
m = abs(Rw)
G_index = np.load("G_.npy")
T_index = np.load("t_.npy")

clis = plt.cm.rainbow_r(np.linspace(0,1,10))

#Plt real
fig1,ax1=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)

plt.plot(T_index, A[9,:],   linewidth=1.5, linestyle='-',  color=clis[9,:]) 
plt.plot(T_index, A[8,:],   linewidth=1.5, linestyle='-',  color=clis[8,:])
plt.plot(T_index, A[7,:],   linewidth=1.5, linestyle='-',  color=clis[7,:])
plt.plot(T_index, A[6,:],   linewidth=1.5, linestyle='-',  color=clis[6,:])
plt.plot(T_index, A[5,:],   linewidth=1.5, linestyle='-',  color=clis[5,:])
plt.plot(T_index, A[4,:],   linewidth=1.5, linestyle='-',  color=clis[4,:]) 
plt.plot(T_index, A[3,:],   linewidth=1.5, linestyle='-',  color = clis[3,:])
plt.plot(T_index, A[2,:],   linewidth=1.5, linestyle='-',  color = clis[2,:])
plt.plot(T_index, A[1,:],   linewidth=1.5, linestyle='-',  color = clis[1,:])
plt.plot(T_index, A[0,:],   linewidth=1.5, linestyle='-',  color = clis[0,:])
plt.plot(T_index, a ,color='#4a488e',linewidth=2,linestyle='-'   ,label='true value')
plt.plot([], [], color='grey', label='g',  linestyle='-', linewidth=1.5 )

plt.legend(loc='best', ncol=1, prop = {'size':12})
#plt.xticks(T_index)
plt.xlabel('$t$')
plt.ylabel('Re$R_w$')
plt.savefig('Re_Rw.png',dpi=400,bbox_inches ='tight')
plt.show() 



#Plt imag
fig2,ax2=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)

plt.plot(T_index, B[9,:],   linewidth=1.5, linestyle='-',   color=clis[9,:]) 
plt.plot(T_index, B[8,:],   linewidth=1.5, linestyle='-',  color=clis[8,:])
plt.plot(T_index, B[7,:],   linewidth=1.5, linestyle='-',  color=clis[7,:])
plt.plot(T_index, B[6,:],   linewidth=1.5, linestyle='-',  color=clis[6,:])
plt.plot(T_index, B[5,:],   linewidth=1.5, linestyle='-',   color=clis[5,:])
plt.plot(T_index, B[4,:],   linewidth=1.5, linestyle='-',  color=clis[4,:]) 
plt.plot(T_index, B[3,:],   linewidth=1.5, linestyle='-',   color = clis[3,:])
plt.plot(T_index, B[2,:],   linewidth=1.5, linestyle='-',  color = clis[2,:])
plt.plot(T_index, B[1,:],   linewidth=1.5, linestyle='-',  color = clis[1,:])
plt.plot(T_index, B[0,:],   linewidth=1.5, linestyle='-',  color = clis[0,:])
plt.plot(T_index, b ,color='#4a488e',linewidth=2,linestyle='-'   , label='true value')
plt.plot([], [], color='grey', label='g',  linestyle='-',  linewidth=1.5 )


plt.legend(loc='best', ncol=1, prop = {'size':12})
#plt.xticks(T_index)
plt.xlabel('$t$')
plt.ylabel('Im$R_w$')
plt.savefig('Im_Rw.png',dpi=400,bbox_inches ='tight')
plt.show() 


#Plt mole
fig2,ax2=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)

plt.plot(T_index, M[9,:],   linewidth=1.5, linestyle='-',    color=clis[9,:]) 
plt.plot(T_index, M[8,:],   linewidth=1.5, linestyle='-',    color=clis[8,:])
plt.plot(T_index, M[7,:],   linewidth=1.5, linestyle='-',    color=clis[7,:])
plt.plot(T_index, M[6,:],   linewidth=1.5, linestyle='-',    color=clis[6,:])
plt.plot(T_index, M[5,:],   linewidth=1.5, linestyle='-',    color=clis[5,:])
plt.plot(T_index, M[4,:],   linewidth=1.5, linestyle='-',    color=clis[4,:]) 
plt.plot(T_index, M[3,:],   linewidth=1.5, linestyle='-',    color = clis[3,:])
plt.plot(T_index, M[2,:],   linewidth=1.5, linestyle='-',    color = clis[2,:])
plt.plot(T_index, M[1,:],   linewidth=1.5, linestyle='-',    color = clis[1,:])
plt.plot(T_index, M[0,:],   linewidth=1.5, linestyle='-',    color = clis[0,:])
plt.plot(T_index, m ,color='#4a488e',linewidth=2,linestyle='-' , label='true value')
plt.plot([], [], color='grey', label='g',  linestyle='-', linewidth=1.5 )


plt.legend(loc='best', ncol=1, prop = {'size':14})
plt.xlabel('$t$')
plt.ylabel('$|R_w|$')
plt.savefig('abs_Rw.png',dpi=400,bbox_inches ='tight')
plt.show() 
