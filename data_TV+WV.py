#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:14:26 2022

@author: aliciaglenda
"""



from qutip import *
import numpy as np
from WM import OperatorA, TrueValue, Point_Final, WeakValue



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
    #Weak Measurement
    T = 1
    t=5.1
    #G_index = np.array([1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1])
    G_index = np.array([0.4, 0.3 ])
    DG=len(G_index)
    OpA = OperatorA(H_tot,x,t)
    
    #TV
    TV=TrueValue(OpA,i,f)
    #WV
    WV = np.zeros(DG, dtype=complex)
    for j in range(DG):
        g = G_index[j]
        pointer_final = Point_Final(pointer,i,f,OpA,g,T)
        print('g=',g)
        WV[j] = WeakValue(g,xi,yi,zi,pointer_final)

    #Save
    np.save("TV.npy",TV)     
    np.save("WV.npy",WV)
    np.save("G_index.npy",G_index)




       
