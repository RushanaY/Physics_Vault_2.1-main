# Modell 
![[Pasted image 20260225181009.jpg]]
### non relativistic Hamilton operator for H atom in CMC
$$ H = \frac{\vec p^2_e}{2m_e} + \frac{\vec p^2_K}{2m_K} + V(|\vec r_e - \vec r_K|)$$
	Transforming the operator into the [[center of mass system]]:  $$H = \frac{\vec p^2}{2M} + \frac{\vec p^2}{2 \mu } + V(r)$$
		with:
		- relative coordinate:  $\vec r = \vec r_e - \vec r_K$ 
		- total mass: $M = m_e + m_K$ 
		- reduced mass : $\mu = \frac{m_e m_K}{m_e + m_K}$ 
		- [[Coloumb potential]] : $V(r) = - \frac{1}{4 \pi \epsilon_0}\frac{Z  e^2}{r}$ 
		
		
### non relativistic Hamilton in spherical coordinates
Transforming into spherical coordinates and solving it, gives two differential equations:
	1. **Winkelanteil**$$L^2 Y = \hbar^2 const Y = \hbar l(l+1) $$
		==Solution: $$Y_{lm}(\Theta, \Phi)$$==
		this is an **eigenfunction**, also called the [[Spherical harmonics function]]:  $$L^2 Y_{lm} (\Theta, \Phi) = \hbar^2 l(l+1) Y_{lm} (\Theta, \Phi)$$$$L_z Y_{lm}(\Theta, \Phi) \hbar m_l Y_{lm}(\Theta, \Phi)$$
			where $m_l = -l, ...,0,...l$ 

1. **Radialanteil** DGL $$(- \frac{\hbar^2}{2 \mu} \frac{1}{r} \frac{\partial}{\partial r} (r^2 \frac{\partial}{\partial r} ) + \frac{\hbar^2}{2 \mu}\frac{l(l+1)}{r^2} + V(r) ) R = ER$$
		==Solution==: $$R(\rho) = e^{\rho/2} \rho^l \sum_{j=1}^{\infty} a_j \rho^j$$
			with:
			- [[Fine structure constant]] $\alpha = \frac{e^2}{4 \pi \epsilon_0 \hbar c}$ -> $V(r) = \frac{\alpha \hbar c}{r}$ 
			- $\rho = 2r \sqrt{\frac{2 \mu |E|}{\hbar^2}}$
			- $E := - \frac{1}{2} \mu c^2 \alpha^2 \frac{1}{\lambda^2}$ with $\lambda$ being a reel number 
				- using **Recursion relation** $$a_{j+1} = \frac{j+l+1- \lambda}{(j+1) (j+2l +2)}$$
					- $l$ - [[angular momentum quantum number]]  
					- $n$ - Hauptquantenzahl 
		- we get the [[Eigenenergy]]: $$E_n = - \frac{1}{2} \mu c^2 \alpha^2 \frac{1}{n^2}$$
			- only descreet energies possible 
![[Pasted image 20260225181158.jpg]]
## 3.0.2. Radial wave function
##  radial position probability
$$W(r)dr = e^{-2r/a_0} r^2 dr$$
- has maxima at $r = \frac{\hbar}{\mu c \alpha} = 0.52197...\cdot 10^{-10}m = a_0$ 
- the zero points of $R(\rho)$ are the osciallation nodes of the wavefunction
	- it has $j_{max} = n - l -1$ points 
![[Pasted image 20260225181222.jpg]]
## Radial probability density 
$$D_{nl} (r) dr = r^2 |R_{nl} (r)|^2 dr$$
- the porbability of an electron to be found in one of the orbitals 
- for:
	- $l =0$ $\psi_{nlm}$ has a finite value at $r=0$$$|\psi_{n00} (0)|^2 = \frac{1}{4\pi} |R_{n0} (0)|^2 = \frac{Z^3}{\pi a_\mu^3 n^3}$$
	with $a_{\mu} = \frac{4 \pi \epsilon_0 \hbar^2}{\mu_e^2} = a_0 \frac{n}{\mu} \approx a_0$ 
	- $l \neq$ 0 there is no $\psi$ for $r \to$ 0 because of the **centrifugal barrier** 
		- Interpretation: electron can't come close to the nucleus 
- the densicty has $n-l$ **minima**  at $$r = \frac{n^2 a_{\mu}}{Z}$$

## states 
- Angular momentum $l$:
	- has $m_l = 2l +1$ substates 
	- if the states $l$ have the same energy, then they are called [[degenerate]] 
- Principal quantum number $n$: 
	- has $n-1$ angular moment states 


# [[angular momentum operator]] 
### Parity of eigenfunction
$$\hat P \{R_{nl}(r) Y_{lm} (\theta, \phi)\} = R_{nl}(r) (-1)^l Y_{lm} (\theta, \phi)$$
### Stern Gerlach experiment 
- particle is being deflected by $$E = - \vec \mu \vec B$$
- force on the atom: $$F = - \triangledown (- \mu_z B_z) = \mu_z \frac{\partial B_z}{\partial z}$$
- electron around the nucleus has magnetic moment of $$\vec \mu_l = - \frac{e \hbar}{2m}\frac{l}{\hbar} = - \mu_g \frac{l}{\hbar} = - g_l \mu_B \frac{l}{\hbar}$$
	with 
	- $\mu_B$ being the bohrs magneton 
	- $g_l$ being the g-factor 
		- if it's the orbital angular momentum, then $g =1$ -> $\mu_{l_z} = - g_z \mu_B m_l$


# Zeeman effect 
- normal Zeeman effect
	- we can observe the l quantasation 
- abnormal Zeeman effect 




# [[Fine structure]] 

# Instrument for that

![[Spin quantum number]] 
 
=> $$\psi_{nlm_l} m_s = \psi_{nlm_l} \otimes \chi_{m_s}$$
# Correction terms
## Relativistic mass 

$$\triangle E_n' = =\frac{\alpha^2 Z^2}{n^2} E_n (\frac{3}{4} - \frac{n}{l + \frac{1}{2}})$$
## Spin Orbit interaction 

$$\triangle E' + \triangle E'' = -\frac{\alpha^2 Z^2}{n^2} E_n \{\frac{3}{4} - \frac{n}{j + \frac{1}{2}} \}$$
with
- total angular momentum $$j = \vec s + l$$
	$j = l \pm \frac{1}{2}$ 

 

## [[Darwin Term]]
$$\triangle E' + \triangle E'' + \triangle E ''' = - \frac{\alpha^2 Z^2}{n^2} E_n (\frac{3}{4} - \frac{n}{j + \frac{1}{2}}) $$


# [[Lamb Shift]]
we quantise the electro magnetic field just like a harminic oscillator from quantum electrodynamics. It has qunatum fluctuations in the basis state, which the electro magnetic field also has 



























# working forces and models on a Hydrogen atom 
- solving of a central potential with Schrodinger equation and using radial functions 
- reducing of the solution to a effectiv potential 

# Radial wave functions
-> Bascially everything form T2 

# Angular momentum operator 
$L^2 Y(\theta, \phi) = \hbar^2 const Y (\theta, \phi)$  

## bound states 




lecture notes 11.06.25 fine structure of hydrogen atom part 2
- recap [[fine structure]] -> states with the same j are degenerate
- somehow counting the states 

[[Lamb Shift]] -> quantenelectrodynamics (= QED)
- before: $\vec E (\vec r, t)$ classical but semiclassical observations
- then quantisie the field and get an operator for the e field: $$\vec E \equiv \hat E$$
	therefore $\vec x \equiv \hat x$
	- x and p are not as definite in QM
	- Example is a [[harmonic osciallator]]. Position in QM, expected value $\langle \hat x \rangle = 0$ and $\langle \hat x^2 \rangle =0$
	- if we want to measure the position x, we won't get one value. The distribution of all measured positions will correlate to the [[Gauss distribution]] => **quantum fluctuation** 

- in QED $\vec E \to \hat E$ $$\langle \hat E \rangle_{vacuum} =0$$$$\langle \hat E^2 \rangle \neq 0$$
	- if we measure the E field and their place?amount? , it also gives the Gauss distributuion 
		- -> **vacuum field fluctioations**
			- the position of the electron fluctuates -> potential energy fluctuates um $$\triangle V = V(\vec + \delta \vec r) - V(\vec r) = \delta \vec r \triangledown V + \frac{1}{2} (\delta \vec r \triangledown)^2 V(\vec r) + ...$$
			to derivation: he [[Taylor expansion|taylor expanded]] the term
		- with: $$\langle \delta \vec r \rangle_{vaccum} =0$$$$\langle (\delta \vec r \cdot \triangledown)^2 \rangle = \frac{1}{6} \langle(\delta \vec r)^2 \rangle_{vaccum} ..$$
		- [[Hans Bethe]] - look up
	visualisation: ![[Pasted image 20250611123957.jpg]]

- Lamb + Rutherford
- ![[Pasted image 20250611124110.jpg]]
	- collistions with electrons can be shown in form of current (like Franck Herz experiment)
	- detectro shows spesifically 2S Atoms, not 2P
	- ![[Pasted image 20250611124516.jpg]]
- more about the QED effect: in dirac theory $g_S = 2$ 
	- is supposed to be exacly two, but experimets show that it is not that exact. 
		-> in QED: $$g_S = 2 (1 + \frac{\alpha}{2 \pi} - 0.328 \frac{\alpha^2}{\pi^2} + ...) = 2.002319 \space  304 \space 361 \space 7 (152)$$))
	- with presicion experiment $g - 2$ $$\vec \mu = -g_S \mu_B \frac{s}{\hbar}$$


- Influence of the kern 
- ![[Pasted image 20250611125325.jpg]]
	- Isotropieverschiebung 
		- VERy Important: $$E_n = - \frac{1}{2} \mu c^2 \frac{(Z \alpha)^2}{n^2}$$
			with reduced mass $\mu = \frac{m_e \cdot m_K}{m_e + m_K} = m_e \cdot \frac{1}{1 + \frac{m_e}{m_K}}$ 
	- for case of Deuterium atom 
	- ....
		- endresult: $$\frac{E_H}{E_D} = \frac{\mu_H}{\mu_D} \sim 1 = \frac{1}{2} \frac{1}{1836}$$
		- general case with A being the Massenzahl$$m_K = A \cdot m_N$$$$m_K' = (A+1) m_N$$$$\frac{\mu_K}{\mu_K'} \sim 1 - \frac{1}{A(A+1)} \frac{m_e}{m_N}$$
		- => $$\frac{\triangle E}{E} \sim - \frac{1}{A^2} \frac{1}{1836}$$bigger and heavier kern need less corrections
- Volume effect 
	- a simple modell for a proton 
	- its force dostribution (just like any case of a homogeniuous sphere)![[Pasted image 20250611130222.jpg]]
	- for the force: 
		- $r < r_0$ : $F = - \frac{Z e^2}{4 \pi \epsilon_0} \frac{r}{r_0^3}$
		- $r > r_0$ : $F = - \frac{Ze^2 }{4 \pi \epsilon_0} \frac{1}{r^2}$
	- by integrating that, we get the potential 
	- for pertubation operator -> from QM T2:$$\triangle V := V_{eff} - V_{Coulomb}$$
		- $r < r_0$ : $\frac{Ze^2}{4 \pi \epsilon_0 2 r_0} ((\frac{r}{r_0})^2) + \frac{2 r_0}{r} - 3)$  ....
		- otherwise 0
- general notes:
- use something different that an electron to make a hydrogen atom? becaus ea myon, for example is much much heavier (less pertubation needed?) . much smaller charge radius, more sensitivity 
- better for spectography 
- more precise size of a hydrogen atom possible 


- Hyper fine stucture 
	- in general :electron and kern have different intertias an tork ->there are two sets of formulars for both of them (are all in the script)
	- Important fomulars:$$\vec E_{Hub} = - \vec \mu_K \vec B_{el}$$$$E_{FS} =  \vec \mu_S \vec B_e$$-> is $\propto \vec e \cdot \vec s$  
	- reminder [[Bohrs Magneton]] $$MB = \frac {e \hbar}{2m_e}$$
	- Commentary to it all
		- get all tork and inertia formulars for electron and kern int he magnetic field of each other 
		- put all rogether into a hamitlon operator
		- find eigenstatese and eigenvalues of that thing
		- this allows to describe the atom very very presicely in the qm way
		- Tensorproduct! 

there is a connection to [[Astro 1]]! fine structure is important for soemthing for meteorites -> "21 m line" 

----------

# Relativistic effect 
-> [[Schroedinger equation]] does not cover spin

- [[Stern Gerlach experiment]] shows existence of [[spin]] 
