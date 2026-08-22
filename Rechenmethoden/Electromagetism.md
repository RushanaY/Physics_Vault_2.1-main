[[Check list of elements]] 
# Field 
A field is a function, that is dependant on time and position. It takes in a position vector and gives a force vector, therefore describing the force on a particle at a certain position.  This [[force]] comes from the medium and can be transferred with a finite velocity. 
Basically a field is where a particle can feel a force. 

## Energy of the electromagnetic field 
$$U = \frac{\epsilon_0}{2} \int_{\mathbb{R}^3} (\vec E^2 + c^2 \vec B^2) d^3 x$$
In order to shoe the conservation of energy we have to show $\frac{dU}{dt} = 0$ . Using the identity:  $$\triangledown \cdot (u \times v ) = (\triangledown \times u) \cdot v - u \cdot (\triangledown \times v) $$
The way to use it, is to integrate both sides, which removes the nabla operator and allows to split the energy integral into two parts. Which allows us to show how the whole integral goes to zero, because we know that both v and u disappear in the distance. 
Doing the derivation of energy with respect of time, we get terms $E \frac{\partial E}{\partial t}$ and $B \frac{\partial B}{\partial t}$, where we can rewrite the partial derivatives using Maxwell equations. Those consist of a vector and cross product. This is our open door to use the identity


# Riemann Siberstein vector
Instead of writing both E and B fields they can be connected together into the [[Rechenmethoden/Riemann Silberstein vector]].  It is a complex vector that allows to make the Maxwell equations shorter


# Maxwell equation
$$\vec \triangledown E = \frac{1}{\epsilon_0} \rho$$$$\vec \triangledown \times \vec E = - \partial_t \vec B$$$$ \vec \triangledown \vec B =0$$$$ \vec \triangledown \times \vec B = \epsilon_0 \mu_0 \partial_t \vec E + \mu_0 \vec j$$where $\vec j (\vec r, t), \rho (\vec r, t)$ are known and I guess are constant
From the Maxwell equations we can derive the ![[wave equation|wave equation]] 
To derive that we first apply $\triangledown \times$ onto $\triangledown \times \vec E$  ([[Faradays law]]) and use the identity $\triangledown \times (\triangledown \times \vec E) = \triangledown (\triangledown \cdot \vec E) - \triangledown^2 \vec E = - \triangledown^2 \vec E$  to get to the end result. An analogous derivation can be done for the wave equation for the B field. Here we apply the same $\triangledown \times$ onto $\triangledown \times \vec B$ ([[Ampere Maxwell law]] )

# Lorentz force 
$$\vec F = q(\vec E + \vec v \times \vec B) $$
An important problem is the fact, that the Lornetz force can't be invariant under transofrmation of the system. The reason lies in the velocity that is not invariant, which leads both electric and magnetic fields to not be invariant either. This means that the force also can't be invariant, but it is. 
This can be explained with [[special relativity]] and using [[Lorenztrafo]]

# Duality of the E and B field 

It is the idea, that in astatic case, where there are no charges and currents, then the magnetic and electric components of the electrodynamics have analogous elements to each other.  The reason lies in the [[special relativity]] 
Again no charges or current and putting all constants as equal to 1
- only in static case! 
- reason in special relativity using the Lorentz transformation -> trafo fro electric to magnetic field 
- basically both E and B field have the same elements or their analogous 


| E field                                      | B field                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------- |
| electric field ($\vec E$)                    | Planck                                                                    |
| electic displacement field ($\vec D$)        | magnetic flux desity ($\vec B$)                                           |
| [[Faradays law of induction]]                | [[Ampere law]]                                                            |
| Gauss law                                    | Gauss law                                                                 |
| potential                                    | potential                                                                 |
| permetivitty $\epsilon$                      | permeability $\mu$                                                        |
| Farday effect (something about poalrization) | Kerr effect (change in refreactive index after an applied electric field) |
| [[Stark effect]]                             | [[Zeeman effect]]                                                         |
| electrical charge                            | magnetic monopole (*just hypothetical*)                                   |

# Quantasation of the EM field
$$\begin{pmatrix} \vec \triangledown \times &0 
\\ 0 & \vec \triangledown \times
\end{pmatrix}
\begin{pmatrix} \vec E \\ \vec B\end{pmatrix} = \begin{pmatrix}  0 & - \partial_t \\ \partial_t & 0\end{pmatrix} \begin{pmatrix} \vec E \\ \vec B \end{pmatrix}$$
$$\vec \triangledown (\vec E + i \vec B) = i \partial_t (\vec E + i \vec B)$$
In order to rotate the whole system, you multiply with $e^{- i \xi}$ 

## what is $\xi$ and what does the equation do 

# Lorenz force:
- galilei invariance is a problem -> why? 
-> velocity is not invariant under change of system, but force should be
- you can't calculate force with an invariant velocity
- more so, neither is electric or magnetic fields are invariant 
- the solution is the Lorenz trafo under special relativity 

# Field tensor and space and time 
 
$$F_{\mu \nu} =\begin{pmatrix} 0 & E_1 & E_2 & E_3 \\ -E_1 & 0 &-B_3 & B_2 \\ -E_2 & B_3 & 0 & -B_1 \\ -E_3 & -B_2 & B_1 & 0 \end{pmatrix}$$

This tensor describes the E and B field. It is antisymmetrical ($F_{\mu \nu} = - F_{\nu \mu}$) and can be defined as:
$$F_{ij} = 0 \epsilon_{ijk} B_k$$where $F_{\mu \nu} = - F_{\nu \mu}$ and $F_{0i} = E_i$ 

using [[Bianachi identity]] we can show that the Maxwell equations hold

# [[Greens function]] 
In electrostatics that's how we use that:
We take the operator/function $$(Gf)(x) = (G * f)(x) = \int G(x-y)f(y) dy = \int G(x,y)f(y) dy$$
I guess this greens function is an analogous of the Coulomb force. Which is why can show that the force gets weaker with the distance by showing $\triangle G (-, \vec r' )|_{\mathbb{R^3} \space  without \space \vec r'} =0$      where the greens function is defined as $$G(\vec r, \vec r') = - \frac{1}{4 \pi |\vec r - \vec r'|}$$It is the generalised version of the coulomb force of a singe charge. It does have some tendencies that remind me of **mirror charges**. To sum up the LibreText article: The potential for a single point charge is simple, but adding on the superposition principle and looking at a spread of charges we are better of using the Greens function. This function works for unlimited space, but using the condition we bound it to last till the next conductor. For the whole thing we using the theorem $$\int_V (f \triangledown^2 g - g \triangledown^2 f) d^3 r = \int_S *f \triangledown g - g \triangledown f)d^2r$$ which is some form of gauss or stokes law.  So we can either look at a volume filled with charges, or just the charges on the surface of this sphere. 
Another equation is explained by using the **Poisson equation**. That's the one that includes the delta function. 
$\to$ still unsure about this text

# Gauss ray
General form:
$$E(x,y,z,t) = E_0 \frac{\omega_0}{\omega(z)} exp (- \frac{x^2 + y^2}{\omega^2(z)}) cos(kz + \frac{k(x^2 + y^2)}{2 R(z)}-\omega t + \psi(z))$$
Helmholtz equation :$(\triangledown^2  +k^2) E =0$ 
useful rewritings: $\omega^2(z) = \omega_0^2 (1 + (\frac{z}{z_R})^2)$, $z_R = \frac{\pi \omega_0^2}{\lambda}$, $\psi(z) = arctan(\frac{z}{z_R})$, $R(z) = z (1 + (\frac{z_R}{z})^2)$ 
superposition principle is used 
If the [[Helmholtz equation]] is full filled, then we  have an applied case for waves. 

# surface integrals in electromagnetism 
The first step is to determine all the surfaces we will have to account for. They are being expressed in maps (Karte), which will create the boundaries of the integrals. It is smart to choose a good coordinate system to have less complicated calculations. 
The whole surface is the sum of all the smaller surfaces, which are defined by the maps from before. Here it is to be noted, that when integrating over this surface we are adding up small areas dS, that are more precisely written as $\hat n dS$. Where the n denotes the normal vector to the surface. 
The important aspect of the surface integral is to get the $dS$ correctly. To remember is, that it is a small surface area, which we want to express in the according coordinates. Generally, in Cartesian coordinates it would be $dS = |dx \times dy| dx dy$ . Instead of $x$ and $y$ we put our according coordinates.
As the next step the normal vector $\hat n$ is determined. It can be done either by a quick sketch or by using a formula of the general form :
$$\hat n = \triangledown F(x,y,z) = \frac{\partial \vec r}{\partial x} \times \frac{\partial \vec r}{\partial y}$$
Putting it together into $$\int_S F\cdot \hat n dS $$
In the case where we have a specific field that is passing through the surface we can just take the part that is actually participating in the flux. Instead of $\vec E$ we can specifically take $E_0 cos \theta$ if needed. 

 