
import numpy as np
from qutip import *
import scipy.linalg as la
import math

D = 2 
L_, N= 1.5, 5  
L = int(2*L_+1)
T = L
N_total= N**((L)**(D-1))
dx = 1
dt = 1
dk = 2*np.pi/L
x = np.arange(-L_,L_+1) * dx
t_ = x
k = x * dk

a = destroy(N)
ad = a.dag()
I = qeye(N)
if L==1:
    A = [a]
    Ad = [ad]
elif L==2:
    A = [tensor(a,I) , tensor(I,a)]
    Ad = [tensor(ad,I), tensor(I,ad)]
elif L==3:
    A = [ tensor(a,I,I), tensor(I,a,I), tensor(I,I,a)]
    Ad = [ tensor(ad,I,I), tensor(I,ad,I), tensor(I,I,ad)]
elif L==4:
    A = [ tensor(a,I,I,I), tensor(I,a,I,I), tensor(I,I,a,I), tensor(I,I,I,a)]
    Ad = [ tensor(ad,I,I,I), tensor(I,ad,I,I), tensor(I,I,ad,I), tensor(I,I,I,ad)]
elif L==5:
    A = [ tensor(a,I,I,I,I), tensor(I,a,I,I,I), tensor(I,I,a,I,I), tensor(I,I,I,a,I), tensor(I,I,I,I,a)]
    Ad = [ tensor(ad,I,I,I,I), tensor(I,ad,I,I,I), tensor(I,I,ad,I,I), tensor(I,I,I,ad,I), tensor(I,I,I,I,ad)]


# Define the mass and coupling constant
M = 1
La = 0.2

# Define the field operator as a numpy array
mode_x = [[ 1/(np.sqrt(2)) * np.power(M**2 + k[j]**2, -1/4) * (A[j] * np.exp(-1j*k[j]*x[i]) ) for j in range(L)]for i in range(L)]
mode_p = [[ (-1j) * 1/(np.sqrt(2)) * np.power(M**2 + k[j]**2, 1/4) * (A[j] * np.exp(-1j*k[j]*x[i]) ) for j in range(L)]for i in range(L)]
mode_dx = [[ (-1j) * k[j] /(np.sqrt(2)) * np.power(M**2 + k[j]**2, -1/4) * (A[j] * np.exp(-1j*k[j]*x[i]) ) for j in range(L)]for i in range(L)]
phi =  [dk/(2*np.pi) * np.sqrt(L) * ( sum(mode_x[i])+ sum(mode_x[i]).dag() ) for i in range(L)]
pi = [ dk/(2*np.pi) * np.sqrt(L) * ( sum(mode_p[i])+ sum(mode_p[i]).dag() ) for i in range(L)]
dphi =  [dk/(2*np.pi) * np.sqrt(L) * ( sum(mode_dx[i])+ sum(mode_dx[i]).dag() ) for i in range(L)]
#dphi = [ (phi[(i+1)%L]-phi[(i-1)%L] )/dx  for i in range(L)]
#V_commu = ( phi[0]*pi[0] - pi[0]*phi[0] ).full()
mode_H_KG = [0.5*( pi[i]**2 + dphi[i]**2 + M**2 * phi[i]**2 ) for i in range(L)]
H_KG =  dx * sum(mode_H_KG)

H_int = sum( [ La/math.factorial(4) * phi[i] **4  for i in range(L)] )
H_tot = H_KG + H_int

# check if the matrix is diagonal
print(H_tot)
is_diag = np.allclose(H_KG, np.diag(np.diagonal(H_KG)))
print('Diagonal:', is_diag)

# Heisenberg Picture_Time evolution
phi_t = [[ (1j*H_tot*t).expm() * phi[i] * (-1j*H_tot*t).expm() for i in range(L)]for t in t_]
GFOP =  [ ]
for i in range(T):
    if t_[i]<0:
        add = phi[int(L/2)] * phi_t[i][int(L/2)]
        print(t_[i])
    else:
        add = phi_t[i][int(L/2)]*phi[int(L/2)]
        print('>',t_[i])
    GFOP.append(add)
print(GFOP)
   
qsave(phi_t, 'phi_t')  
qsave(phi, 'phi')
qsave(H_KG, 'H_KG')
qsave(H_tot, 'H_tot')
qsave(GFOP, 'GFOP')

np.save("N_total.npy", N_total)
np.save("x.npy", x)
np.save("T.npy", T)
np.save("t_.npy", t_)
