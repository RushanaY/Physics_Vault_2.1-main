```table-of-contents
```
# Cavity:
- bound volume 
- **conducting surface**
## cavity problems 

# Conductor
- in E statics -> electrons can freely move and therefore "compensate" any field (on the inside of the enclosed volume!) = electrons have reached equillibrium$$\vec E = - \vec \triangledown \phi =0 \qquad \Rightarrow \qquad \phi = const \qquad \Rightarrow \qquad \rho = 0 \qquad \Rightarrow \qquad \vec \triangledown^2 \phi =0$$
	- ($\phi = const => \rho =0$ from Poisson equation)
	- the last part means that all charge is on the surface $$\rho (\vec x) = \sigma (x) \delta (s)$$
		- $s$ : distance from surface along $\hat n$ 
		- $\sigma(\vec x)$ : Surface charge density

## conductor problems 
-> solve the field equation for the field along the surface 

### ways to solve conductor problems 
for a volume $V$ that is bounded by a surface $S = \partial V$. there is a continuous function $\rho(\vec x)$ on $V$ and the Poisson Equation $\triangledown^2 \phi = - \rho/\epsilon_0$ 
-> [[Dirichlet condition]] $$\phi|_S = \psi$$
	- if potential $\phi$ is given
-> [[Neumann condition]] $$\int_S d^2 x \space \chi (\vec x) = - \frac{1}{\epsilon_0} \int_V \rho (\vec x) d^3 x $$
	- if surface charge or electric filed are given

#### Hohlraumresonator 
Take $\phi$ to be constant at the boundary $S$ 
- $\rho =0$ on $V$ 
	- we knew from conditions from above we know that there is a unique solution of $\triangledown^2 \phi =0$ (no charges, no potential )
			=> solution is $\phi = constant$ 
					=> $\vec E =0$ on the inside (because the constant potential meant equilibrium and therefore no field)
- $\rho \neq 0$ on $V$
	- **gauge freedom** allows to shift potential $\phi$ so that it's zero at the boundary
	- solve $\triangledown^2 \phi = - \rho/\epsilon_0$ with the Dirichlet condition $\phi|_S =0$ (that means no charges lead to no potential)
	- It is solved by [[Dirichlet Green's function]] (potential of a unit point charge at $\vec x '$ inside the cavity) $$\triangledown^2 G_D (\vec x, \vec x') = - \frac{1}{\epsilon_0} \delta(\vec x - \vec x')$$
		- when proving validity (example of a sphere with radius R), show
			- $G_D (\vec x, \vec x')$ holds for $|x|<R$ 
			- $G_D (\vec x, \vec x') =0$ at $|x| =R$ 
		
#### special case: **sphere** 
- function is $$G_D (\vec x , \vec x') = \frac{1}{4 \pi \epsilon_0} \frac{1}{|\vec x - \vec x'|} + \frac{1}{4 \pi \epsilon_0} \frac{\alpha }{|\vec x - \vec x''|}$$
	- first part is the [[Greens function]] for unbounded space 
	- second part is the image charge outside of the cavity -> corrects the boundary condition 
		- $\alpha = - \frac{R}{|\vec x'|}$
		- $\vec x'' = \vec x' (\frac{R}{|\vec x'|})^2$ 
		- In general case it is $F_D (\vec x, \vec x')$ 
			- -> satisfies Laplace equation $$\triangledown_x^2 F_D (\vec x, \vec x') =0$$
- any other cases : Eigenfunction expansion (like Multipol expansion I think) 
#### general Dirichlet Problem 
Conditions
$$\vec \triangledown^2 \phi = - \frac{\rho(x)}{\epsilon_0} \qquad \forall x \in V$$$$\phi|_{x \in \partial V} = \psi (\vec x)$$
($\partial V$ is not a conductor)
Solution: $$\phi(\vec x) = \int_V d^3 x' G_D (\vec x, \vec x') \rho(\vec x') - \epsilon_0 \int_{\partial V} d^2 x' \psi( \vec x') \hat n' \cdot \vec \triangledown_{x'} G_D (\vec x, \vec x')$$

#### general Neumann Problem
Neumann Greens function: $$\vec \triangledown^2 G_N (\vec x, \vec x') = - \frac{1}{\epsilon_0} \delta (\vec x - \vec x')$$
with boundary condition $$(\hat n \cdot \vec \triangledown_x) G_N (\vec x, \vec x') |_{x \in \partial V} = - \frac{1}{\epsilon_0 |\partial V|} = const$$
another requirement $$\int_{\partial V} d^2 x' G_N (\vec x, \vec x') =0$$
Solution: $$\phi(\vec x) = \int d^3 x' G_N (\vec x, \vec x') \rho(\vec x') + \epsilon_0 \int_{\partial V} d^2 x' \chi (\vec x ') G_N (\vec x, \vec x')$$

## tangentially related notes 
- derivatives of a delta function correspond to a dipole layer of charge (so it is important that charge density on the surface of a conductor is not derivative)
- the field not having a derivative in the Poisson equation implies, that **field has to be continuous along the whole surface** 
- using the **gauge freedom** we can shift the electrical potential $\phi$ 
- [[Greens theorem]] $$\int_{\partial V} d^2 x \hat n \cdot (\phi_1 \vec \triangledown \phi_2 - \phi_2 \vec \triangledown \phi_1) = - \frac{1}{\epsilon_0} \int_V d^3 x (\phi_1 S_2 - \phi_2 S_1)$$


# related questions from homework sheets 
## [[Problem set 3]] 
