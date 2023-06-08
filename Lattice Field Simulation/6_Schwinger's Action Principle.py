
import numpy as np
from qutip import *
import datetime
T = np.load("T.npy")
N_total = np.load("N_total.npy")
Rw = np.load("Rw.npy")

Omg = qload('gs')
Teta = qload('Teta')
R = qload('H')

#define the spin appratus
is1 = basis(2,0)
fs1 = (basis(2,0)+basis(2,1)).unit()
is2 = (1j*basis(2,0)+basis(2,1)).unit()
fs2 = basis(2,1)
I1 = tensor(Omg,is1)
I2 = tensor(Omg,is2)

sx = sigmax()
Sgw1 = (fs1.dag()*sx*is1/(fs1.dag()*is1)[0,0])[0,0]
Sgw2 = (fs2.dag()*sx*is2/(fs2.dag()*is2)[0,0])[0,0]

# coupling constant
G = np.arange(10,0,-1)
G_= G/10
DG=len(G)

a_wm = np.zeros([DG,T],dtype=complex)
b_wm = np.zeros([DG,T],dtype=complex)
#b_wm = np.load('b_wm01234.npy')
#a_wm = np.load('a_wm01234.npy')

#test t=1  multiprocess
time0 = datetime.datetime.now()
for i in range(T):
    print('\nRound',i,': t_{index}=',i)
    H_int = tensor(R[i],sx)
    #EH = (-1j*G_[-1]*H_int).expm('sparse')
    F1 = tensor(Teta[i],fs1) 
    F2 = tensor(Teta[i],fs2)
    P1i = (tensor(Teta[i],fs1).dag() * I1 ).norm()**2
    P2i = (F2.dag() * I2).norm()**2
    
    for j in range(DG):
        print('\nfor g =', G_[j])
        time1 = datetime.datetime.now()
        print('Start calculating expm at:',time1)
        P1f = (F1.dag() * (-1j*G_[j]*H_int).expm() * I1).norm()**2
        P2f = (F2.dag() * (-1j*G_[j]*H_int).expm() * I2 ).norm()**2
        time2 = datetime.datetime.now()
        print('Finish calculating expm at:',time2)
        print('Calculating time for expm',time2-time1)

        b_wm[j,i] = 0.5*(np.log(P1f) - np.log(P1i))/G_[j] 
        a_wm[j,i] = 0.5*(np.log(P2f) - np.log(P2i))/G_[j] 
        
    

timef = datetime.datetime.now()
print('running time',timef-time0)
         
        
np.save("b_wm.npy", b_wm)
np.save("a_wm.npy", a_wm)
np.save("G_.npy", G_)


