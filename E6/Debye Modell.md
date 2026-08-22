### Assumption 
- there is a large number of oscillation states 
- describes only ==acoustic phonons== 

Sum of the internal energy $$U = \int _0^{\infty} \hbar \omega \cdot D (\omega) \cdot \langle n \rangle d \omega = 9 N k_B T (\frac{T}{\theta_D})^3 \int_0^{x_D} \frac{x^3}{e^x -1} d x$$
	the right side has subsitutioned $x = \frac{\hbar \omega}{k_B \space T}$, $\theta_D = \frac{\hbar \omega_D}{k_B}$ 

 where considering the 3 [[acoustic branch]]es and taking the [[density of states (Zustandsdichte)]] $$D_{acoust} (\omega) = 3 \cdot \frac{V \omega^2}{2 \pi^2 \nu^3_{sound}}$$
	The integral diverges , up to the [[Debye frequency]] $\omega_D$  


We get $3N$ oscillation states for $N$ atoms: $$3N = \int_0^{\omega_D} D (\omega) d \omega$$

### for low temperatures 
In order to calculate the integral for internal energy from above, we assume low temperatures (this allows to take $\infty$ instead of $x_D$ ), because less modes are exited 
Using the identity $\int_0^{\infty} \frac{x^3}{e^x -1} dx = \frac{\pi^4}{15}$ we calculate the internal energy as :$$U = \frac{3}{5} \pi^4 N k_B T (\frac{T}{\theta_D})^3$$
and from that the specific heat capacity being: $$C_V = \frac{\partial}{\partial T}{U} = \frac{12}{5} \pi^4 N k_B T (\frac{T}{\theta_D})^3$$
-> observation: for low temperatures we have have the same relation of $C_V \sim T^3$ as in the observed one, that can be seen in experiments 

### for high temperatures 
we assume here $x = \frac{\hbar \omega}{k_B T} << 1$ , that put into the integral gives the value $\int_0^{x_D} x^2 dx= \frac{1}{3} x_D^3$ => $C_V = 3 N k_B$ (again corresponds perfectly with the [[Duolong Petit law]])


### all in all evaluation 
- $T < \theta_D$ : quanten mechanical area => modes freeze up
- $T> \theta_D$ : classical areal => all modes exited 