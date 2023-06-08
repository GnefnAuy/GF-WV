
import numpy as np
from qutip import *

H_tot = qload('H_tot')
# Calculate the eigenvalues and eigenstates of the Hamiltonian
eigenvalues, eigenstates = H_tot.eigenstates()
gs = eigenstates[0]
E_gs = eigenvalues[0]
qsave(gs, 'gs')



