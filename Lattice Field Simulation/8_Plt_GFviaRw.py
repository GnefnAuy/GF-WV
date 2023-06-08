
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import seaborn as sns  
sns.set(style="darkgrid")
sns.set_context("poster", font_scale = 3/4 , rc={"grid.linewidth": 9/4})

T = np.load("T.npy")
T_index = np.load("t_.npy")

Omg = qload('gs')
Teta = qload('Teta')
b_wm = np.load('b_wm.npy')
a_wm = np.load('a_wm.npy')
Rw_wm = a_wm+1j*b_wm
GF_wm = Rw_wm*0
for i in range(T):
    GF_wm[:,i] = (Teta[i].dag()*Omg)[0,0] * Rw_wm[:,i]

A = GF_wm.real
#A = np.roll(A,3,axis=1)
B = GF_wm.imag
#B = np.roll(B,3,axis=1)
M = abs(GF_wm)
#M = np.roll(M,3,axis=1)
GF = np.load("GF.npy")
#GF = np.roll(GF,3,axis=0)
b = GF.imag
a = GF.real
m = abs(GF) 
#T_index=np.arange(0,5,1)

clis = plt.cm.rainbow_r(np.linspace(0,1,10))

#Plt real
fig1,ax1=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)

plt.plot(T_index, A[9,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[9,:]) 
plt.plot(T_index, A[8,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[8,:])
plt.plot(T_index, A[7,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[7,:])
plt.plot(T_index, A[6,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[6,:])
plt.plot(T_index, A[5,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[5,:])
plt.plot(T_index, A[4,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[4,:]) 
plt.plot(T_index, A[3,:],   linewidth=1.5,linestyle='--', marker='x', color = clis[3,:])
plt.plot(T_index, A[2,:],   linewidth=1.5,linestyle='--', marker='x', color = clis[2,:])
plt.plot(T_index, A[1,:],   linewidth=1.5,linestyle='--', marker='x', color = clis[1,:])
plt.plot(T_index, A[0,:],   linewidth=1.5,linestyle='--', marker='x', color = clis[0,:])
plt.plot(T_index, a ,color='#4a488e',linewidth=2,linestyle='-', marker='.',label='true value')
plt.plot([], [], color='grey', label='g', linestyle='--', linewidth=1.5, marker='x')

plt.legend(loc='best', ncol=1, prop = {'size':12})
plt.xticks(T_index)
plt.xlabel('$t$')
plt.ylabel('Re$G(t,0)$')
plt.savefig('Re_G.png',dpi=400,bbox_inches ='tight')
plt.show() 



#Plt imag
fig2,ax2=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)

plt.plot(T_index, B[9,:],   linewidth=1.5,linestyle='--', marker='x',  color=clis[9,:]) 
plt.plot(T_index, B[8,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[8,:])
plt.plot(T_index, B[7,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[7,:])
plt.plot(T_index, B[6,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[6,:])
plt.plot(T_index, B[5,:],   linewidth=1.5,linestyle='--', marker='x',  color=clis[5,:])
plt.plot(T_index, B[4,:],   linewidth=1.5,linestyle='--', marker='x', color=clis[4,:]) 
plt.plot(T_index, B[3,:],   linewidth=1.5,linestyle='--', marker='x',  color = clis[3,:])
plt.plot(T_index, B[2,:],   linewidth=1.5,linestyle='--', marker='x', color = clis[2,:])
plt.plot(T_index, B[1,:],   linewidth=1.5,linestyle='--', marker='x', color = clis[1,:])
plt.plot(T_index, B[0,:],   linewidth=1.5,linestyle='--', marker='x', color = clis[0,:])
plt.plot(T_index, b ,color='#4a488e',linewidth=2,linestyle='-', marker='.', label='true value')
plt.plot([], [], color='grey', label='g', linestyle='--',  linewidth=1.5, marker='x')


plt.legend(loc='best', ncol=1, prop = {'size':12})
plt.xticks(T_index)
plt.xlabel('$t$')
plt.ylabel('Im$G(t,0)$')
plt.savefig('Im_G.png',dpi=400,bbox_inches ='tight')
plt.show() 


#Plt abs
fig2,ax2=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)

plt.plot(T_index, M[9,:],   linewidth=1.5,linestyle='--', marker='x',   color=clis[9,:]) 
plt.plot(T_index, M[8,:],   linewidth=1.5,linestyle='--', marker='x',   color=clis[8,:])
plt.plot(T_index, M[7,:],   linewidth=1.5,linestyle='--', marker='x',   color=clis[7,:])
plt.plot(T_index, M[6,:],   linewidth=1.5,linestyle='--', marker='x',   color=clis[6,:])
plt.plot(T_index, M[5,:],   linewidth=1.5,linestyle='--', marker='x',   color=clis[5,:])
plt.plot(T_index, M[4,:],   linewidth=1.5,linestyle='--', marker='x',   color=clis[4,:]) 
plt.plot(T_index, M[3,:],   linewidth=1.5,linestyle='--', marker='x',   color = clis[3,:])
plt.plot(T_index, M[2,:],   linewidth=1.5,linestyle='--', marker='x',   color = clis[2,:])
plt.plot(T_index, M[1,:],   linewidth=1.5,linestyle='--', marker='x',   color = clis[1,:])
plt.plot(T_index, M[0,:],   linewidth=1.5,linestyle='--', marker='x',   color = clis[0,:])
plt.plot(T_index, m ,color='#4a488e',linewidth=2,linestyle='-',marker='.', label='true value')
plt.plot([], [], color='grey', label='g', linestyle='--', linewidth=1.5, marker='x')


plt.legend(loc='best', ncol=1, prop = {'size':12})
plt.xticks(T_index)
plt.xlabel('$t$')
plt.ylabel('$|G(t,0)|$')
plt.savefig('abs_G.png',dpi=400,bbox_inches ='tight')
plt.show() 
