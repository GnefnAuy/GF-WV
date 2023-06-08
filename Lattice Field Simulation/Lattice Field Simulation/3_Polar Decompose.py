
import numpy as np
from qutip import *

GFOP = qload('GFOP')
phi = qload('phi')
N_total = np.load("N_total.npy")
T = np.load("T.npy")


Uh = np.zeros((T, N_total , N_total), dtype=complex) 
H = np.zeros((T, N_total , N_total), dtype=complex) 

#Polar Decompose
for i in range(T):
    U, s, V = np.linalg.svd(GFOP[i].full())
    S = np.diag(s)
    Uh[i] = U @ V
    H[i] = V.conj().T @ S @ V
    print('\nVerify Plolar Decompose')
    print("Is Uh unitary?")
    print(np.allclose(np.eye(Uh[i].shape[0]), Uh[i] @ Uh[i].conj().T))
    print("Is H Hermitian?")
    print(np.allclose(H[i], H[i].conj().T))
    print("Is A = UH?")
    print(np.allclose(GFOP[i], Uh[i] @ H[i]))

Uh = [ Qobj(Uh[i],dims = phi[0].dims)  for i in range(T)]
H = [ Qobj(H[i], dims = phi[0].dims)  for i in range(T)]
qsave(H, 'H')
qsave(Uh, 'Uh')






