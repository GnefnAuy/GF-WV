
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns  
from pandas import DataFrame
sns.set(style="darkgrid")

#Import
TV=np.load("TV.npy")
WV=np.load("WV.npy")
MD=np.load("MD.npy")
G_index = np.load("G_index.npy")
N_index=np.load("N_index.npy")
M=np.load("M.npy")
DN=len(N_index)
DG=len(G_index)
#Radial Vector
RV = (MD[:,0,:]-TV)
RRV = RV/abs(TV)
#Plot
a = RRV.real
b = RRV.imag

c = np.column_stack((a[0,:],b[0,:]))
d = np.ones(M)*G_index[0]
data = np.insert(c, 2, d, axis=1 )

for j in range(DG):
    c = np.column_stack((a[j,:],b[j,:]))
    d = np.ones(M)*G_index[j]
    data1 = np.insert(c, 2, d, axis=1 )
    data = np.append(data, data1, axis=0)
Trafdata = DataFrame(data, columns=['Re','Im','g_merit'])


pal2 = sns.color_palette("rainbow", as_cmap=True)
sns.set_context("poster", font_scale = 0.83 , rc={"grid.linewidth": 3})
g = sns.JointGrid(x='Re', y='Im', data= Trafdata, 
              hue='g_merit',
              palette=pal2, marginal_ticks= False,
              xlim=(-5, 5), ylim=(-5, 5)
)
g.plot_joint(sns.kdeplot, shade = True, legend= False)
g.plot_marginals(sns.kdeplot, shade = True)
plt.savefig('seaborm.png',dpi=400,bbox_inches ='tight')
plt.show()
