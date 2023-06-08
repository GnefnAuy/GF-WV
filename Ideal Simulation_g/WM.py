
from qutip import *
import numpy as np

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



 