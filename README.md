# Weak-Valued Correlation Functions

Source codes for our latest work on Weak-Valued Correlation Functions: https://arxiv.org/abs/2306.04398.

![Schematic diagram of (a) correlation function with the GellMann and Low Theorem, (b) weak-valued
correlation function.](Fig0.png "Fig0.png")
By employing TSVF to accelerate the adiabatic evolution contained in the Gell-Mann and Low theorem, we establish an equivalent theory where correlation function is interpreted as weak values.

Our proposal in quantum mechanics is exemplified by the perturbed quantum harmonic oscillator (PQHO). 
[Fig1.pdf](https://github.com/GnefnAuy/GF-WV/files/12157573/Fig1.pdf)
The simulations presented in are idealized, assuming perfect estimations of the expectation values $\langle\hat{\sigma_i}\rangle_f$, i.e.,  requiring infinite copies of the final state. The relevant source codes are included in the file named <QM-Ideal Simulation_g>.
[Fig2.pdf](https://github.com/GnefnAuy/GF-WV/files/12157585/Fig2.pdf)
In practical implementations, the accuracy of our readout depends on both the coupling strength and the number of available copies. The relevant source codes are included in the file named <QM-Practical Simulation_gNM>. The detailed treatment of trade-off between $g$ and $N$ is given in <data_figure_of_merit.py>, where the final result could be summarized as follows:
[S3.pdf](https://github.com/GnefnAuy/GF-WV/files/12157643/S3.pdf)

To extend our scheme to quantum field theory, we carry out lattice field simulation of $\phi^4$ scalar field.
[S4.pdf](https://github.com/GnefnAuy/GF-WV/files/12157633/S4.pdf)

Moreover, in order to explore the connection between weak measurements in quantum field theory (QFT) and quantum mechanics (QM), we consider the one-lattice limit where the behavior of the $\phi^4$ field theory resembles that of the PQHO:
[S5.pdf](https://github.com/GnefnAuy/GF-WV/files/12157670/S5.pdf)



