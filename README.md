# Weak-Valued Correlation Function

Source codes for our latest work on Weak-Valued Correlation Function: [PhysRevA.109.052210](https://doi.org/10.48550/arXiv.2306.04398). We proposed a new interpretation for the correlation function as weak values of a specific type of weak measurement and the experimental scheme for retrieving it.

Our proposal in quantum mechanics is exemplified by the perturbed quantum harmonic oscillator (PQHO). 
![QM scheme: Idealized Simulation](https://github.com/GnefnAuy/GF-WV/blob/main/Relevant%20Figures/Fig1.png)

The simulations presented in are idealized, assuming perfect estimations of the expectation values $\langle\hat{\sigma_i}\rangle_f$, i.e.,  requiring infinite copies of the final state. The relevant source codes are included in the file named <QM-Ideal Simulation_g>.
![QM scheme: Practical Simulation](https://github.com/GnefnAuy/GF-WV/blob/main/Relevant%20Figures/Fig2.png)

In practical implementations, the accuracy of our readout depends on both the coupling strength and the number of available copies. The relevant source codes are included in the file named <QM-Practical Simulation_gNM>. The detailed treatment of trade-off between $g$ and $N$ is given in <data_figure_of_merit.py>, where the final result could be summarized as follows:
![Trade-off details](https://github.com/GnefnAuy/GF-WV/blob/main/Relevant%20Figures/FigS3.png)

To extend our scheme to quantum field theory, we carry out lattice field simulation of $\phi^4$ scalar field.
![QFT scheme: Lattice Simulation](https://github.com/GnefnAuy/GF-WV/blob/main/Relevant%20Figures/Fig4.png)

Moreover, in order to explore the connection between weak measurements in quantum field theory (QFT) and quantum mechanics (QM), we consider the one-lattice limit where the behavior of the $\phi^4$ field theory resembles that of the PQHO:
![Connection between QM and QFT](https://github.com/GnefnAuy/GF-WV/blob/main/Relevant%20Figures/Fig7.png)


