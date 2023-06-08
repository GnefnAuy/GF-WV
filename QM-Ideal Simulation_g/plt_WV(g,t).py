
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns  
sns.set(style="darkgrid")
sns.set_context("poster", font_scale = 3/4 , rc={"grid.linewidth": 9/4})
clis = plt.cm.rainbow_r(np.linspace(0,1,10))

#import
TV = np.load("TV.npy")
WV = np.load("WV.npy")
G_index = np.load("G_index.npy")
T_index = np.load("T_index.npy")
#Real and Imag Separation
a = TV.real
b = TV.imag
A = WV.real
B = WV.imag


#Plt real
fig1,ax1=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)
plt.plot(T_index, A[9,:],   linewidth=1.5,linestyle='--',   color=clis[9,:]) 
plt.plot(T_index, A[8,:],   linewidth=1.5,linestyle='--',   color=clis[8,:])
plt.plot(T_index, A[7,:],   linewidth=1.5,linestyle='--',   color=clis[7,:])
plt.plot(T_index, A[6,:],   linewidth=1.5,linestyle='--',   color=clis[6,:])
plt.plot(T_index, A[5,:],   linewidth=1.5,linestyle='--',   color=clis[5,:])
plt.plot(T_index, A[4,:],   linewidth=1.5,linestyle='--',   color=clis[4,:]) 
plt.plot(T_index, A[3,:],   linewidth=1.5,linestyle='--',   color=clis[3,:])
plt.plot(T_index, A[2,:],   linewidth=1.5,linestyle='--',   color=clis[2,:])
plt.plot(T_index, A[1,:],   linewidth=1.5,linestyle='--',   color=clis[1,:])
plt.plot(T_index, A[0,:],   linewidth=1.5,linestyle='--',   color=clis[0,:])
plt.plot(T_index, a ,color='#4a488e',linewidth=2,linestyle='-',label='true value')
plt.plot([], [], color='grey', label='g',   linewidth=1.5,linestyle='--')
plt.legend(loc='lower right', ncol=2, prop = {'size':14})
plt.ylim(-0.6,0.45)
plt.xlabel('$t$')
plt.ylabel('Re$A_w$')
plt.savefig('Real_WV.png',dpi=400,bbox_inches ='tight')
plt.show() 

#Plt imag
fig2,ax2=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)
plt.legend(loc='lower left', ncol=1, prop = {'size':14})
plt.plot(T_index, B[9,:],   linewidth=1.5,linestyle='--',   color=clis[9,:]) 
plt.plot(T_index, B[8,:],   linewidth=1.5,linestyle='--',   color=clis[8,:])
plt.plot(T_index, B[7,:],   linewidth=1.5,linestyle='--',   color=clis[7,:])
plt.plot(T_index, B[6,:],   linewidth=1.5,linestyle='--',   color=clis[6,:])
plt.plot(T_index, B[5,:],   linewidth=1.5,linestyle='--',   color=clis[5,:])
plt.plot(T_index, B[4,:],   linewidth=1.5,linestyle='--',   color=clis[4,:]) 
plt.plot(T_index, B[3,:],   linewidth=1.5,linestyle='--',   color=clis[3,:])
plt.plot(T_index, B[2,:],   linewidth=1.5,linestyle='--',   color=clis[2,:])
plt.plot(T_index, B[1,:],   linewidth=1.5,linestyle='--',   color=clis[1,:])
plt.plot(T_index, B[0,:],   linewidth=1.5,linestyle='--',   color=clis[0,:])
plt.plot(T_index, b ,color='#4a488e',  linewidth=2,linestyle='-',label='true value')
plt.plot([], [], color='grey', label='g',   linewidth=1.5,linestyle='--')
plt.legend(loc='lower right', ncol=2, prop = {'size':14})
plt.ylim(-0.6,0.45)
plt.xlabel('$t$')
plt.ylabel('Im$A_w$')
plt.savefig('Imag_WV.png',dpi=400,bbox_inches ='tight')
plt.show() 


    