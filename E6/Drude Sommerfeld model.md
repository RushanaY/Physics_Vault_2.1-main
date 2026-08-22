 
=>  where suddently the ideas: 
	- [[Pauli exclustion principle]] 
	- [[Fermi dirac distribution]] 
	become improtant are the innovative part 


We take the infinite [[potential well]] with $V= L^3$ and $T=0K$ 
-> electrone waves from the [[Schroedinger equation]] is $\psi_k (\vec r) = \frac{1}{\sqrt{V}} e^{i \vec k \cdot \vec r}$
	-> but that back into the Schroedinger equation gives the [[dispersion relation for electrons]] $$E(\vec k) = \frac{\hbar^2 k^2}{2m}$$
	each wave vector has 2 electronen states with the energy $$E_n = \frac{\hbar}{2m} [\frac{(2 \pi)^2}{L_x^2} n_x^2 + \frac{(2 \pi)^2}{L_y^2} n_y^2 + \frac{(2 \pi)^2}{L_z^2}n_z^2]$$


	
## [[density of states (Zustandsdichte)]] 

==number of states per energy unit== (also analogous to what a [[phonon]] does) 
- assume a cubic body!
- k value is $\vec k_{x,y,z} = \frac{ 2n \pi}{L_x,y,z}$ 
	- => 3D density of states $D(\vec k) = 2 \frac{V}{8 \pi^3}$ 
		- => energy of an electron per square $$E(\vec k) = \frac{\hbar^2 k^2}{2m}$$
- ![[electronic properties of metalls 2025-12-25 13.32.02.excalidraw]]

##  [[fermi energy]] 
- [[Pauli exclustion principle]] says that only 2 electrons with different spins can have the same eigen state 
- maximal possible energy when filling up the system is the fermi energy $E_F$ 
- $T=0$ gives a sphere with radius $k_F$ being the [[fermi sphere]], whose surface is [[fermi surface]] -> seperates filled from unfilled states 
- using the [[fermi wave number]] 
- there are also [[fermi velocity]], [[fermi wavelength]], [[fermi wave number]] and much more 


## [[fermi sphere]]
- at $T=0$ we have a sphere in the $\vec k$ space with the radius $k_F$ 
- ==it has all the filled states==


## [[fermi surface]] 
- it is the surface of the [[fermi sphere]]


## [[fermi wave number]]

Number of filled states:
$$N = 2 (\frac{V}{(2\pi)^3}) \cdot (\frac{4}{3} \pi k_F^3)$$
	$2 (\frac{V}{(2\pi)^3})$ :  [[density of states (Zustandsdichte)]] in the k space 
	$(\frac{4}{3} \pi k_F^3)$ :  volume of the k space 
=> we get the wave number $$k_{F, 3D} = (3 \pi^2 n_{3D})^{1/3}$$
# typical values 
For the electronic density of $n \approx 5 \cdot 10^{22}cm^{-3}$ we have the according values:
- fermi wave number $$k_F \simeq 10^8 cm^{-1}$$
- [[fermi energy]]$$E_F = \frac{\hbar k_F^2}{2m} \simeq 4 eV$$
- [[fermi temperature]] $$T_F = \frac{E_F}{k_F} \simeq 50 \space 000K$$
- [[fermi wavelength]] $$\lambda_F = \frac{2 \pi}{k_F} \simeq 1 \overset{\circ}{A}$$
- [[fermi velocity]] $$\nu_F = \frac{p_F}{m} = \frac{\hbar k_F}{m} \simeq 10^8 cm/s$$


# [[fermi gas]]
- for $T>0$ we get the [[Fermi dirac distribution]] being $$
- f_{FD} (E) = \frac{1}{e^{\frac{E- \mu}{k_B T}}+1}$$
with $\mu$ being the [[chemical potential]]	

==It is the probability that a state is filled==

$T=0K$
- all states under $E= \mu = E_F$ are filled 
- all states above are empty
$T>0K$ 
- electrons can be thermally exicted 
- those exited electrons leave the states with $E<E_F$ and go to states  with $E>E_F$
-> higher temperature means more electrons go on this journey and he calls it the "Umwandlung" 

Umwandlung:
- happens in the area of a around $k_B T$
- at toom temperature the percentage of electrons, that do the Umwandlung is: $$\frac{k_B T}{E_F} \approx 10^{-2} = 1\%$$
- heat capacity is in this case 
$$C_P = \gamma \cdot T + A \cdot T^3$$
	- the closest that experimental values are to the theoretical ones is in case of the alkali metals 
	- for transition metalls the assumtion of [[free electrons]] does not hols, because the d-orbit has too much influence onto the [[density of states (Zustandsdichte)]]
	- generally the expected values are not really what is measured -> reason is the fact that we did not consider all the other possible interactions (like elektron with crystal potential, electron with phonons, electron with eachother) -> the effective mass is therefore bigger -> has influence on the [[Beweglichkeit (mobility)]] (so it looks like they are still the free electrons, but heavier)

# electron density
# ![[electron density]] 
# [[heat capacity]] 
- it is caused by both [[phonon]]s and electrons 
$$C_V^{classical} = \frac{\partial \langle U \rangle}{\partial T}|_V = 2 \cdot N \cdot 3 \cdot \frac{1}{2} k_B = 3 N k_B$$
# [[specific heat capacity]] 
$$c_v = \gamma \cdot T$$
with the [[Sommerfeld coefficient]] $$\gamma = \frac{\pi^2}{2} = \frac{n k_B}{T_F}$$
The reason why it is so different to the heat capacity on its own is again Pauli principle. For the most electrons part of their degrees of freedom are "forzen", unusable because the space is already taken up by someone else. 



More to find in the [[Kap. 4 electronic properties of metalls]]
