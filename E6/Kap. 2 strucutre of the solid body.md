# 2.1. what is holding the solid body together?
# Thermodynamics 
- [[free energy]] $$F = U - TS$$
- [[Gibbs energy]] $$G = U + pV - TS$$
- in thermodynamical equillibrium -> $F,G$ at minimum (*at constant temperature is important, as the the chemical reaction might go the other way, if temperature high enough)
	- looking at [[entropy]] liquids and gases are more stable than solid bodies (*makes sense, as the bigger the entropy, the smaller F and G both get . Loquids and gasses are much more random and have many more options and possible states*)
### 2.1.2. ![[Van der Waal]]

### 2.1.3. ![[covalent]]

### 2.1.4. ![[metallic connection]]



### internal energy -> holds the atoms together 
- Anziehende Energie 
	- potential energy betweem elektrons and nucleus (= [[Coloumb energy]])
	- kinetic energy :
		- mor space in molecule and going by [[Heisenber pronciple]] the momentum is smaller and therefore also the kinetic energy too
		- in most molecules it is the strongest partner 
	- Austauschenergie (= quantenmechanical effecct because of [[hybratisaton]] $\Delta E = E_{AB} -E_B$)
- Abstossende energie ->  [[Pauli exclustion principle]]




# 2.2. Crystall structures 
perfect crystal is the infinite repetition of identical structures

![[Crystall]]

# 2.2.1.  ![[Bravais grid]]


### [[Wigner Seitz cell]] 
-> it is a special tupe of a [[Elemntarzelle (primitive Gitterzelle)]] 
- has **one grid point in the centre** 




# 2.2.2. Important crystal strucutres 
## [[simple cubic (sc)]]

- we take only 1 atom  -> 8 atoms on the corners of the cube 
- side length is the [[grid constant]] $a$ 
Important idea is the [[Packungsdichte (Atomic packing factor)]] 

## important types 
- ![[bcc structure (raumzentriert)]] 
![[fcc structure (flächenzentriert)]] 
![[hcp]] 


### some intresting types of crystals 
-> [[CsCl]] 
-> [[NaCl]]
-> [[Diamant]]
-> [[Zinkblende]]  
-> [[Wurtzi strucutre]] 
When an element could be both wurtzit and zinkblende, then we call it **==[[Polymorphismus]]==** 

### [[Packungsdichte (Atomic packing factor)]] 
$$\text{Packungsdichte} = \frac{\text{volume of atoms}}{\text{volume of unit cell}}$$




# 2.2.3. [[Millersche Indizies]]

How to make them:
1. mark the 3 Schnittpunkte with the axies 
2. give the results in the units of the grid vector -> $(3,1,2)$ 
3. make inverse -> $(\frac{1}{3}, \frac{1}{1}, \frac{1}{2})$ 
4. take the smallest Vielfaches -> $6 \times (...)$ 
5. finished indicies: $(263)$ 


# 2.3. Methods to analyse the strucures 
possible one: 
- diffraction of photons, neutreons or electrons on the crystal (for example with [[x ray]]s ) 
	->  look at diffraction maxima and minima
Diffratcion densitity is made up from scattering -> real part  and absorbiton -> imaginary one => periodic grid $\rho (\vec r) = \rho (\vec r + \vec R)$ with R being the trnaslation vecotr we know form [[Bravais grid]]
=> using [[fourier sequence]] to analyse the diffratcion 

## 2.3.1  ![[reciprocal grid]] 

### 2.3.2. ![[Bragg relation]] 

## how to determine direction

- in order to describe the scattering, we use the [[reciprocal grid]] 
$$\vec G = h \vec b_1 + k \vec b_2 + l \vec b_3$$
		the grid made up from these vectors is then called the [[brillouin zone]] 


### 2.3.3 Von Laue condition 
- it is used in the [[Laue condition]] bein the assumptionm although in the same way, but a bit worse, we can use the [[Bragg relation]] (here we assume that the particles have wave characteristics -> [[de Brogli wavelength]] can be used) 

It is similar to optics, the way x rays diffract on the grid
-> same energy $$E = \frac{hc}{\lambda}$$
## how to determine intensity 
- when we want not only the directon, but also the **Intensity**, we can use the [[Structure factor]] which is derifed from looking at the amplitude of the scattering  $$F = \int d V \rho(\vec r) exp (- i \Delta \vec k \vec r)$$with $\Delta \vec k \overset{!}{=} \vec G$ 
	- the amplitude for a crystall with $N$ unit cells $$F_G = N \int_{EZ} dV \rho(\vec r) exp(- i \vec G \vec r)$$
	- The measure on how much each atom scatters the rays is the [[Atomfaktor]] (which is relevant if the basis is made up from different atoms)

An easy overview ove rall the ypes of diffrction particles and their energies 

![[Kap. 2 strucutre of the solid body 2025-12-20 13.55.03.excalidraw]]



### 2.3.4. ![[Structure factor]]
### 2.3.5. ![[brillouin zone]]

## 2.3.6. Experiments 
- [[Drehkristall verfahren]] 
- the crystal gets rotated along one axis with certain angles, so that scattering happens 
=> measure the width of a peak, which can tell you something about the [[grid constant]] and the quality of the probe 

-  [[Von Laue Verfahren]] 
- every Netzebenenschar as an according wavelength, that results in scattering 
=> measure the width of the peak, which tells about the variation of the [[grid constant]] and the quality of the probe 

- [[Debye Scherrer Verfahren (Pulververfahren)]] 
- crystalss are randomly oriented -> scattering happens in every case 
=> allows to detec crystal structures, crystal size, Gitterspannung, phase transitions 




# 2.4.1 ![[Defects in crystals]] 
- a crystal should be made up from the periodic connection of lattice and basis, but soemtomes this order gets interrupted 
- basis elements can be missing or shift from their usual place in the grid 




# 2.4.2 [[non crystalline bodies]]
- don't have a orderd structure 
- also called [[amorph]] solid body 
- glas is a good example
	-> has elastisity of an isotrope body
	-> they are formed by rapid coolung of a fluid (= Abschrecken)
	-> metallic glas is harder and hold better against corrosion, but break easily when bended (metall would just bend)



























Thermodynamik - holds solids together
- free energy
- gibbs free energy 
VAn der Waals Edelkristalle

Arten der BIndung:
Kovalente kristalle? - Hybrid?
-> energie davon 
- potential energue (coloumb)
- kinetic
- austauschenergie

Pauli verbot

Metallische Kristalle 
- Ionen und Kationen
- Elektronengas
- schwache BIndung 

Ionische Kristalle 

in natur:
- gemischte bindungstypen



review types of (chemical) connections and look how it is then in rerality in solid state physics   

every type of connection need a certain set of initial conditions 
most typica one is the form of a crystal 
that's why the most basic: CRYSTAL:
- defined over :Kristallstruktur = Gittter + Basis 
	- grid: peropdical, infinite order of points in space 
	- basis: the thing that is at the points = Struktureinheit (it can be a group of atoms. as long as it gets repeated periodacly, we have a grid and therefore a crystal)

Bracais grid:
- mathematical way to describe the crystal?
- infinite grid of space points (basically the most perfect grid possible)
- 3D ha spoints $\vec R = n_1 \vec a_1 + n_2 \vec a_2 + n_3 \vec a_3$ 
- where $\vec a$ die elementar gitterverktoren
- die kleinen vektoren spannen eine primitive gitterezelle/ elementarzelle  (Volumen ganz normal mit "det" berechnet) (das ist die einheit, die man unednlich oft wiederhooen kann)
- primitive Gitterzellen:
	- no overlapping
	- whole space is filled 
	- although there are ones that matter more or less 
	- don't need to have symmetry 
	- haben nur ein Gitterpunkt   


Tutorium:
aaah, nice, less time for the same amount of material and also for less points




oooooooooh, bachelor......
halbleiter, damn i am really copying my dad 
75% aller kreuze ..........

I think she was in my team
And didn't show up on Saturday...
defector

want to confront her? for the party 
Yep
When is the party?

Could you check lsf at some point? I'm still not in the extra QM seminar
Wondering if you still are
\

do you remember when your topic will be? I will be there anyways 

hintunen))))))))))
it was intentonal! 


Angabe
PLQY photo lymenecence quantum  y... (efficiency of absorbing and emitting of photons)


i think we will leave earlier again
i will go again to the stufcafe 
although i am not sure if i am feeling the period or if i am sick because of this freaking weqther
Screw the weather!
Can I come with you to the cafe?
sure, no problem. but i thought you want to go home
I mainly just don't want to spend more time at uni, but food is nice, aaah
