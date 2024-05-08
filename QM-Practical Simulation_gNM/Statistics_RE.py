# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:45:34 2022

@author: Administrator
"""

import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

#Import
TV=np.load("TV.npy")
WV=np.load("WV.npy")
MD=np.load("MD.npy")
G_index = np.load("G_index.npy")
N_index=np.load("N_index.npy")
M=int(np.load("M.npy"))
DN=len(N_index)
DG=len(G_index)
    
MD = MD
TV = TV
RL = np.zeros((4,DG,DN,M), dtype=complex)

RL[0] = (MD-TV)/abs(TV) #c
RL[1] = abs(MD-TV)/abs(TV) #s = abs
RL[2] = (MD-TV).real/abs(TV) #a
RL[3] = (MD-TV).imag/abs(TV) #b

#Statistics of complex average and dispersion
RL_AVE = np.zeros((4,DG,DN), dtype=complex)
RL_DEV = np.zeros((4,DG,DN))

#expectation & variance
for j in range(DG):
    for n in range(DN):
        for i in range(4):
            RL_AVE[i,j,n] = np.mean(RL[i,j,n,:])
            for m in range(M):
                RL_DEV [i,j,n] += abs(RL[i,j,n,m]- RL_AVE[i,j,n])**2
            RL_DEV [i,j,n] =   M / RL_DEV [i,j,n]
    
Delta_ = 2/np.sqrt(RL_DEV)
RL_AVE = abs(RL_AVE)

np.save("RL_AVE.npy",RL_AVE)
np.save("RL_DEV.npy",RL_DEV)
np.save("Delta_.npy",Delta_)
