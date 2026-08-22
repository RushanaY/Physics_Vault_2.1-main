- main idea: 
	- atoms and ions technically have a strict place inside the crystal grid, but it is only a mean value -> they can get shifted form that palce by a small amount and then go back
	- this shift impacts all other atoms around it leading to restoring force -> oscialltion starts 

- this is important, because it influences
	- specific heat -> energy of the oscillation
	- temperatur transport  -> the way the osciallation waves move 
	- thermal expansion - anharmonic potential 
	- acoustic waves 
	- elastic waves 
	- optical effects in IR 

-  mathematical idea: 
	- local displacement results in restoring force (just like a spring)
	- we have energy $U = U(\vec r)$ 
	- displacement of atoms = change in the electron state - >change in optical, electrical and magnetic properties change 
	- the exact solution to how many oscillations there are is given by the hamilton operator $$\hat H = \sum_k \frac{\vec p^2_k}{2M} + \sum_i \frac{p^2_i}{2m} + \sum_{i<j} \frac{e^2}{4 \pi \epsilon_0 | \vec r_i - \vec r_j|} + \sum_{k \leq i} \frac{Z^2 e^2}{4 \pi \epsilon_0 |\vec R_k - \vec R_l|} - \sum+{i,k} \frac{|e^2}{4 \pi \epsilon_0 |\vec r_i - \vec R_k|}$$
	=> Problem: this is too complicated to actually solve. Therefore there are two possible approximations - [[Born Oppenheimer approximation]] and the [[harmonic approximation]] 
	

# 3.1. Phonons, dispersion , Zustandsdichte 
Useful approximations of the system in order to realistically solve the Hamiltonian from above
#### ![[Born Oppenheimer approximation]]
-> shifted electrons do not impact the nucleus; shifted nuclei take electrons with them 
#### ![[harmonic approximation]] 
-> imagine the atoms being masses and connected by a "spring" 


# ![[Quasiimpuls (crystal momentum)]]



### ![[dispersion relation]]

# interaction with close neighbrous 


## [[group velocity]] 
->  how fast energy gets transported (not matter, just energy)
-> is the velocity of the energy packet 
$$\nu_G \equiv \frac{d \omega}{d q}$$
In order to look at all atoms and the total picture: 
- In case of our circular frequnency $\omega(q) = 2 \sqrt{\frac{C}{M}} \sin (\frac{qa}{2})$ we get the group velocity as being $\nu_G = \sqrt{C \cdot \frac{a^2}{M}} \cos (\frac{qa}{2})$ 

Looking at the velocity at: 
- In centre of [[brillouin zone]] -> **langwellig** at $q \to 0$ gives $$\nu_G = \sqrt{C \cdot \frac{a^2}{M}}$$ 
- at the edge ov [[brillouin zone]] -> **standing wave** at $q = \frac{\pi}{a}$ gives $$\nu_G =0$$ 

# interaction with neighbhours that are far away 
-> atoms interact with all atoms, not only the close neighbours 
$$\omega^2 = \frac{4}{M} \sum_p C_p \sin^2 (\frac{pqa}{2})$$
-> it acts in the same way for centre and edge of [[brillouin zone]] as before 



# Oscillation energy
Given:  [[Hamilto operator]] for harmonic oscillation $$H = \frac{\vec p2}{2m} + \frac{1}{2} m \omega^2 x^2$$
- with eigenvalues $$E_n = \hbar \omega (n + \frac{1}{2})$$
- for N atoms -> 3N independand oscillations 
- boundary conditions: $n=0 (x=0)$ -> $exp(iqNa) = exp(0)=1$ 
	- total energy is all modes summed up $$E = \sum{\vec q r}(n_{\vec qr} + \frac{1}{2}) \hbar \omega+r (\vec q)$$where $r$ is the Dispersionszweig and $q$ is the wave vector 

# ![[phonon]] 
= a particle, that is the oscillation of frequency $\omega$ and wave vector $\vec q$ 


## [[acoustic branch]] 
we look at the behaviour of the frequency from the [[harmonic approximation#two types of atoms]] in centre and on the edge of the [[brillouin zone]] 
on the edge we get: $$\omega_- (\frac{\pi}{a}) = \sqrt{\frac{2C}{M_1}}$$
	-> it is a solution for the case with only one type of atom 
	- both atoms oscillate bascially with the same amplitude and phase 

# [[optical branch]]
Just like with the [[acoustic branch]] we look at the frequency on the edge of the [[brillouin zone]]: $$\omega_+ (\frac{\pi}{a}) = \sqrt{\frac{2C}{M}}$$
	-> both atoms oscillate out of phase and the Schwerpunkt stays in the same place $$\frac{u_0}{\nu_0} \approx - \frac{M_2}{M_1}$$

![[Kap. 3 grid oscillations 2025-12-21 16.46.21.excalidraw]]



# [[energy band gap]]
-> it is a gap in the [[dispersion relation]], so that there appears an area with oscillation frequencies, that are not possible 
(in 3D [[transversal modes]]s are allowed -> why is that so special?))

If crystal is bade up from ions: 
- optical branch has an oscillation out of phase -> optisch aktiv 
- in multiple atomic basis -> optica modes get created 
- for **p atomic** basis => 3 acoustic branches => ==3p -3== optical branches 

![[Kap. 3 grid oscillations 2025-12-21 16.59.08.excalidraw]]


### [[density of states (Zustandsdichte)]] for Phonons 
-> number of oscillation states in a frequency intervall 
General solution for the voume of a crystall: $$D(\omega) = \frac{q^2}{2 \pi^2} \cdot (\frac{\partial \omega}{\partial q})^{-1}$$
	for [[acoustic phonons]] $$D_{acoust} (\omega) \sim \omega^2$$
	[[optical phonons]] $$D_{opt} (\omega) = \delta (\omega - \omega_{opt})$$


## 3.2.1. Conservation of [[Quasiimpuls (crystal momentum)]] and energy
-> especially intersting in case of inelastic scattering, where we have absorbtion and emission 

In this case: 
- [[Quasiimpuls (crystal momentum)]] $$\vec k' = \vec k' +\vec G \pm q$$
- Energy $$E' = E \pm \hbar \omega_{ph} (\vec q)$$

#### Scattering types 
Dispersion relation $\omega (\vec q)$ can be determined by measuring $\vec k' - \vec k$ and $E' - E$ 

![[Stokes process]] 

![[Anti Stokes process]] 


## 3.2.2 Scattering on photons 
![[Pasted image 20260315120330.jpg]]

### scattering types and their intensity 
![[Pasted image 20260315121634.jpg]]


### types of scattering 
- ![[Rayleigh scattering]] 
- ![[Raman scattering]] - inelastic scattering on [[optical phonons]] 
- [[Brillouin scattering]] - inelasic scattering on [[acoustic phonons]]


## 3.3.1 specific heat capacity of a crid 
solid body can absorb warmth (thermal energy) via
- electrons 
- atomic nuclei (because of grid oscillations)
	- energy of the oscillations is quantised on [[phonon]]s -> $E = \hbar \omega$ 
	- energy of the grid $$U_{grid} = \sum_q [ \langle n_q \rangle + \frac{1}{2}] \hbar \omega$$
here $$\langle n_q \rangle = \frac{1}{exp(\frac{\hbar \omega_q}{k_B T}) -1}$$ is the [[Bose Einstein distribution]] 
 
at hight temperature ($k_B T >> \hbar \omega_q$) there is the approximation of $\langle n_q \rangle \approx \frac{k_B T}{\hbar \omega_q}$ 

### heat capacity derivation 
$$C_V = (\frac{\partial U}{\partial T})_V =\frac{\partial}{\partial T} 3 N k_B T = 3 N k_B$$

## Approximations for calculating the heat capcity
### ![[Einstein modell]] 

# ![[Debye Modell]] 

### Comparing those two models 
![[Pasted image 20260320135801.jpg]]


![[Pasted image 20260320141013.jpg]]


## 3.3.4. aharmonic effect: thermal expansion 
- in reality atoms are not prefect harmonic oszillators with $V \sim x^2$, but more something like $V (x) = ax^2 - bx^3 - cx^4$ 
	- $r^3$ is there for asymmetric repulsion 
	- $r^4$ is the dampending if the oscillation at higher amplitudes 
	- calculating the mean deflection gives the values $\langle u \rangle \approx \frac{3b}{4 a^2} k_B T$  => **thermal expansion coefficient** is $$\alpha_L = \frac{3b}{4a^2} \frac{k_B}{x_0}$$
![[Pasted image 20260320143024.jpg]]
#### In real crystals: 
- at $b=0$ there is no expansion and $b<0$ there is thermal contraction 
- thermal expansion coefficient can be different in the different directions in side the crystal and also temperature dependand ($\alpha_L (T)$) 

## ![[Three photon process]] 

## thermal conductivity 
- in solid bodies warmth gets transported via Phonons ans electrons (in metalls its mainly electrons)
- conductivity comes from a temperature gradient (difference in temperature in two places)
- thermal flow: 
$$\vec J_h = - \kappa \vec \triangledown T$$
=> Minus in the term means, that warmth flows from hot to cold 
$\kappa$ is generally a tensor, but in isotrop bodies a scalar 



Both $\langle n \rangle$ and $\langle U \rangle$ are thermal equillibrium quantity => it is important to consider the local fluctuations around the object. This lead to needed assumptions: 
- the variation of temperature in space is small -> assume to be homogenious, so that $\langle n \rangle$ 
- for two neighbouring spaces the temperature is different, meaning $\langle n \rangle \to \langle n(x) \rangle$ 


#### Calculate the thermal condictivity:
- we need to get $J_h$ dependand on $\langle n \rangle$ 
- thermal quantity $Q$ that gets transportet in time $\tau$ in $x$-direction through the $A$ surface with the energy density $\frac{U}{V}$ => define thermal quantity as $$Q = (\frac{U}{V}) \cdot A \nu_x \tau$$
where $\nu_x = \frac{\partial \omega}{\partial _x}$ is the mean phonon velocity 
![[Pasted image 20260321205907.jpg]]
- density of the thermal flux per surface $A$ in time $\tau$ in $x$- direction $$J_{h,x} = \frac{Q}{A \cdot \tau} = (\frac{U}{V}) \nu_x$$
- the internal energy U of the phonon system is: $$J_{h, x} = \frac{1}{V} \sum_{\vec q,r} \hbar \omega_{\vec q, r} (\frac{1}{2} + \langle n_{\vec q,r} \rangle ) \nu_x (\vec q, r)$$
- thermal flux exists only if the mean phonon number is deviating from the equillibrium $\langle n \rangle^0$ => $J_{h,x} = \frac{1}{V} \sum_{\vec q,r} \hbar \omega (\langle n \rangle - \langle n \rangle^0 ) \nu_x$ 
- Phonon number changes because: 
	- diffusion of phonons through the area 
	- phonon decay through [[three photon process]] $$\frac{ d \langle n \rangle }{dt} = \frac{\partial \langle n \rangle}{\partial t}|_{diffusion} + \frac{\partial \langle n \rangle }{\partial t}|_{decay}$$ 
	- special case: [[Boltzmann transport equation]]

- looking at stationary state $\frac{d \langle n \rangle }{d t} =0$  
	- from that we can calculate the coefficient for the thermal flow $$\kappa = \frac{1}{3} c_{\nu} \cdot \nu \cdot l$$with the mean free path $l=  \nu \cdot \tau$ 

- [[specific heat capacity]] of phonons and their [[group velocity]] is important for the thermal conductivity 
- the mean free path is imporant too -> is determined via scattering processes of phonons 
- before: dependancy on frequency disregarded 
- a couple simplifications 
	- [[optical phonons]]s disregareded at low temperatures 
	- [[acoustic branch]]es approximate with $\nu_r = \frac{\omega}{q} = const.$ 

#### Temperature dependance of thermal conducitvity 
- $\nu$  is approximately independand -> can be disregarded => look at mean free path $l$ 
=>  $l$ comes from scattering processes: 
##### phonon phonon scattering 
- from the phonon conversion we get $$l \sim \tau \sim \frac{1}{n_{ph}(T)}$$
	- in [[Normal process]]  -> total momentum conserverd => no thermal resistance 
	- finite thermal resistance only in [[Umklapp process]] -> total momentum changes, which allows the thermal resistance to become finite 
	
##### scattering on defects, on surface 
- scattering probablity depends on density of defects $n_D$ and scattering cross section $\sigma$ 
- extrinsic defect density depends on temperature => therefore the scattering probability too$$\sigma \simeq \pi a^6 q^4$$
- therefore caclulating the mean free path $$l \sim (n_D \omega^4)^{-1}$$
- point defects are the most effective for high energy phonons 
- very pure probes -> scattering length $l$ kan be bigger than the phonon expansion 
	##### metalls: electron photon scattering $$l \simeq d$$
##### magnetic materials: Phonon magnon scattering 
- using the [[Mattheissen rule]] we can add up all scattering rates, because they happen all at the same time $$\frac{1}{\tau} = \frac{1}{\tau_{P-P}} + \frac{1}{\tau_{def}} + ... \sim \frac{1}{l}$$

#### In total
- at low temperatures -> barely any phonons to scatter on, only defects 
- only $c_{\nu}$ is depentand on temperature -> visible in that graph of temperature to the thermal conductivity coefficient $\kappa$ 