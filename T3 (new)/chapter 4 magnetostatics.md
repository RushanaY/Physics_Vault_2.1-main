```table-of-contents
```
static magnetic field 
-> $\rho =0, \space \phi =0, \space \partial_t \vec J (t, \vec x)=0,\space  \partial_t \chi =0$ 

in the end: $$\vec \triangledown (\vec \triangledown \cdot \vec A) - \vec \triangledown^2 \vec A = \mu_0 \vec J$$

poisson equation $$\vec \triangledown^2 \chi = - \vec \triangledown \cdot \vec A $$
Coulomb gauge $$\vec \triangledown \cdot \vec A =0$$

# carteisan multipol expansion 
$$\int d^3 x \space \space \vec J (\vec x) = 0$$


$$\vec A = \frac{\mu_0}{4 \pi} \frac{\vec \mu \times \hat x}{|\vec x |^2} \space + \space ...$$

magnetic moment $$\vec \mu = \frac{1}{2} \int d^3 x' \space \vec x ' \times \vec J (\vec x ')$$

# spherical multipol expansion 
main think are spherical functions! 
charge distribution $\rho_{lm}$ are used to express the $\phi_{lm} (r, \theta, \psi)$ 

vector field: 
$$\vec \rho = \sum_{l,m} [\rho_{lm} (r) Y_{lm} (\theta, \psi) \hat r + g_{lm} (r) r \vec \triangledown Y_{lm} (\theta, \psi) + h_{lm} (r) \vec r \times \vec \triangledown Y_{lm} (\theta, \psi)]$$

so the solution for magnetostatic vector potential :
$$\vec A (\vec x) = - \sum_{lm} \frac{\mu_0}{l (2l + 1) } \frac{m_{lm}}{r^{l+1}} \space \vec  r \times \vec \triangledown Y_{lm}$$

magnetic scalar potential $$\phi_M = \sum_{lm} \frac{\mu_0}{2l +1} \frac{m_{lm}}{r^{l+1}} Y_{lm} (\theta, \psi)$$
# interaction energy 
going from the general equation for energy density and the assumption of $E=0$ and integrating for the total energy: $$E_{tot} = \frac{1}{2} \int d^3 x \space \vec A \cdot \vec J$$
for a magnetic dipol: $$\mathcal{E}^{int} = \vec \mu \cdot \vec B^{ext}$$
Lorentz force in this case is of course ($B =0$ ) $$\vec f = \vec J \times \vec B$$
total force $$\vec F = (\vec \mu \cdot \vec \triangledown)\vec B^{ext}|_{\vec x =0} \space x \space ...$$similar would electrostatic case look like: $$\vec F = (\vec p \cdot \vec \triangledown) \vec E^{ext}|_{\vec x =0} \space + \space ...$$

# Work in the field and self energy 
We take the model, where we have two dipols $p_1$ and $p_2$ . Dipol $p_1$ is stationary and acts as the external magnetic field for $p_2$. Meanwhile $p_2$ is moving up and down. 
We look at the work, that get's done and the energy exchanged
## electric dipol
$$\delta W = - \vec F \cdot \delta \vec x = - \vec p_2 \cdot \delta \vec E_1$$
## magnetic dipol
$$\delta W = - \vec  F \cdot \delta \vec x = - \vec \mu_2 \cdot \delta \vec B$$
but at the same time the **interaction energy** increases $$\delta \mathcal{E}^{int} = + \vec \mu_2 \cdot \delta \vec B_1 >0$$
electromagnetic field gets transmitted with $$\frac{d \mathcal{E}^M}{dt} = \int d^3 x \space \vec E \cdot \vec J$$
in our case with two dipols $$\frac{d \mathcal{E}^M_2}{dt} = \int d^3 x \space (\vec E_1 + \vec E_2) \cdot \vec J_2$$
in there there is the part, which describes the **change in internal energy** $$\frac{d}{dt} \mathcal{E}^{self}_2 = \int d^3 x \space \vec E_2 \cdot \vec J_2$$
the second part is the energy from the **interaction of flux J with the fixed field E_1** $$\delta \mathcal{E}^{field}_2 = \int d^3 x \space \vec E_1 \cdot \vec J_2 =0$$
main point: $$\text{external magnetical field DOES NOT produce WORK}$$

so in our case (quasi statics = changes very slowly) there is no electromagnetic radiation, because the dipol cannot exchange energy with the external magnetic field.  
Therefore the internal Ruheenergie has to change, the self energy. $$\delta \mathcal{E}^{self}_1 = - \delta \mathcal{E}^{int}$$

the change in Ruheenergie is proof for relativity theory 

an example is the [[Zeeman effect]]:$$\hat H = - \vec \mu \cdot \vec B^{ext}$$
the coupling of the spin of the electron with a dipol $\vec \mu_S$ $$\hat H = - \vec \mu_S \cdot \vec B^{ext}$$ 
# magnetic materials 
these materials have 'random' free fluxes flowing through the material, so that in total we have the continous flux being: $$\langle \vec J \rangle = \langle \vec J_f \rangle + \vec \triangledown \times \langle \vec M \rangle$$
where $\langle \vec M \rangle$ is the Magnetisierung ($\vec \triangledown \times \langle \vec M \rangle$ is the Magnitisierungsstrimdichte)

in this part we want to get the field, that comes only from these natural free fluxes: $$\langle \vec H \rangle = \frac{1}{\mu_0} \langle \vec B \rangle - \langle \vec M \rangle$$
where we get $$\vec \triangledown \times \langle \vec H \rangle = \langle \vec J_f \rangle$$
### at the boundary
if there are no $\delta$ function things of $\langle \vec M \rangle, \langle \vec J_f \rangle$, then there are no surface charge flux $\langle \vec J_f \rangle$, which leads to the boundary conditions: 
- $\langle \vec A \rangle$ is continuous 
- $\langle B_{\perp} \rangle = \hat n \cdot \langle \vec B \rangle$ is continuous
- $\langle \vec H_{\parallel} \rangle$ is continuous

### linear magnetic materials 
$$\langle \vec M \rangle = \chi_m \langle \vec H \rangle$$
with $\chi_m$ is the (linear) magnetic suszepbility 
defining the magnetic field: $$\langle \vec B \rangle = \mu \langle \vec H \rangle$$
with the magnetic permeability: $$\mu = \mu_0 (1 + \chi_m)$$
### diamagnetic 
$$\chi_m <0$$
### paramagnetic 
$$\chi_m > 0$$
### permanent magnet 
$$\langle \vec M \rangle \neq 0$$
where the direction of $\langle \vec M \rangle$ is the Hystersis 