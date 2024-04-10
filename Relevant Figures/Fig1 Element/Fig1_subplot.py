import math
import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
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
sns.set_context("poster", font_scale = 0.4 , rc={"grid.linewidth": 2})
#PREVIOUS FONTSIZE=0.34
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

clis = plt.cm.rainbow_r(np.linspace(0,1,10))

#Plt real
fig,axs=plt.subplots( 2, 1, figsize=(3.386, 4.8), sharey=False, sharex=False)#,gridspec_kw={'height_ratios': [1, 1, 0.12]})
fig.tight_layout(pad=2.5)

axs[0].plot(T_index, A[9,:],   linewidth=1.5,linestyle='--',   color=clis[9,:]) 
axs[0].plot(T_index, A[8,:],   linewidth=1.5,linestyle='--',   color=clis[8,:])
axs[0].plot(T_index, A[7,:],   linewidth=1.5,linestyle='--',   color=clis[7,:])
axs[0].plot(T_index, A[6,:],   linewidth=1.5,linestyle='--',   color=clis[6,:])
axs[0].plot(T_index, A[5,:],   linewidth=1.5,linestyle='--',   color=clis[5,:])
axs[0].plot(T_index, A[4,:],   linewidth=1.5,linestyle='--',   color=clis[4,:]) 
axs[0].plot(T_index, A[3,:],   linewidth=1.5,linestyle='--',   color=clis[3,:])
axs[0].plot(T_index, A[2,:],   linewidth=1.5,linestyle='--',   color=clis[2,:])
axs[0].plot(T_index, A[1,:],   linewidth=1.5,linestyle='--',   color=clis[1,:])
axs[0].plot(T_index, A[0,:],   linewidth=1.5,linestyle='--',   color=clis[0,:])
axs[0].plot(T_index, a ,color='#4a488e',linewidth=2,linestyle='-',label='true value')
#axs[0].plot([], [], color='grey', label=r'g',   linewidth=1.5,linestyle='--')
#axs[0].legend(loc='lower right', ncol=2, prop = {'size':11})#LAST FONT SIZE=7
axs[0].set(xlabel='$t$', ylabel='Re$G_w$',ylim=(-0.6,0.65))
#axs[0].set_title('a)', loc='left')
axs[0].tick_params(pad=-3)
axs[0].text(-10.46, 0.55, '(a)')


axs[1].plot(T_index, B[9,:],   linewidth=1.5,linestyle='--',   color=clis[9,:]) 
axs[1].plot(T_index, B[8,:],   linewidth=1.5,linestyle='--',   color=clis[8,:])
axs[1].plot(T_index, B[7,:],   linewidth=1.5,linestyle='--',   color=clis[7,:])
axs[1].plot(T_index, B[6,:],   linewidth=1.5,linestyle='--',   color=clis[6,:])
axs[1].plot(T_index, B[5,:],   linewidth=1.5,linestyle='--',   color=clis[5,:])
axs[1].plot(T_index, B[4,:],   linewidth=1.5,linestyle='--',   color=clis[4,:]) 
axs[1].plot(T_index, B[3,:],   linewidth=1.5,linestyle='--',   color=clis[3,:])
axs[1].plot(T_index, B[2,:],   linewidth=1.5,linestyle='--',   color=clis[2,:])
axs[1].plot(T_index, B[1,:],   linewidth=1.5,linestyle='--',   color=clis[1,:])
axs[1].plot(T_index, B[0,:],   linewidth=1.5,linestyle='--',   color=clis[0,:])
axs[1].plot(T_index, b ,color='#4a488e',  linewidth=2,linestyle='-',label='true value')
#axs[1].plot([], [], color='grey', label=r'$g$',   linewidth=1.5,linestyle='--')
#axs[1].set_title('b)', loc='left')
axs[1].legend(loc='best', ncol=1, prop = {'size':10},bbox_to_anchor=(1.1, 2.6))
axs[1].text(-10.46, 0.55,  '(b)')
axs[1].set(xlabel='$t$', ylabel='Im$G_w$',ylim=(-0.55,0.6))
axs[1].tick_params(pad=-3)
#plt.text(0.35, 0.5, '(a)')
cmap = mpl.cm.rainbow
norm = mpl.colors.Normalize(vmin=0.1, vmax=1)
cbar=fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=axs[:], pad=0.13,orientation='horizontal', norm = colors.Normalize(vmin=0.1, vmax=1,clip=False),ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
#cbar=mpl.colorbar.Colorbar(axs[2], cmap='rainbow', norm = colors.Normalize(vmin=0.1, vmax=1,clip=False),orientation='horizontal',location=None,ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
cbar.ax.tick_params(width=1,length=4)
#cbar.outline.set_linewidth(1)
axs[1].text(-5.5, -1.16, '$g$')#,fontfamily=['Times'])
#plt.subplots_adjust(hspace=0.5,wspace=0.1)

plt.savefig('Fig1.pdf',dpi=400,bbox_inches ='tight')
plt.show() 





    