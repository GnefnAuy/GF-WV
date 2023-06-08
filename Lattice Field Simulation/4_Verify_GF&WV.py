
import numpy as np
import scipy.linalg as la
from qutip import *

A = qload('GFOP')
Omg = qload('gs')
R = qload('H')
Uh = qload('Uh')
T = np.load("T.npy")
N_total = np.load("N_total.npy")

#WV
Teta = [Uh[i].dag() * Omg  for i in range(T)]
Rw = [ (Teta[i].dag() * R[i] * Omg)[0,0] / (Teta[i].dag() * Omg)[0,0]for i in range(T)]
GF = [ (Omg.dag() * A[i] * Omg)[0,0] for i in range(T)]

#Verification
for i in range(T):
    print('Is G=Rw<T|O>',np.allclose(GF[i], Rw[i] * (Teta[i].dag() * Omg)[0,0] ))


qsave(Teta, 'Teta')
np.save("Rw.npy", Rw)
np.save("GF.npy", GF)