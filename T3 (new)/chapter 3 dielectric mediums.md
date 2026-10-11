<mark style="background: #ADCCFFA6;">for cheat sheet </mark>


```table-of-contents
```

electric fields penetrating matter (= atoms, molecults wih own electrogamn fields)


# ED of dielectrica themselves 
Main function to describe potential inside matter -> continious, glatt function 

new charge distribution in this case: $$\langle \rho (\vec x) \rangle = \langle \rho_{free} (\vec x) \rangle - \vec \triangledown \cdot \langle \vec P (\vec x ) \rangle$$
=> polarisation density that comes from charge neutral electric dipols$$- \vec \triangledown \cdot \langle \vec P (\vec x ) \rangle$$
 Define I guess the field inside the material : $$\vec \triangledown \cdot \langle \vec D \rangle = \langle \rho_{free} (\vec x) \rangle$$
 because the field itself also needs that extra polarization component $$\langle \vec D \rangle = \epsilon_0 \langle \vec E \rangle + \langle \vec P \rangle$$
 subcase: **linear dielectric medium** -> has the electric suzeptibility $\chi$
 $$\langle P_i (\vec x) \rangle = \epsilon_0 \sum_k \chi_{ik} (\vec x) \langle E_k (\vec x) \rangle$$
 $$\langle \vec P \rangle = \epsilon_0 \chi \langle \vec E \rangle$$
 homogenous dielectrica => $\vec E$ independant of $x$ position 
with different electric permetivvity: 
$$\epsilon = \epsilon_0 (1 + \chi)$$
Poisson equation for dielectrica 
 $$\vec \triangledown^2 \langle \phi \rangle = - \frac{1}{\epsilon} \langle \rho_{free} \rangle$$
 -> everything from [[chapter 2 on cavities (just notes 19(20).08.26)]] also applicable here, just need to multiply with permettivity coefficient 

Transition form on medium to another: 
-> surface charge $$\sigma (\vec x ) = \vec P (\vec x) \cdot \vec n$$
-> $\langle \vec E \rangle, \langle \vec P \rangle$ are both continous 
-> $E_{senkrecht}$ is not continous 
(this is for solving the conductor problems)


# forces and interactions 
dielectrica interacts with external field 

Poisson equation solved for fixed and distant charges" $$\vec \triangledown^2 \phi_{ext} = - \frac{\rho_{ext}}{\epsilon_0}$$
-> assumed that external field is fairly constant on our sensible scales 
## Force 
**force onto the dielectricum** $$F_i = \int d^3 x [\langle \rho_{free} (\vec x) \rangle E_i^{ext} + \sum_k \langle P_k \rangle \partial_k E_i^{ext}]$$
-> same for non linear mediums 
-> still the dielectricum is a bunch of dipols 
-> $$\langle \vec E \rangle = \vec E_{ext} + \langle E_{self} \rangle$$
while $$\langle \vec E_{self} \rangle = - \vec \triangledown \langle \phi_{self} \rangle = - \frac{1}{4 \pi \epsilon_0} \vec \triangledown \int d^3 x' \frac{\langle \rho (\vec x') \rangle}{|\vec x - \vec x'|}$$

With some mysterious calculations: $$F_i = \int d^3 x [\langle \rho_{free} (\vec x ) \rangle + \sum_k \langle P_k (\vec x ) \rangle \partial_k] \langle E_i (\vec x ) \rangle $$

## Energy 
$$E_{tot} = E_{mat} + E_{EM}$$
-> $E_{mat}$ comes only from the matter itself 

with $E_{EM} = E_{EM, self} +E_{ext} + E_{int}$ 
-> $E_{ext}$ comes from the external field $\phi_{ext}$ 
-> $E_{EM, self}$ is the internal EM field (from protons and stuff) 
=><mark style="background: #ADCCFFA6;"> only change can be calcualted </mark>
	assume $\langle \rho_{free} (\vec x ) \rangle =0$ and $\langle \vec P \rangle = \epsilon_0 \chi \langle \vec E \rangle$ 
-> $E_{int}$ describes the interaction of the external field with the dielectrica =><mark style="background: #ADCCFFA6;"> probably the only one that can be calculated </mark>

$$E_{int} = \int d^3 x \space \langle \rho_{free} (\vec x ) \rangle \phi_{ext} (\vec x) - \int d^3 x \langle \vec P (\vec x ) \rangle \cdot \vec E_{ext} (\vec x)$$
-> holds for lineaer and non linear dielectrica 


# Work 
$$\Delta W = \Delta (E_{self} + E_{int}) = \frac{1}{2} \int d^3 x \space \langle \vec D \rangle \cdot \langle \vec E \rangle$$


