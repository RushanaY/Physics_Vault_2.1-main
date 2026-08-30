*here are just comments and summarized the main points*
# Problem 1

# Problem 2 

# Problem 3
## calculating electrostatic potential  
-> using [[Dirichlet Green's function]] 
$$\phi(\vec r)|_{z >= 0} = \int_{z' >=0} G_D (\vec r, \vec r') \space \rho ({\vec r}) \space d^3 r'$$

where we have the Dirichlet Greens function: $$G_D = \frac{1}{4 \pi \epsilon_0} (\frac{1}{|| \vec r - \vec r'||} - \frac{1}{|| \vec r - \vec r^*||})$$
	with $\vec r^* = (x', y', -z')$ being the mirror charge location 
we have the charge density of the rod:
$$\rho = \lambda \delta (y') \delta (z' - d) \Theta (\frac{L}{2} - |x'|)$$
	with linear charge density $$\lambda = \frac{Q}{L}$$
good identity to know from the [[hyberbolic substitution]]: $$\frac{du}{\sqrt{u^2 + a^2}} = arcsinh(\frac{u}{a})$$
## calculate the force on the rod 
$$F_z = \int_{-L/2}^{L/2} \lambda E_z^{plane} dx$$
only the z components counts
you can imagine that our planes is seen by us as a mirror charge. in a) that helped calculating the plane. now we have to consider the fact, that the charged rod induces charges in the conducting plane and this makes a force back at the rod. 

## consider limit, where rod is very far away from the plane 
use the expansion from the [[useful expansions]]: $$\sqrt{1 + x} = \sum^{\infty}_{k=0} \frac{f^{(k)}(a)}{k!} (x - a)^k$$


