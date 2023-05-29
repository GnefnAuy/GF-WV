from qutip import *
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#Import
TV=np.load("TV.npy")
WV=np.load("WV.npy")
MD=np.load("MD.npy")
G_index = np.load("G_index.npy")
N_index=np.load("N_index.npy")
M=np.load("M.npy")
DN=len(N_index)
DG=len(G_index)

#Radial Vector
ov = np.zeros([DN,1])
#Tradeoff 
#Figure of Merit

for n in range(DN):
    AA = np.zeros([DG,DG,M])
    BB = np.zeros([DG,DG])
    RRV = (MD[:,n,:]-TV)/abs(TV)
    for i in range(DG):
        for j in range(DG):
            AA[i,j,:] = abs(RRV)[i,:]-abs(RRV)[j,:]
            BB[i,j] = (AA[i,j,:]<0).sum()
            CC = (BB>(M/2))
            CC_ = DataFrame(CC,index=G_index)
            ov[n] = CC_.sum(axis=1).idxmax() 
OV = DataFrame(ov, index=N_index, columns=['g_optimal'])     
OV.to_excel('data.xlsx', index=True)    
OV.to_csv('data.csv', index=True)


