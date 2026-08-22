## 4.1 ![[free electron gas]] 


## 4.1.1. ![[Drude (Sommerfeld) model]]





## 4.2. Transport propertis

### 4.2.1.  ![[electric conductivity]]
### in the [[Drude (Sommerfeld) model]] 
- assumption: **electrons move with mean velosity** $\nu_{th}$ 
- accelerated with the el field $\vec E$, collide with atomic core => lose velocity because of friction 
- [[drude mean velocity]]$$\vec \nu_D = - \frac{e \tau}{m} \cdot \vec E = - \mu \cdot \vec E$$
	$\tau$ - characteristic collistion time (probably the amount of time the collistion takes)
	$\mu= \frac{e \tau}{m}$ - [[Beweglichkeit (mobility)]]   


### in the [[Sommerfeld model]] 
- assume free, [[fermion]]ic gas => abides by the Schrodinger equation and Pauli principle 
- in thermal equillibrium $\langle \vec k \rangle =0$ there is not current flow 
- for current flow we need the mean of momentum (wave vector) of electrons to change 
- -> this is posisble though external forces or through scattering 
	- in case of scattering we need to consider [[relaxation]] (like in the Drude model) 
- we want the momentim of the electron to be changed in time $t$ through the force $\vec F$ by the absolute value of $\hbar \partial \vec k$ 
- => is the same as the shift of the [[fermi sphere]] by $\partial \vec k$ in time $t$ 
#### application in the Fermi sphere
- electric field leads to shift of the fermi sphere by $\delta \vec k$ 
- states inside the area of the sphere get shifted 
- after electric field is turned off => sphere gets shifted back into the original state via scattering with $\delta \vec k \sim e^{- t/\tau}$ 

#### why fermi velocity and not drift velocity? 
-> biggest energy that gets transmitted by scattering is $$E_{scattering} \approx  k_B T << E_F$$
- only electrons on the [[fermi surface]] can participate in scattering processes (because anywhere else there are no filled states to scatter on)
- those electrons have $| \vec \nu| \approx \nu_F$ 
- typical shift in the fermi sphere is ca. $\delta k/k_F \simeq 10^{-5}$ 
- => a small number of electrons move with $\nu_F$, where as in Drude modell all electrons move with $\nu_D << \nu_F$ 
![[Pasted image 20260322123146.jpg]]



####  temperature dependance of the conductivity and resistance 

General relation from experimets is:  $$\rho = \sigma^{-1}$$
from the equation : $$\rho^{-1}_{el} = \sigma_{el} = \frac{ne^2 l}{m \nu_F} = \frac{ne^2 \tau}{m}$$
	we see that only $l$, or better so $\tau$ are temperature dependant
	-> in metalls scattering is usually from 
		- phonons
		- defecs 
		- surface of the object 
		=> scatterin time is therefore from the [[Mattheissen rule]] $$\tau^{-1} = \tau^{-1}_{phonon} + \tau^{-1}_{defect}...$$
		this allows to look at all scattering parts seperately

### electric conductivity in different cases 
### ![[electron phonon scattering]]

### ![[electron defect scattering]] 

#### experimentally
- the scattering changes the conductivity a lot and has to be considerd, because there are no pure enough crystals that wouldn't at least have the scatterin on defects -> leads to [[Restwiderstand (residual resistance)]] 
-> we need the [[residual resistans ratio (restwiderstandsverhältnis)]] $$RRR = \frac{\rho(300K)}{\rho_0}$$
![[Pasted image 20260322123907.jpg]]

### 4.2.2.  [[thermal conductivity]]
Definition:
$$\vec J_h = - \kappa \cdot \triangledown T$$
Comparing with [[electric conductivity]] we get the [[Wiedermann Franz law]] $$\frac{\kappa}{\sigma_{el}} = \frac{\pi^2}{3} (\frac{k_B}{e})^2 T$$
-> this makes sense, because in metalls both electric and thermal are important

The ration of those two in metalls is the proportionality number [[Lorenz number]] $$L = \frac{\pi^2}{3} (\frac{k_B}{e})^2 \equiv \frac{\kappa}{\sigma \cdot T} = 2.44 \cdot 10^{-8} W \Omega/K^2$$
####  temperature dependance 
- there is a maximum of thermal conductivity
- the maximum is better visible in low temperature, but the material has to be clear 
- in alloys there is no maximum (to "dirty")
![[Pasted image 20260322124001.jpg]]


### 4.2.3. mobility in magnetic fields 
-> in [[electric conductivity]] electrons move because of a nelectric field 
taking the part of the frequency we get the [[cyclotron velocity]] $$\omega_c \equiv \frac{e}{m} B$$
Actuallty this effect is nicely sumed up in the:
# [[Hall effect]]
![[thermal conductivity 2025-12-29 17.09.40.excalidraw]]

Describtion:
- we have an E field along a conductor and the whole thing is inside a B field, orthogonally 

 -> from the measurement of the [[Hall constant]] we can get the algebraic sign (Vorzeichen) of the charge carrier in the solid body 


------------ 

==Modells for calculating electic transport:==  

# [[Drude modell]]
- ==classical==
- assumption: **electrons move with mean velosity** $\nu_{th}$ 
- accelerated with the el field $\vec E$, collide with atomic core => lose velocity because of friction 
- [[drude mean velocity]]$$\vec \nu_D = - \frac{e \tau}{m} \cdot \vec E = - \mu \cdot \vec E$$
	$\tau$ - characteristic collistion time (probably the amount of time the collistion takes)
	$\mu= \frac{e \tau}{m}$ - [[Beweglichkeit (mobility)]]   






## 4.3  [[energy band]] 
- expansion of the free electron gas theory, by putting the electron in the potention of the nuclei and other electrons 
-> it leads to a complicated [[Schroedinger equation]], reminding of the [[pertubation theory]] from quantum mechanics 

In order to solve it there are two ways to look at the problem, which go from the opposite sides, but end up in the same place: 

### 4.3.1.  [[quasi free electron]] 
- assume electrons are free to move, therefore the potential of the nulceus and other electrons is assumed to be a non important pertubation -> $V(\vec r) =0$ 
- a good approximation for [[delocolised electron]]s 

### 4.3.2. Tight binding modell 
## [[quasi bound electron]] 
- start at localised electrons 
- [[Tight binding method]]: interaction of electrons between neighbouring atoms new orbitals get created -> those can be described though a linear combnation of teh atomic orbitals 

==both of the approximations of quasi free and quasi bound electrons end up showing the existance of the [[energy band]]s and [[energy band gap]]s== 

ANother thing that becomes relevant in all those apporximations, is the [[effective mass]], which comes from the dispersion relation: $$m^* = \frac{\hbar^2}{2 \beta^i a^2}$$






# 4.4 Metalls, semicinductors, isloators 
# Definitions of metal, semi conductor and half metal
 we need for the definition ->  [[energy band gap]] (because the atoms are so close to eachother)
- the filling of those bands at $T=0K$ is just like in [[fermi gas]]  -> the states get filled from the bottom and all electrons get a place 

with $E_G$ we mean the energy of the gap! 
## [[metall]]
- states arae empty inside the energy gap
- current flows if an electric field applied 

## [[semiconductor]]
- $E_g \leq 4eV$ -> current flow at $T=0K$ and no current at $T>0$ 

## [[isolator]] 
-> when $$E_g >= 4 eV$$
-> for $T>0$ there is no current possible 


In the middle (at 3 or 4 eV) the conductivity is very much temperature dependant 

## [[Halbmetall]] 
-> here what happens is a small **overlapp** of the [[energy band gap]]s 
- overlapp small, [[density of states (Zustandsdichte)]] very small => small number of current carrierers
- nevertheless there is still current flow at $T=0K$ 
-  another effect of the overlapp -> different [[dispersion relation]] in different directions of the crystal 



==crystals are halbmetalle==


## 4.4.1.  number of states in the band
-> helps to determine if a **crystal** is an isolator or a metall

- in case of [[quasi free electron]]s :
	- 
## 4.4.2 band structure, state density 



# 4.5 Fermi surfaces of metals 
## 4.5.1.  [[free electrons]] 
change in temperature, specifically the increase changes the way the states are filled, but only in the neighborhood of the [[fermi surface]]
in case of free electrons the fermi surface is a cicle 
the [[electron density]] from that coems from the [[fermi energy]] gives then the [[fermi wave number]] in 2D is then $$k_F = \sqrt{2 \pi n_{2D}}$$
- fermi radius is dependand on the electrondensity and the number of valenz electrons 
- this leads to big differences between fermi surfaces 
- in case of small electron densities - >fermi wave vector is also small (wow, logical)
- the fermi circe (the fermi surface) is completely **inside** of the first [[brillouin zone]] => just as we expect from free electron gas 
- if the fermi wave number is bigger -> fermi surface outside of the first brillouin zone 
	- 1BZ barely filled 
	- 2BZ partly filled, looks like ovals in the periodic scheme 
	- 3BZ is empty 
- more overfilling of the zones leads to the 3BZ having "spikes" and the 2BZ to hve "holes" => this can be easily shown by drawing onw zone and making it periodic 

## 4.5.2. almost free electrons 
almost free electrons
- there are energy band gaps on the borders of the BZ 
- schroedinger equation at the borders of the zone is solved by standing zones 
	- gradients of $E(\vec k)$ are parallel to the BZ border 
	- the lines of constant energy $E (\vec k)$ are prependicular to the BZ 

- important
	- crystal potential rounds to corners of the BZ 
	- the total volume that is inside of the fermi surface is dependand on the number of electrons => has to stay the same 

- what is it in metalls?
	- alkaline: in bcc structure -> fermi surface is very much inside the first BZ  and is shaped like a sphere 
	- edelmetall: also inside the first BZ, but the borders get touched and the sphere doesn't look as perfect 

## 4.5.3. electrons in magnetic fields, electron and hole orbits , measurement of fermi surfaces 
Experimentsl determination of the shape pf the fermi surfe 
- electron move orthogonal to the magnetic field and the enregy gradient 
- for movement ew need free electron states => lokated at the boundaries of the surface 
- depending on the f surface the electrons might behave like gaps in magnetiv fields 
- almost empty bands -> orbits look like made from the electrons 
- almost filled bands -> gap orbits 
- differenc in orbits between:
	- open orbit -> get continued in the periodic zone scheme 
	- metalls might have both types 
- a metall can be exited along one direction of the zone and this leads to oscillation in certain periods and certain directions too
- basically exiting the metall in acertain direction will show what kind of fermi surface it 

# 4.6 Electrons and gaps 
we go back to the idea of [[effective mass]] and especially the strange  idea of it being negative 

-> happens if we don;t use the modell with free electrons 

- effective mass is give though the curvature of the band at the place of $k_0$ 
- looking at this place closer , it shows the relation if acceleration and force as being $$\vec a \sim - \vec F$$
- this way we get the negative mass 
- but instead of having this bad consept we can switch the Vorzeichen -> we get a particle , with positive mass, that is the we call a **gap** , which moves in the opposite direction 

- a gap is a quasi particle 
	- behaves just like a particle, but is not one. we need it so we don't have to suffer with negative mass 
	- wave vector 
		- full band has $\sum \vec k =0$ -> if we take one electron out we get the negative wave vector $- \vec k_e$ 
	- energy
		- same idea -> negative energy 
		- in free states the particles go in the dispersion relation 
			- electrons go down
			- gaps go up 
	- effective mass
		- negative mass possible 
	- velocity
		- $\vec \nu_h (\vec k) = \vec \nu_e (\vec k)$
	- equation of motion 
		- gaps move like paricles with postivie charge (bascially negaitve mass)



