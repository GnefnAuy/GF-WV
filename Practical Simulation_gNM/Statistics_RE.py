
from qutip import *
import numpy as np

#Import
TV=np.load("TV.npy")
WV=np.load("WV.npy")
MD=np.load("MD.npy")
G_index = np.load("G_index.npy")
N_index=np.load("N_index.npy")
M=np.load("M.npy")
DN=len(N_index)
DG=len(G_index)
    
MD = MD
TV = TV
RL = (MD-TV).imag/abs(TV)
#Statistics of complex average and dispersion
CC = np.zeros((DG,DN), dtype=complex)
DD = np.zeros((DG,DN))

#expectation & variance
for j in range(DG):
    for n in range(DN):
        CC[j,n] = np.mean(RL[j,n,:])
        for m in range(M):
            DD [j,n] += abs(RL[j,n,m]- CC[j,n])**2
        DD [j,n] =   M / DD [j,n]
D = 2/np.sqrt(DD)

np.save("CC.npy",CC)
np.save("DD.npy",DD)
np.save("D.npy",D)
