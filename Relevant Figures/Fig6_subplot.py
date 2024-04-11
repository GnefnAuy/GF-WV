import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import seaborn as sns  

from matplotlib import colors  
from matplotlib import rc
#plt.rcdefaults()
mpl.rcParams['font.family']= 'sans-serif'
mpl.rcParams['font.serif'] = 'Computer Modern Roman'
mpl.rcParams['font.sans-serif']= 'Computer Modern Sans Serif'
mpl.rcParams['mathtext.fontset']='stix'
mpl.rcParams['mathtext.rm'] = 'sans'
mpl.rcParams['mathtext.it'] = 'sans:italic'
mpl.rcParams['mathtext.default']='it'
mpl.rcParams['mathtext.bf']= 'sans:bold'


sns.set(style="darkgrid")
sns.set_context("poster", font_scale = 0.2 , rc={"grid.linewidth": 1})


N_index=np.load("N_index.npy")/1000
DN = len(N_index)

RL_AVE = np.load("RL_AVE.npy")
RL_DEV = np.load("RL_DEV.npy") /1000
Delta_ = np.load("Delta_.npy")



clis = plt.cm.rainbow_r(np.linspace(0,1,10))

#Plt real
fig,axs=plt.subplots( 2, 4, figsize=(6.772, 1.7), sharey=False, sharex=False)#,layout='constrained')#,gridspec_kw={'height_ratios': [1, 1, 1, 0.12]})
plt.subplots_adjust(hspace=0.9,wspace=0.5)

axs[0,0].errorbar(N_index, RL_AVE[0,9,:], xerr=None, yerr=Delta_[0,9,:],capsize=0.6,fmt='.', label='g=0.1', color = clis[9,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].errorbar(N_index, RL_AVE[0,8,:], xerr=None, yerr=Delta_[0,8,:],capsize=0.6,fmt='.', label='g=0.2', color = clis[8,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].errorbar(N_index, RL_AVE[0,7,:], xerr=None, yerr=Delta_[0,7,:],capsize=0.6,fmt='.', label='g=0.3', color = clis[7,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].errorbar(N_index, RL_AVE[0,6,:], xerr=None, yerr=Delta_[0,6,:],capsize=0.6,fmt='.', label='g=0.4', color = clis[6,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].errorbar(N_index, RL_AVE[0,5,:], xerr=None, yerr=Delta_[0,5,:],capsize=0.6,fmt='.', label='g=0.5', color = clis[5,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].errorbar(N_index, RL_AVE[0,4,:], xerr=None, yerr=Delta_[0,4,:],capsize=0.6,fmt='.', label='g=0.6', color = clis[4,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].errorbar(N_index, RL_AVE[0,3,:], xerr=None, yerr=Delta_[0,3,:],capsize=0.6,fmt='.', label='g=0.7', color = clis[3,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].errorbar(N_index, RL_AVE[0,2,:], xerr=None, yerr=Delta_[0,2,:],capsize=0.6,fmt='.', label='g=0.8', color = clis[2,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].errorbar(N_index, RL_AVE[0,1,:], xerr=None, yerr=Delta_[0,1,:],capsize=0.6,fmt='.', label='g=0.9', color = clis[1,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].errorbar(N_index, RL_AVE[0,0,:], xerr=None, yerr=Delta_[0,0,:],capsize=0.6,fmt='.', label='g=1', color = clis[0,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,0].set_title('(a)  $Z_{\mathrm{RV}}$')
axs[0,0].set(xlabel='$10^3~N$', ylabel='$\overline{Z}$',ylim=(-1,1.3))

axs[0,1].errorbar(N_index, RL_AVE[1,9,:], xerr=None, yerr=Delta_[1,9,:],capsize=0.6,fmt='.', label='g=0.1', color = clis[9,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].errorbar(N_index, RL_AVE[1,8,:], xerr=None, yerr=Delta_[1,8,:],capsize=0.6,fmt='.', label='g=0.2', color = clis[8,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].errorbar(N_index, RL_AVE[1,7,:], xerr=None, yerr=Delta_[1,7,:],capsize=0.6,fmt='.', label='g=0.3', color = clis[7,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].errorbar(N_index, RL_AVE[1,6,:], xerr=None, yerr=Delta_[1,6,:],capsize=0.6,fmt='.', label='g=0.4', color = clis[6,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].errorbar(N_index, RL_AVE[1,5,:], xerr=None, yerr=Delta_[1,5,:],capsize=0.6,fmt='.', label='g=0.5', color = clis[5,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].errorbar(N_index, RL_AVE[1,4,:], xerr=None, yerr=Delta_[1,4,:],capsize=0.6,fmt='.', label='g=0.6', color = clis[4,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].errorbar(N_index, RL_AVE[1,3,:], xerr=None, yerr=Delta_[1,3,:],capsize=0.6,fmt='.', label='g=0.7', color = clis[3,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].errorbar(N_index, RL_AVE[1,2,:], xerr=None, yerr=Delta_[1,2,:],capsize=0.6,fmt='.', label='g=0.8', color = clis[2,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].errorbar(N_index, RL_AVE[1,1,:], xerr=None, yerr=Delta_[1,1,:],capsize=0.6,fmt='.', label='g=0.9', color = clis[1,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].errorbar(N_index, RL_AVE[1,0,:], xerr=None, yerr=Delta_[1,0,:],capsize=0.6,fmt='.', label='g=1', color = clis[0,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,1].set_title('(b)  $|Z_{\mathrm{RV}}|$')
axs[0,1].set(xlabel='$10^3~N$', ylabel='$\overline{Z}$',ylim=(0,1.2))

axs[0,2].errorbar(N_index, RL_AVE[2,9,:], xerr=None, yerr=Delta_[2,9,:],capsize=0.6,fmt='.', label='g=0.1', color = clis[9,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].errorbar(N_index, RL_AVE[2,8,:], xerr=None, yerr=Delta_[2,8,:],capsize=0.6,fmt='.', label='g=0.2', color = clis[8,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].errorbar(N_index, RL_AVE[2,7,:], xerr=None, yerr=Delta_[2,7,:],capsize=0.6,fmt='.', label='g=0.3', color = clis[7,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].errorbar(N_index, RL_AVE[2,6,:], xerr=None, yerr=Delta_[2,6,:],capsize=0.6,fmt='.', label='g=0.4', color = clis[6,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].errorbar(N_index, RL_AVE[2,5,:], xerr=None, yerr=Delta_[2,5,:],capsize=0.6,fmt='.', label='g=0.5', color = clis[5,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].errorbar(N_index, RL_AVE[2,4,:], xerr=None, yerr=Delta_[2,4,:],capsize=0.6,fmt='.', label='g=0.6', color = clis[4,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].errorbar(N_index, RL_AVE[2,3,:], xerr=None, yerr=Delta_[2,3,:],capsize=0.6,fmt='.', label='g=0.7', color = clis[3,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].errorbar(N_index, RL_AVE[2,2,:], xerr=None, yerr=Delta_[2,2,:],capsize=0.6,fmt='.', label='g=0.8', color = clis[2,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].errorbar(N_index, RL_AVE[2,1,:], xerr=None, yerr=Delta_[2,1,:],capsize=0.6,fmt='.', label='g=0.9', color = clis[1,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].errorbar(N_index, RL_AVE[2,0,:], xerr=None, yerr=Delta_[2,0,:],capsize=0.6,fmt='.', label='g=1', color = clis[0,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,2].set_title('(c)  Re$\{Z_{\mathrm{RV}}\}$')
axs[0,2].set(xlabel='$10^3~N$', ylabel='$\overline{Z}$',ylim=(-0.5,0.7))

axs[0,3].errorbar(N_index, RL_AVE[3,9,:], xerr=None, yerr=Delta_[3,9,:],capsize=0.6,fmt='.', label='g=0.1', color = clis[9,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].errorbar(N_index, RL_AVE[3,8,:], xerr=None, yerr=Delta_[3,8,:],capsize=0.6,fmt='.', label='g=0.2', color = clis[8,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].errorbar(N_index, RL_AVE[3,7,:], xerr=None, yerr=Delta_[3,7,:],capsize=0.6,fmt='.', label='g=0.3', color = clis[7,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].errorbar(N_index, RL_AVE[3,6,:], xerr=None, yerr=Delta_[3,6,:],capsize=0.6,fmt='.', label='g=0.4', color = clis[6,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].errorbar(N_index, RL_AVE[3,5,:], xerr=None, yerr=Delta_[3,5,:],capsize=0.6,fmt='.', label='g=0.5', color = clis[5,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].errorbar(N_index, RL_AVE[3,4,:], xerr=None, yerr=Delta_[3,4,:],capsize=0.6,fmt='.', label='g=0.6', color = clis[4,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].errorbar(N_index, RL_AVE[3,3,:], xerr=None, yerr=Delta_[3,3,:],capsize=0.6,fmt='.', label='g=0.7', color = clis[3,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].errorbar(N_index, RL_AVE[3,2,:], xerr=None, yerr=Delta_[3,2,:],capsize=0.6,fmt='.', label='g=0.8', color = clis[2,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].errorbar(N_index, RL_AVE[3,1,:], xerr=None, yerr=Delta_[3,1,:],capsize=0.6,fmt='.', label='g=0.9', color = clis[1,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].errorbar(N_index, RL_AVE[3,0,:], xerr=None, yerr=Delta_[3,0,:],capsize=0.6,fmt='.', label='g=1', color = clis[0,:],ms=2, mew=0.2,elinewidth=0.5)
axs[0,3].set_title('(d)  Im$\{Z_{\mathrm{RV}}\}$')
axs[0,3].set(xlabel='$10^3~N$', ylabel='$\overline{Z}$',ylim=(-0.5,0.7))

axs[1,0].scatter(N_index, RL_DEV[0,0,:], s=5, linewidth=0.1, color = clis[0,:],marker='*' )
axs[1,0].scatter(N_index, RL_DEV[0,1,:], s=5, linewidth=0.3, color = clis[1,:],  marker='x' )
axs[1,0].scatter(N_index, RL_DEV[0,2,:], s=5, linewidth=0.1, color = clis[2,:], marker='^' )
axs[1,0].scatter(N_index, RL_DEV[0,3,:], s=5, linewidth=0.1, color = clis[3,:], marker='s' )
axs[1,0].scatter(N_index, RL_DEV[0,4,:], s=5, linewidth=0.1, color=clis[4,:],  marker='h' ) 
axs[1,0].scatter(N_index, RL_DEV[0,5,:], s=5, linewidth=0.1, color=clis[5,:],marker='o' )
axs[1,0].scatter(N_index, RL_DEV[0,6,:], s=5, linewidth=0.1, color=clis[6,:],  marker='d' )
axs[1,0].scatter(N_index, RL_DEV[0,7,:], s=5, linewidth=0.1, color=clis[7,:], marker='<' )
axs[1,0].scatter(N_index, RL_DEV[0,8,:], s=5, linewidth=0.1, color=clis[8,:], marker='p' )
axs[1,0].scatter(N_index, RL_DEV[0,9,:], s=5, linewidth=0.1, color=clis[9,:],  marker='1' ) 
axs[1,0].set_title('(e)  $Z_{\mathrm{RV}}$')
axs[1,0].set(xlabel='$10^3~N$', ylabel='$10^3~1/\delta^2$')

axs[1,1].scatter(N_index, RL_DEV[1,0,:], s=5, linewidth=0.1, color = clis[0,:],marker='*' )
axs[1,1].scatter(N_index, RL_DEV[1,1,:], s=5, linewidth=0.3, color = clis[1,:],  marker='x' )
axs[1,1].scatter(N_index, RL_DEV[1,2,:], s=5, linewidth=0.1, color = clis[2,:], marker='^' )
axs[1,1].scatter(N_index, RL_DEV[1,3,:], s=5, linewidth=0.1, color = clis[3,:], marker='s' )
axs[1,1].scatter(N_index, RL_DEV[1,4,:], s=5, linewidth=0.1, color=clis[4,:],  marker='h' ) 
axs[1,1].scatter(N_index, RL_DEV[1,5,:], s=5, linewidth=0.1, color=clis[5,:],marker='o' )
axs[1,1].scatter(N_index, RL_DEV[1,6,:], s=5, linewidth=0.1, color=clis[6,:],  marker='d' )
axs[1,1].scatter(N_index, RL_DEV[1,7,:], s=5, linewidth=0.1, color=clis[7,:], marker='<' )
axs[1,1].scatter(N_index, RL_DEV[1,8,:], s=5, linewidth=0.1, color=clis[8,:], marker='p' )
axs[1,1].scatter(N_index, RL_DEV[1,9,:], s=5, linewidth=0.1, color=clis[9,:],  marker='1' ) 
axs[1,1].set_title('(f)  $|Z_{\mathrm{RV}}|$')
axs[1,1].set(xlabel='$10^3~N$', ylabel='$10^3~1/\delta^2$')

axs[1,2].scatter(N_index, RL_DEV[2,0,:], s=5, linewidth=0.1, color = clis[0,:],marker='*' )
axs[1,2].scatter(N_index, RL_DEV[2,1,:], s=5, linewidth=0.3, color = clis[1,:],  marker='x' )
axs[1,2].scatter(N_index, RL_DEV[2,2,:], s=5, linewidth=0.1, color = clis[2,:], marker='^' )
axs[1,2].scatter(N_index, RL_DEV[2,3,:], s=5, linewidth=0.1, color = clis[3,:], marker='s' )
axs[1,2].scatter(N_index, RL_DEV[2,4,:], s=5, linewidth=0.1, color=clis[4,:],  marker='h' ) 
axs[1,2].scatter(N_index, RL_DEV[2,5,:], s=5, linewidth=0.1, color=clis[5,:],marker='o' )
axs[1,2].scatter(N_index, RL_DEV[2,6,:], s=5, linewidth=0.1, color=clis[6,:],  marker='d' )
axs[1,2].scatter(N_index, RL_DEV[2,7,:], s=5, linewidth=0.1, color=clis[7,:], marker='<' )
axs[1,2].scatter(N_index, RL_DEV[2,8,:], s=5, linewidth=0.1, color=clis[8,:], marker='p' )
axs[1,2].scatter(N_index, RL_DEV[2,9,:], s=5, linewidth=0.1, color=clis[9,:],  marker='1' ) 
axs[1,2].set_title('(g)  Re$\{Z_{\mathrm{RV}}\}$')
axs[1,2].set(xlabel='$10^3~N$', ylabel='$10^3~1/\delta^2$')

axs[1,3].scatter(N_index, RL_DEV[3,0,:], s=5, linewidth=0.1, color = clis[0,:],marker='*' )
axs[1,3].scatter(N_index, RL_DEV[3,1,:], s=5, linewidth=0.3, color = clis[1,:],  marker='x' )
axs[1,3].scatter(N_index, RL_DEV[3,2,:], s=5, linewidth=0.1, color = clis[2,:], marker='^' )
axs[1,3].scatter(N_index, RL_DEV[3,3,:], s=5, linewidth=0.1, color = clis[3,:], marker='s' )
axs[1,3].scatter(N_index, RL_DEV[3,4,:], s=5, linewidth=0.1, color=clis[4,:],  marker='h' ) 
axs[1,3].scatter(N_index, RL_DEV[3,5,:], s=5, linewidth=0.1, color=clis[5,:],marker='o' )
axs[1,3].scatter(N_index, RL_DEV[3,6,:], s=5, linewidth=0.1, color=clis[6,:],  marker='d' )
axs[1,3].scatter(N_index, RL_DEV[3,7,:], s=5, linewidth=0.1, color=clis[7,:], marker='<' )
axs[1,3].scatter(N_index, RL_DEV[3,8,:], s=5, linewidth=0.1, color=clis[8,:], marker='p' )
axs[1,3].scatter(N_index, RL_DEV[3,9,:], s=5, linewidth=0.1, color=clis[9,:],  marker='1' ) 
axs[1,3].set_title('(h)  Im$\{Z_{\mathrm{RV}}\}$')
axs[1,3].set(xlabel='$10^3~N$', ylabel='$10^3~1/\delta^2$')

for i in [0,1]:
    for j in [0,1,2,3]:
        axs[i,j].tick_params(pad=-10)
cmap = mpl.cm.rainbow
norm = mpl.colors.Normalize(vmin=0.1, vmax=1)
cbar=fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=axs[:], pad=0.03,orientation='vertical',ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
cbar.ax.tick_params(width=0.5,length=3)
plt.savefig('Fig6.png',dpi=400,bbox_inches ='tight')
plt.show()

# ave & Delta *1
# Dev/1000 
