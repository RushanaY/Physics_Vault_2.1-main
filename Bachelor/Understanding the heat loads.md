```table-of-contents
```
General approach 
$$\sum_i dQ_i=0$$
$$\Rightarrow \qquad T''(x) + a T(x) + b =0$$
all heat loads get added together and then "umgeformt nach T"


It is important what the temperature is of -> the second order derivative is of the wire temperature , so differential equation will be too
# Conduction along the wire 
looks alright $$Q = - k \frac{d^2T}{dx^2}\cdot \pi \frac{D^2}{4}dx$$
	only questionable how we get from $- k \frac{dT}{dx}|_{x = x_0 + dx}$ to $-k \frac{dT}{dx}|_{x = x_0} + k \frac{d^2 T}{dx^2} dx$ 
it is the definition of a derivative, right? 
but why is + still valid, and no **chain rule?**

*later, on paper: calculate the option of extra temperature dependence of conductivity of tungsten*
*is there a better equation to describe this phenomena?*
# Probe current 
Important: $I_{probe} = 1mA$ 
-> heats wire up 

$$Q = I^2_{probe}  (\frac{\rho_R}{\pi (\frac{D}{2})2}) dx $$


# Beam Gas
*does the collision between the hydrogen molecules and the wire heat it up at all?*
cheack out the sticking coefficients fro papaer (when doing the imporved version)

Kinetic energy of molecular gas $$Q = \overset{\cdot} N C \triangle T$$
	 C  : heat capacity of molecular hydrogen
	 $\overset{\cdot} N$ : rate of particles 

Result: 
$$Q = (1 - \alpha) \phi_{H_2} d \space dx \frac{5k_B}{2} (T_w - T_{H_2}) + 2 \alpha \phi_{H_2} d \space dx \frac{3 k_B}{2}( T_w - T_{H_2})$$


# Recombination of atomic hydrogen
$$Q = \eta_{rec} \frac{E_{rec}}{2} \phi_H d \space dx = \eta_{rec} \frac{E_{rec}}{2} 2 \alpha \phi_{H_2} d \space dx$$ 


humble approximation $$\eta_{rec} = 0.1$$ 
# Background gas cooling 
$$Q = \beta_{H_2} \pi d \cdot dx \frac{P_{bkg}}{4 k_B T_{chamber}} \sqrt{\frac{8 k_B T_{chamber}}{\pi m_{H_2}}} \frac{5k_B}{2} (T_w - T_{chamber})$$

# Radiative cooling 
from cold nozzle (shoulr really be considerd, as the nozzle in main set up is even colder. so it is good to make it varibale)
she assumes it to be a [[gray body]] 

## Nozzle 
$$Q = - \pi d \space dx \sigma \epsilon_W \epsilon_{Cu} T_{nozzle}^4$$
## Wire 
$$Q = \pi d dx \sigma \epsilon_W T_w^4$$
if I actually want to insert it into the whole heat load equation then i should make it negative? as it is actually cooling? 

## Chamber 
$$Q = - \pi d dx \sigma \epsilon_W T_{chamber}^4$$



# Random notes from the first overview 
![[thermal equilibrium]]

![[Fourier law]] 

## effect of dirt onto the wire resistance 
from Mattesian law we now $$\rho_e (T) \approx \rho_{res} + \rho_{ph} (T)$$
#   Upgrade ideas 
-> make coeffcients dependant on $x$ because the flux density is position dependant 
	=> the flux of hydrogen onto the wire is more in the shape of a cosine, instead of the assumed homogenic version 
-> make the material conductivity temperature dependant, as it might change with big heat jumps (maybe not as relevant for the 15$\mu m$ , but may become a bigger problem for $5 \mu m$)



# In total:
## General DEQ
$$T'' = A \space T(x) + B\space T(x)^4 + C$$
## All heat loads explicitly

$$\sum_i Q_i = Q_{conduction} + Q_{current} + + Q_{beam \space gas} + Q_{recomb} + Q_{bkg \space gas} + Q_{radiative}=0$$
$$\kappa T'' \cdot A_{cs} + I^2_{probe} (\frac{\rho_0 (1 +\alpha_R (T(x) - T_{ref})}{A_{cs}}) + (1 -\alpha) \phi_{H2} d \frac{5 k_B}{2} (T(x) - T_{H2} ) + 2 \alpha \phi_{H2} d \frac{3 k_B}{2} (T(x) - T_{H2})+ \eta_{recomb}E_{rec} 2 \alpha \phi_{H_2} d + (- \beta_{H2} \pi d C_{H2} \phi(P_{bkg} , T_{chamber}) (T(x) - T_{chamber}))+ \pi d \sigma \epsilon_W \epsilon_{Cu} T^4_{nozzle} - \pi 
$$