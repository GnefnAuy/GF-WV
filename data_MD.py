#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 17:15:51 2022

@author: aliciaglen
"""



from qutip import *
import numpy as np
from WM import OperatorA, TrueValue, Point_Final, WeakValue, Sampling, MDresult



if __name__ == "__main__":

    #define system
    N_cutoff = 6
    a = destroy(N_cutoff)
    H_free = a.dag()*a + 1/2
    x = 1/np.sqrt(2) * (a + a.dag())
    p = -1j/np.sqrt(2) * (a - a.dag())
    la = 0.2
    H_int = la * x * x * x * x
    H_tot = H_free + H_int
    c0 = 1
    c2 = -3/(2*np.sqrt(2))
    c4 = -np.sqrt(6)/8
    Omega = np.zeros([N_cutoff,1])
    Omega[0] = c0
    Omega[2] = la * c2
    Omega[4] = la * c4
    Omega = Qobj(Omega,dims=[[N_cutoff],[1]])
    i = Omega
    f = Omega
    #pointer_initial
    pointer = np.cos(0.87)*basis(2,0) + np.sin(0.87)*basis(2,1)
    xi = expect(sigmax(),pointer)
    yi = expect(sigmay(),pointer)
    zi = expect(sigmaz(),pointer)
    #eigen-states
    up = basis(2, 0)
    down = basis(2, 1)
    up_x = (up + down).unit()
    down_x = (up - down).unit()
    up_y = (1j*up - down).unit()
    down_y = (1j*up + down).unit()
    #Weak Measurement
    T = 1    
    t=5.1
    M=10000
    N=10000
    G_index = np.array([1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1])
    #G_index = np.array([0.4, 0.3])
    #N_index = np.array([50000, 500000])
    #N_index = np.array(range(5001,10001,1))
    DG=len(G_index)
    DN=len(N_index)
    OpA = OperatorA(H_tot,x,t)
    MD = np.zeros((DG,DN,M), dtype=complex)
    MX = np.zeros((DG,DN,M), dtype=complex)
    MY = np.zeros((DG,DN,M), dtype=complex)
    MZ = np.zeros((DG,DN,M), dtype=complex)
    
    for m in range(M):
        np.random.seed(10+m)
        RDN= np.random.rand(N)
        print('seed number',m)
        for j in range(DG):
            g = G_index[j]
            pointer_final = Point_Final(pointer,i,f,OpA,g,T)
            print('g=',g)
            PR_x, PR_y, PR_z = Sampling(RDN, N, pointer_final, up, down, up_x, down_x, up_y, down_y)

            for n in range(DN):
                n_= int(N_index[n])
                MX[j,n,m]= (np.sum(PR_x[1,0:n_])-np.sum(PR_x[0,0:n_]))/n_
                MY[j,n,m]= (np.sum(PR_y[1,0:n_])-np.sum(PR_y[0,0:n_]))/n_
                MZ[j,n,m]= (np.sum(PR_z[1,0:n_])-np.sum(PR_z[0,0:n_]))/n_
                MD[j,n,m] = MDresult(g,xi,yi,zi, MX[j,n,m], MY[j,n,m], MZ[j,n,m])
         
    #Save        
    np.save("MD.npy",MD)
    np.save("N_index.npy",N_index)
    np.save("M.npy",M)



       
