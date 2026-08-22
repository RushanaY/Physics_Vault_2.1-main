### Drude Model 
-> classical describtion of electron gas  
- therefore assumption if the Maxwell Boltzmann distribution ended up being wrong
- accidental correct describtion of derivation of Ohms law and the relation of electric and thermal conductivity 

Modell was not perfect -> needed to be updated

### Drude Sommerfeld model
This model has added ideas of: 
-  [[Pauli exclustion principle]] 
-  [[Fermi dirac distribution]] 
	become improtant are the innovative part 

#### Dispersion relation 
We take the infinite [[potential well]] with $V= L^3$ and $T=0K$ 
-> electrone waves from the [[Schroedinger equation]] is $\psi_k (\vec r) = \frac{1}{\sqrt{V}} e^{i \vec k \cdot \vec r}$
	-> but that back into the Schroedinger equation gives the [[dispersion relation for electrons]] $$E(\vec k) = \frac{\hbar^2 k^2}{2m}$$
	each wave vector has 2 electronen states with the energy $$E_n = \frac{\hbar}{2m} [\frac{(2 \pi)^2}{L_x^2} n_x^2 + \frac{(2 \pi)^2}{L_y^2} n_y^2 + \frac{(2 \pi)^2}{L_z^2}n_z^2]$$


	
### [[density of states (Zustandsdichte)]] in the Drude Modell 
-> we have a [[dispersion relation]] of the energy and we also know the allowed energies => from that we have get the number of states per energy unit 
Assume: cubic body with sides of length $L_{x,y,z}$ in the 3D inrinite dimentional [[potential well]]

number of states per energy unit in this cubic body(also analogous to what a [[phonon]] does) 
- assume a cubic body!
- k value is $\vec k_{x,y,z} = \frac{ 2n \pi}{L_x,y,z}$ 
	- => 3D density of states $D(\vec k) = 2 \frac{V}{8 \pi^3}$ 
		- => energy of an electron per square $$E(\vec k) = \frac{\hbar^2 k^2}{2m}$$
![[Pasted image 20260313212857.jpg]]

- ![[electronic properties of metalls 2025-12-25 13.32.02.excalidraw]]



##  [[fermi energy]] 
- [[Pauli exclustion principle]] says that only 2 electrons with different spins can have the same eigen state 
- maximal possible energy when filling up the system (starting at the bottom) is the fermi energy $E_F$ (at $T=0$ is $E_F$ the line between filled and empty states)
- in order to remove an electron from the metall -> Austrittsarbeit $\Phi$ needed -> this means the assumption of being an infinite potential well is correct 
- $T=0$ gives a sphere with radius $k_F$ being the [[fermi sphere]], whose surface is [[fermi surface]] -> seperates filled from unfilled states 
- using the [[fermi wave number]] 
- there are also [[fermi velocity]], [[fermi wavelength]], [[fermi wave number]] and much more 


#### ![[fermi sphere]]


#### ![[fermi surface]] 



#### ![[fermi wave number]]

#### Number of filled states:
$$N = 2 (\frac{V}{(2\pi)^3}) \cdot (\frac{4}{3} \pi k_F^3)$$
	$2 (\frac{V}{(2\pi)^3})$ :  [[density of states (Zustandsdichte)]] in the k space 
	$(\frac{4}{3} \pi k_F^3)$ :  volume of the k space 
=> we get the wave number $$k_{F, 3D} = (3 \pi^2 n_{3D})^{1/3}$$
#### typical values 
For the electronic density of $n \approx 5 \cdot 10^{22}cm^{-3}$ we have the according values:
- fermi wave number $$k_F \simeq 10^8 cm^{-1}$$
- [[fermi energy]]$$E_F = \frac{\hbar k_F^2}{2m} \simeq 4 eV$$
- [[fermi temperature]] $$T_F = \frac{E_F}{k_F} \simeq 50 \space 000K$$
- [[fermi wavelength]] $$\lambda_F = \frac{2 \pi}{k_F} \simeq 1 \overset{\circ}{A}$$
- [[fermi velocity]] $$\nu_F = \frac{p_F}{m} = \frac{\hbar k_F}{m} \simeq 10^8 cm/s$$

Remark:
- $\lambda_F$ is the size of the distance between atoms => probably there will be a lot of diffraction effects on the nuclei 
- $T_F >> T_{melting}$ => usually it is the other wayt round, because electrons in solid states are quantenentartet 
	- the initial statement is the case if we have heavily diluted quantum gas (happens in weak [[dotiert]] Semiconductors or optical traps or hot and dense plasma (sun or fusion plasma))
	- velocity of classical electron gas $\nu_{th} \simeq 10^7 cm/s << \nu_F \simeq 10^8 cm/s$ 
		- -> electrons appear to move faster as it is expected according to the classical theory 
	- total energy of the system goes from a sum to an integral $$E_{ges} = 2 \frac{V}{(2 \pi)^3} \int_0^{k_F} \frac{\hbar^2 k^2}{2m} 4 \pi k^2 dk = \frac{V}{10 \pi^2} \frac{\hbar^2}{m} k_F^5$$
		- with particle density $n_{3D} = N/V$ and definition of $k_{F,3D}$ we get $$\frac{E_{ges}}{N} = \frac{3}{5} E_F = \frac{3}{5} k_B T_F$$
		- -> but in classical gas we have $\frac{E}{N} = \frac{3}{2} k_B T$ 
		- this means, that at $T \to 0$ there is still energy per particle left => reason: [[Pauli exclustion principle]] 



#### ![[fermi gas]]


### 
# ![[electron density]] 

#### ![[chemical potential]]





### 4.1.3.  [[heat capacity]] 
- it is caused by both [[phonon]]s and electrons 
$$C_V^{classical} = \frac{\partial \langle U \rangle}{\partial T}|_V = 2 \cdot N \cdot 3 \cdot \frac{1}{2} k_B = 3 N k_B$$
# [[specific heat capacity]] 
$$c_v = \gamma \cdot T$$
with the [[Sommerfeld coefficient]] $$\gamma = \frac{\pi^2}{2} = \frac{n k_B}{T_F}$$
The reason why it is so different to the heat capacity on its own is again Pauli principle. For the most electrons part of their degrees of freedom are "forzen", unusable because the space is already taken up by someone else. 


