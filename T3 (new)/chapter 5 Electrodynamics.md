```table-of-contents
```

now have both electric and magnetic field interacting and being active at the same time
# equations of electrodynamics 
Reminder - [[gauge transformation]] , which lead to gauge invariant E and B fields: $$\vec E = - \vec \triangledown \phi - \frac{\partial}{\partial t } \vec A$$$$\vec B = \vec \triangledown \times \vec A$$
this leads to:  $$\vec \triangledown \times \vec E + \frac{\partial }{\partial t}\vec B =0$$ $$\vec \triangledown \cdot \vec B =0$$
the other [[Maxwell equations]] stay the same 

We can look back to the [[continuity equation]] in this situation: $$\frac{\partial}{\partial t} \rho + \vec \triangledown \cdot \vec J =0$$
=> conservation of charge always holds 

## Duality of E and B 
in case of $\vec J =0$ and $\rho =0$: $$\vec E \to c \vec B$$$$c \vec B \to - \vec E$$

## E and B field under and angle 
because of linearity of Maxwell equations, there are solutions for the case, where the fields have the angle $\alpha \in \mathbb{R}$ between them: 
$$\vec E' = \cos (\alpha) \vec E + \sin (\alpha) c \vec B$$
$$\vec B ' = - \sin (\alpha) \frac{1}{c} \vec E + \cos (\alpha) \vec B$$

## Energy and momentum density 
Reminder: [[Energy density]] and [[Momentum density]] 
adding the relativistic $E = mc^2$ 
from that we get the Energiestrom/[[Poynting vector]] 

looking at the Poynting vector, that goes through a surface $A = \partial V$, we get some sort of a power $$P_{\partial V} = \int_{\partial V} d^2 x \space \hat n \cdot \vec S = \int_V d^3 x \space \vec \triangledown \cdot \vec S$$

change in energy densty: $$\frac{\partial}{\partial t} \mathcal{E} = ... = \epsilon_0 \vec E \cdot (c^2 \vec \triangledown \times \vec B - c^2 \mu_0 \vec J ) + \frac{1}{\mu_0} \vec B \cdot (-\vec \triangledown \times \vec E)$$

the total change of electromagnetic energy in a volume $V$: $$\frac{d}{dt} E_V = \int_V d^3x \space \frac{\partial}{\partial t} \mathcal{E} = - P_{\partial V} + P_{mat}$$
where: 
- $P_{\partial V}$ : over $\partial V$ radiated power 
- $P_{mat}$ : by the matter absorbed power onside of $V$ 
$$P_{mat} = - \int_V d^3 x \space \vec E \cdot \vec J$$
we call it the "Energieaufnahme" by matter by the field $$\frac{\partial \mathcal{E}_{mat}}{\partial t} = \vec J \cdot \vec E$$
### Result 
$$\frac{\partial }{\partial t} \mathcal{E} + \vec \triangledown \cdot \vec S = - \vec J \cdot \vec E \equiv - \frac{\partial \mathcal{E}_{mat} }{\partial t}$$
same with the [[Momentum density]] and [[Cauchy stress tensor]] 

$$\frac{\partial}{\partial t} P_i - \sum^3_{j=1} \partial_j \Theta_{ij} = - f_i \equiv - \frac{\partial p_i^{mat}}{\partial t}$$
where the last part is the [[lorentz force density]] and the stress tensor acts like the directed momentum flux density 

## Maxwell equations for the gauge field 
### ![[Lorenz gauge]] 
The gauge transformation that fullfills this gauge is: 
$$\frac{1}{c^2} \frac{\partial}{\partial t} \phi' - \frac{1}{c^2} \frac{\partial^2}{\partial t^2} \chi + \vec \triangledown \cdot \vec A' + \vec \triangledown^2 \chi \equiv S$$
($S$ is just any equation)
which means, rephrased: $$\square \chi \overset{!} = -\frac{1}{c^2} \frac{\partial^2}{\partial t^2} + \vec \triangledown^2 = \partial_{\mu} \partial^{\mu}$$

