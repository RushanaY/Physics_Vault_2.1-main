# 1.1. Theory of E and B fields 
-> $\vec E (t,\vec x) \text{ and } \vec B (t, \vec x)$

1. electrodynamics in vacuum
![[Pasted image 20260606195403.jpg]]



2. electro-/magnetostatics 
![[Pasted image 20260606195417.jpg]]
with 
	a) [[point charge]] with [[charge density rho(x)]] 
	b) [[line current]] with [[current density J(x) (ED)]]   



3. electrodynamics 
![[Pasted image 20260606201159.jpg]]
-> how electrodynamics changes the optical properties of a material 
![[Pasted image 20260606201159.jpg]]


4. coupling onto dynamic matter $\vec X(t)$ 
![[Pasted image 20260606201253.jpg]]





# 1.2. Theoretical Formalism 
-> from observations the maxwell equations were derived 
Going from the easier cases of [[Electrostatics]] and [[Magnetostatics]] 

=> both together form the Maxwell equations![[Maxwell equations]] 

## [[Lorentz force]] 
-> we need this additional force to describe ED, because [[Maxwell equations]] are not enough 

![[Lorentz force]]


## 1.2.2. Classical field theory 
Apply the [[principle of least actions]] 

**Electrodynamics is a classical field theory, that describes a vector field**

Using the principle of least action we also have the idea of [[Lagrange density]] 

For [[T3 Electrodynamics|electrodynamics]] the [[Euler Lagrange Equation]]s are $$\frac{\delta \mathcal{L}}{\delta \phi} - \partial_{\mu} (\frac{\delta \mathcal{L}}{\delta(\partial_{\mu} \phi)}) =0$$ 

### 1.2.3. Modern formulation of electrodynamics 
Question is, what is the [[Lagrange density]] ? and how much? 

Important symmetries 
- Lorentz invariance of special relativity 
- local Gauge symmetry

If no flux or charge $$\mathcal{L}_{EM} = \frac{1}{2 \mu_0} (\frac{1}{c^2} | \vec E |^2 - | \vec B |^2)$$
-> coupling on charges and flux need more parameters than we have right now 
	=> we need more parameters to describe the field better: 
#### [[scalar potential]] $\phi$ 
#### [[vector potential]] $\vec A$ 


Then the fields are $$\vec E = - \vec \triangledown \phi - \frac{\partial A}{\partial t}$$
$$\vec B = \vec \triangledown \times \vec A$$ 

## ![[4 vector field]] 

From this the [[Lagrange density]] can be derived 
![[Lagrange density]]


Note on the writing style:
- Fields can be expressed as $$F_{\mu \nu} = \partial_{\mu} A_{\nu} - \partial_{\nu} A_{\nu} $$
- with the field tensor $$E_i = cF_{i0}, \quad i =1,2,3$$$$B_i = F_{jk}, \quad (i,j,k) \text{cyclical}$$
More parameters! that are not derived from the Maxwell equations and are just as fundemental
## [[Energy density]] 
![[Energy density]]

## [[Momentum density]]
![[Momentum density]]

## [[Cauchy stress tensor]] 
![[Cauchy stress tensor]]

## [[Poynting vector]] 
![[Poynting vector]]


## 1.2.4. Derivation of the [[lorentz force]]
