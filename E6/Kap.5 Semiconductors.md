# 5.1 Classification of [[semiconductor]]s: 
- we use the [[energy band gap]] -> has to be less than $0 < E_g < 4eV$  
- at $T=0K$ all electrons are under the [[fermi energy]] have an infinite [[specific resistance]]  
- at $T> 0K$ resistance gets smaller because charge carrier get created thermaly 
- anuything bigger than zero -> less resistance -> current flows 


## types of semicoductors:
- [[intrinsic]] (pure) and [[dotiert]]e (mixed with other atoms) semic onductors 
- [[cristalline]] and [[amorph]] semiconductors 
- direct and [[indirect semiconductors]] (differ in their optical transitions)
- element semiconductors:
	- group IV: graphit, si ,gem zinn, P , se , te 
	- very pure stuff:[[Czochralski procedure]]  -> Silizium
#### Production of element semiconductors
- [[Czochralski procedure]] 
	1.  take very pure silizium  
	2. melt it down
	3. put in a small Si Impfkristall
	4. Einkristall gets pulled out of the melted substance, while rotating
	5. diamteter of this cylinder gets determined through rotation velocity and the pull veliocity 

#### Verbindungshalbleiter
- binary 
	- group III -IV
		- switch one electrons from an atom of the IV and II groups - >get a new material with properties liek an Elementhalbleiter 
		- iotnischer type of the bounding -> bigger band gap htan the normal material would have 
		- important: GaAs, AIAs, GaN, InP, InSb
	-  II -VI
		- more ionic than the II-CV semiconductor 
		- even bigger band gap
		- exeption is, if there is Hg in the connection 
		- important ones that work: CdD, CdSe, ZnTe, ZnO, HgTe
- ternäre 
	- legierung of two semiconductors 
- quantiär
	- also a Legierung 
	- with the properties 
		- [[Vergards rule]] $$a_{Al_xGa_{1-x}As}= x \cdot a_{AlAs} + (1 -x) \cdot a_{GaAs}$$
			which is a good approximation 
- important for the alloy components -> identical crystal structure, grid constant and radius of the ion also have to be similar 

#### organic semiconductors 
- usually electrically isolating 
- if they have a conjugated binding system from double or triple connection or aromatischen Ringen , then they are electrically conductive 
- differentiation by molar mass
	- conjugated mass: Angharcen, Perylen
	- conucated Polymer: Polyanilin, POlkyacdtylen 
- they are cheaper to produce, are lighter and bendy
- porblem: don;t hold for very long and are not as stable 


# 5.2 Intrinsic semiconductors 
## 5.2.1. structure of the band and effective mass 
- at $0K$ the [[fermi energy]] lies between two gaps 
- the botttom gap is called the **Valenzband** (VB) and the upper one is called the **Leitungsband** (LB) 
- the band gap is then the difference of the Maximum of VB -> VBM and the Maxmimum of the LB -> LBM $$E_g (T = 0K) = E_{LBM} - E_{VBM}$$
the gap is also temperature dependant: $$E_g (T) = E_g (T =0) - \frac{aT^2}{T _b}$$we differentiate between **direct** and [[indirect semiconductors]]: 
- direct
	- VBM and LBM are in the same point in the k space 
- indirect
	- VBM and LBM are in different points 
![[Kap.5 Semiconductors 2026-02-21 18.20.05.excalidraw]]
- Important SD values 
	- Si: $E_g^{indirect} = 1.12 eV$
	- CdS: $E_g^{direct} = 2.58 eV$
	- GaAs: $E_g^{direct} 1.519 eV$
	- GaN: $E_g^{direct} = 3.28 eV$ 

many important SC (semiconductor) have the properties of the [[angular momentum quantum number]] and the [[Spin quantum number]] :
- LB has $l=0$ 
- VB has $l=1$ 
- then the total angular momentum $j$ is for the bands:
	- LB: $j = 1/2$, $m_j = \pm 1/2$
	- VB: $j = 3/2$, $m_j = \pm 3/2$ (**heavy hole**) and $m_j = \pm 1/2$ (**light hole**) 
		- $j=1/2$ , $m_j = \pm 1/2$ (**spin orbit split hole**)
## 5.2.1. spin orbit interaction 
because of the interaction the energy of **heavy and light hole gets increased** and the **energy of splitted hole gets decreased**
=> tha magnitude of the interaction is measured in $\Delta$ 
	$\Delta_{Ge} = 290meV$, $\Delta_{GaAs} = 350 meV$ , $\Delta_{Si} = 44meV$, $\Delta_{diamant}  =6 meV$ 

a light hole ->  a strong curvature gives a small [[effective mass]] $m_{lh}^*$ 
a heavy hole ->  small curvature gives a big effective mas $m_{hh}^*$ 
![[Kap.5 Semiconductors 2026-02-21 18.25.16.excalidraw]]


## important band structures 
![[Kap.5 Semiconductors 2026-02-21 18.26.09.excalidraw]]
![[Kap.5 Semiconductors 2026-02-21 18.26.38.excalidraw]]

## 5.2.2. optical absorbece, relaxation, luminecence
SD become conducting when electrons from the VB get transported into the LB 
Ways of transporting:
- Exitation 
	- thermical 
		- at $T>0K$ the [[Fermi dirac distribution]] gets smeared and some electrons get thermically exited 
	- optically 
		- a photon of the energy that is bigger than $E_G$ gets absorbed by an electrin in the VB -> Absorbtion, this electron takes a free state in the LB ->  Interband Übergang 
	- to note: it is important to remember the conservation laws -> $\Delta k$ is very samll and the transition goes almost vertically in the [[dispersion relation]] 


## [[direct transition]] and [[indirect transition]]
- in an indirect transition very important is the **absorbtion/emission of a photon**  in order to fulfuill the conservation of momentum
- because we need an exptra parrticle, this transition is less likely to happen than just a direct one 
- in indirect SD absorbtion is possible only for $\hbar \omega > E_g$ (photons with the energy bigger than the energy gap)
describtion of the **absorbtion in asemiconductror**:
- [[absorption coefficient]] -> shows how much light looses intensity after going though a medium in x directoion 
![[Kap.5 Semiconductors 2026-02-21 18.32.37.excalidraw]]

for a SD with direct band we have $$\hbar \omega < E_g :D(\hbar \omega ) =0$$
$$\hbar \omega >= E_g : D (\hbar \omega) = \frac{1}{2 \pi} (\frac{2 \mu}{\hbar^2})^{3/2} (\hbar \omega - E_g)^{1/2}$$
	where $\mu = (\frac{1}{m_e^*} + \frac{1}{m_h^*})^{-1}$  being the [[reduced mass]]  
and for the [[absorption coefficient]] will be expected $$\alpha \sim (\mu)^{3/2} \sqrt{\hbar \omega - E_g}$$
### the measurement of absorbtion coefficent 
- for [[indirect transition]] => all possible states in the [[Valenzband]] and [[Leitungsband]] have to be summed up
- for [[direct transition]] => no analytical derivation is possible 
		=> generally we get a quadratic thing $$\alpha \sim (\hbar \omega - \hbar \Omega - E_g)^2$$
	- $\alpha$ increaes in direct SD faster than in indirect and is also generally higher 
- Measurement using **Absoribtion spectrum**  
	- monochromatic light gets send though a probe -> intensity after the proble is analyzed 
	- => wavelength of the exitation light gets measured and from that we can get the absorbtion 

### [[fluoresence]], [[relaxation]] , recombination 
= is the opposite process of absorbtion 
- electron from [[Leitungsband]] takes the free state in the [[Valenzband]] = $e^-$ and $h^+$ [[recombination|recombine]]  (this pair lives only a couple nanoseconds)
- Energy in form of a photon gets released: $\hbar \omega = E_L - E_V$ and is called [[fluoresence]]
- In case that the $e^- h^+$ gets created by a photon of $\hbar \omega > E_g$ then: 
	- charge carriers want to minimize the energy => this why they take the lowest state (highest state of a hole) possible and emmit photons 
![[Pasted image 20260226134359.jpg]]
### [[luminecence]], [[relaxation]], [[recombination]] 
Here we have $e^-$ and $h^+$ **relax** 
1. relaxation happens by **emission** of [[optical phonons]] until the excess energy of a charge carrier is smaller than the energy of theoptical phonon (over the time frame of fs-ps)
2. the rest of the relaxaation goes over [[acoustic phonons]] (time frame of ps)
3. after that [[recombination]] can happen again (time frame of ns) => emitted photon has a smaller energy than the absorbed photon 
Optional: 
- direct recombination can happen before the relaxation -> but very improbable ($k_{rad} = \tau_{rad}^{-1} << k_{relax}$)
![[Pasted image 20260226134450.jpg]]

### [[optical transition]] in [[indirect semiconductors]] 
-> charge carriers do relax in indirect SD, but it happens at really different places 

- [[fluoresence]] has an extra absorbtion/emission of a [[phonon]] , because of conservation of momentum 
	=> this makes [[recombination]] less probable and also slower (time frame of $\mu m -ms$) 
	-> recombination is then [[radiativ]]  and [[non radiativ]] 

#### [[Fallunterstütze Rekombination]]
- Defects in the grid lead to energy states in the middle of the [[energy band gap]] 
	=> electrons/holes can jump there => more relaxation/recombination goes over emission of [[phonon]]s 
#### [[Auger Rekombination]]
- when there are high charge carroer concentrations => many-body processes are more probable 
	=> two holes and two electrons get together 
	=> after $e^- h^+$ recombine, their energy gets transmittet onto a third charge carrier

### [[Recombination rate]] 
![[Recombination rate]]

	
## 5.2.3. [[exiton]]
- optical exitation of an electron into the [[Leitungsband]] makes an **electron - hole** pair => interaction
=> electron and hole interact with eachother with [[Coulomb interacton]] 
- together $e^-$ and $h^+$ are a bound state = **Exziton** (= pair of electron and hole)
	- similar to a $H_2$ atom, but is in a solid body 
	- how much shielding the electron and hole experience depends on the [[dielectric]] neighbourhood 

### Types of Exzitons: 
### [[Wannier Mott exziton]] 
 a lot of dielectric force => a lot of shielding => free exiton 
- anorganic SD 

- exiton binding energy
$$E_B = \frac{e^4}{8 h^2 \epsilon_0^2} \frac{\mu^*}{\epsilon^2} = \frac{R_y}{m_0} \cdot \frac{\mu^*}{\epsilon^2}$$
- exiton bohr radius 
$$a_B = a_H m_0 \cdot \frac{\epsilon}{\mu^*} = 1 - 60nm$$

- binding energy and exziton bohr radius correlate a lot with the [[energy band gap]] of the material
	- for $E_g > 4 eV$ : $a_B \approx a$ -> $\epsilon_r$ no longer useful
	- for $E_g < 1 eV$ : Binding energy is too small for any binding to happen
		- e.g. InSb :$E_B = 0.2 meV = E_{therm} (2.3 K)$ -> for anything above $3K$ the exziton is unimportant 

![[Pasted image 20260226135937.jpg]]



### [[Frenkel exit zone]] 
- small dielectric force => small amount of shielding => very bound electrons 
- organic SD 
![[Pasted image 20260226140035.jpg]]


### Depiction of the exziton in the band schema 
![[Pasted image 20260226141019.jpg]]

$$\vec K = \vec k_e + \vec k_h$$
$$E_n^X = E_h + E_e - \frac{E_B}{n^2} = E_G + \frac{\hbar^2 K^2}{2 \mu} - \frac{E_B}{n^2}$$
- starting at $n = \infty$ => $E_B = 0$ between electron and hole => charge carrier is not bound 
- this is where energies stop being discret/quantised and start being a **Continuum** 

### optical transition in the two particle piscture 
-> particle transition are not just straght up or down, but can also go sideways 
- in order to absorb a photon exziton and light dispersion have to cross => $E_{\gamma}(k) = \hbar k$ 
- the absorbtion spectrum of area above and belov the continuums absorbiotn 
![[Pasted image 20260226141538.jpg]]
	-> under Continuums absorbtion => line. that belongs to the exzition states 

### temperature dependand absorbtion spectrum
-> e.g. GaAS 
- no exziton effects at room temperature 
- exziton absorbtion maximum at lower temperatures => because of the thermal widening of the energy niveaus because of **Exziton phonon coupling** 

### relaxation and recombination of exzitons 
- relaxation mainly through LO ohonon emission 
- if energy to big => more relaxation though emission of acoustic phonons 
- a the crossing of the dispersion relations => recombination possible 
![[Pasted image 20260226142009.jpg]]


## 5.2.4. [[Charge carrier statistics]]
-> in semiconductors electrons can get exited from the [[Valenzband]]into the [[Leitungsband]] though optical or thermal effects 
- number of those charge carrieres ( $e^-$ and $h^+$ ) is important for the characteristics of a semiconductor => density of those carriers 
$$n_L (T) = \frac{1}{V} \int_{E_L}^{\infty} D_L (E) f_{FD} (E) dE$$
$$p_V (T) = \frac{1}{V} \int_{-\infty}^{E_V} D_V (E) (1 - f_{FD}(E) ) dE$$
![[Pasted image 20260226142417.jpg]]

In the neighbrougood of the band edge both [[Valenzband]] and [[Leitungsband]] are approximated to be parabolic $$D_L (E) = \frac{V}{2 \pi^2} (\frac{2 m_L^*}{\hbar^2})^{3/2} \sqrt{E - E_L}$$
$$D_V (E) = \frac{V}{2 \pi^2} ( \frac{ 2 m_V^*}{\hbar^2})^{3/2} \sqrt{E_V - E}$$
Usually band gao us much bigger than the temperature smearung of $f_{FD}$ , which means $E_L - \mu >> 2 k_B T$ => this allows to approximate the [[Fermi dirac distribution]] and from that get simpler values for density, number of carrieres 
$$n_L = 2 (\frac{2m_L^* k_B T}{2 \pi\hbar^2})^{3/2} e^{-\frac{E_L - \mu}{k_BT}} = n_L^{eff} e^{- \frac{E_L - \mu}{k_B T}}$$
$$p_V = 2 (\frac{2m_V^* k_B T}{2 \pi\hbar^2})^{3/2} e^{-\frac{\mu - E_V}{k_BT}} = p_V^{eff} e^{- \frac{\mu - E_V}{k_B T}}$$


### [[chemical potential]] 
- in [[intrinsic]] semiconductor -> all electrons from LB to VB => $n_L = p_V$ 
	=> equation the two values for $n_L$ and $p_V$ from above, we can get the chemical potential $$\mu = E_V + \frac{1}{2} E_g + \frac{3}{4} k_B T ln (\frac{m_V^*}{m_l^*})$$
	-> if $m_V^* = m_l^*$, then chemical potential is in the middle of the band gap 
	- but chemical potential is temperature dependand because usually $m_V^* > m_L^*$ 
Gernerally it is also possible to do everything without the chemical potential 
$$n_L \cdot p_V = 4 (\frac{k_B T}{ 2 \pi\hbar^2})^3 (m_L^* m_V^*)^{3/2} e^{-\frac{E_g}{k_B T}} = n_L^{eff} p_V^{eff} e^{- \frac{E_g}{k_B T}}$$
	-> important:  $n_L \cdot p_V = const$ 
for intrinsic semiconductor, the charge carrier concentration $n_i = n_L = p_V$ $$n_i = \sqrt{n_L p_V} = 2 (\frac{k_B T}{2 \pi\hbar^2})^{3/2} (m_L^* m_V^*)^{3/4} e^{- \frac{E_g}{2 k_B T}}$$
#### a couple intresting examples 
![[Pasted image 20260226151108.jpg]]

at room temperature:
- $E_g (Ge) = 0.67 eV$ 
- $E_g(Si) = 1.12 eV$ 
- $E_g (GaAs) = 1.42 eV$ 
- 