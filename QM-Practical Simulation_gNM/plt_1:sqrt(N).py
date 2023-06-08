
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns  
import matplotlib.ticker as ticker

N_index=np.load("N_index.npy")
DN = len(N_index)
CC = np.load("CC.npy")
DD = np.load("DD.npy")    

clis = plt.cm.rainbow_r(np.linspace(0,1,10))
fig,ax=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)
sns.set(style="darkgrid") 
sns.set_context("poster", font_scale = 1 , rc={"grid.linewidth": 3})

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-3,3)) 
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.offsetText.set_fontsize(0)
ax.xaxis.offsetText.set_fontsize(0)


plt.scatter(N_index, DD[0,:], s=10, label='g=1', color = clis[0,:],marker='*', cmap='rainbow')
plt.scatter(N_index, DD[1,:], s=10, label='g=0.9', color = clis[1,:],  marker='x', cmap='rainbow')
plt.scatter(N_index, DD[2,:], s=10, label='g=0.8', color = clis[2,:], marker='^', cmap='rainbow')
plt.scatter(N_index, DD[3,:], s=10, label='g=0.7', color = clis[3,:], marker='s', cmap='rainbow')
plt.scatter(N_index, DD[4,:], s=10, label='g=0.6', color=clis[4,:],  marker='h', cmap='rainbow') 
plt.scatter(N_index, DD[5,:], s=10, label='g=0.5', color=clis[5,:],marker='o', cmap='rainbow')
plt.scatter(N_index, DD[6,:], s=10, label='g=0.4', color=clis[6,:],  marker='d', cmap='rainbow')
plt.scatter(N_index, DD[7,:], s=10, label='g=0.3', color=clis[7,:], marker='<', cmap='rainbow')
plt.scatter(N_index, DD[8,:], s=10, label='g=0.2', color=clis[8,:], marker='p', cmap='rainbow')
plt.scatter(N_index, DD[9,:], s=10, label='g=0.1', color=clis[9,:],  marker='1', cmap='rainbow') 
ax.set_xlabel('N' + r' ($\times 10^{}$)'.format(int(np.log10(np.max(N_index)))))
ax.set_ylabel('$1/\delta^2$' + r' ($\times 10^{}$)'.format(int(np.log10(np.max(N_index)))))

#plt.yticks([0,1000, 2000 ])#C
#plt.yticks([0,1000, 2000 ,3000])#|C|
#plt.yticks([0,4000, 8000])#A
#plt.xticks([0, 2000, 4000])
plt.xlabel('N')
plt.ylabel('$1/\delta^2$')
plt.legend(loc='best', ncol=1, prop = {'size':7}, frameon=False)
#plt.savefig('C.png',dpi=400,bbox_inches ='tight')
plt.show()







    
    