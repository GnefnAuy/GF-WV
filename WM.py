#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 13:52:23 2022

@author: yuan
"""

import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

#ideal WV=GF
def OperatorA(H_tot,x,t):
    xt = (1j*t*H_tot).expm() * x * (-1j*t*H_tot).expm()
    A= xt * x
    return A

def TrueValue(OpA,i,f):
    tv = f.dag()*OpA*i/(np.array(f.dag()*i)[0][0])
    tv = np.array(tv)[0][0]
    return tv

def Point_Final(pointer,i,f,OpA,g,T):
    #evolution of WM
    rho = ket2dm(tensor(i,pointer))
    H = g * tensor(OpA,sigmay())
    Uleft = (-1j * T * H).expm()
    Uright = (1j * T * H.dag()).expm()
    rho_ent = Uleft * rho * Uright
    #post-selection
    Pf = tensor(tensor(f,f.dag()),qeye(2))
    Pf = Qobj(np.array(Pf),dims=[[6, 2], [6, 2]])
    rho_final = Pf * rho_ent * Pf
    pointer_fin = rho_final.ptrace(1)/np.trace(rho_final.ptrace(1))
    return pointer_fin


def WeakValue(g,xi,yi,zi,pointer_fin):
    xf= expect(sigmax(),pointer_fin)
    yf= expect(sigmay(),pointer_fin)
    zf= expect(sigmaz(),pointer_fin)
    b = (yf-yi)/(2*g*(1-yi*yi))
    a = (zf-zi+2*g*b*zi*yi)/(-2*g*xi)
    wv = a+1j*b
    return wv


def Sampling(RDN, N, pointer_final, up, down, up_x, down_x, up_y, down_y):

    PR_x = np.zeros([2,N])
    PR_y = np.zeros([2,N])
    PR_z = np.zeros([2,N])
    
    px1=np.array(down_x.dag()*pointer_final*down_x)[0,0]
    py1=np.array(down_y.dag()*pointer_final*down_y)[0,0] 
    pz1=np.array(down.dag()*pointer_final*down)[0,0]

    for k in range(N):
        if RDN[k] >= px1:
            PR_x[1,k] = 1
        else:
            PR_x[0,k] = 1
            
        if RDN[k] >= py1:
            PR_y[1,k] = 1
        else:
            PR_y[0,k] = 1
            
        if RDN[k] >= pz1:
            PR_z[1,k] = 1
        else:
            PR_z[0,k] = 1
            
    return PR_x, PR_y, PR_z


def MDresult(g,xi,yi,zi, MX, MY, MZ):
    xf, yf, zf = MX, MY, MZ
    IM=(yf-yi)/(2*g*(1-yi*yi))
    RM=(zf-zi+2*g*IM*zi*yi)/(-2*g*xi)
    MD= RM+1j*IM
    return MD




 
