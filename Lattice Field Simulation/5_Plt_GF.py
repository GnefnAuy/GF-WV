
import matplotlib.pyplot as plt
import numpy as np
from qutip import *
import seaborn as sns  
sns.set(style="darkgrid")
sns.set_context("poster", font_scale = 3/4 , rc={"grid.linewidth": 9/4})
T = np.load("T.npy")
t_ = np.load("t_.npy")
A = qload('GFOP')
Omg = qload('gs')
GF = np.array([ (Omg.dag() * A[i] * Omg)[0,0] for i in range(T)], dtype=complex)


fig1,ax1=plt.subplots( 1, 1, figsize=(4, 2.5), sharey=False, sharex=False)
plt.plot(t_, GF.real ,color='r',linewidth=2,linestyle='dotted', marker='.',label='Re$G$ (true value)')
plt.plot(t_, GF.imag ,color='b',linewidth=2,linestyle='dotted', marker='.', label='Im$G$ (true value)')
plt.plot(t_, abs(GF) ,color='g',linewidth=2,linestyle='dotted', marker='.', label='$|G|$ (true value)')
plt.legend(loc='best', ncol=2, prop = {'size':7})
plt.xlabel('$t$')
plt.ylabel('$G(t,0)$')
plt.savefig('GF_true value.png',dpi=400,bbox_inches ='tight')
plt.show() 
