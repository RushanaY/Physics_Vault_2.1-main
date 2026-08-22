- assume electrons are free to move, therefore the potential of the nulceus and other electrons is assumed to be a non important pertubation -> $V(\vec r) =0$ 
- a good approximation for [[delocolised electron]]s 


The electrons are inside a periodic grid potential: $$\overset{\sim}{V} (\vec r) = \overset{\sim}{V} (\vec r + \vec R)$$
though fourier and stuff like that we get to the equation that describes Schrodinger equetion in a reciptocal grid for an electron $$(\frac{\hbar^2 k^2}{2m} - E) c_k + \sum_G \overset{\sim}{V}_G c_{k-G} =0$$
-> every wave function is then made up form plane waves, which differ by the [[reciprocal grid|reciprocal]] grid vector $\vec G$ -> $$\sim_{k (\vec r)} = \sum_G c_{k -G} e^{i(\vec k - \vec G)\cdot \vec r}$$
which though some other rewriting and shperteing of the notation we get the [[Bloch function]] $$\psi_k (\vec r)= u_k (\vec r) e^{i \vec k \cdot \vec r}$$

## case of $\overset{\sim}{V}_G$: 
- [[eigenvalue]]s are then $$E_k = \frac{\hbar^2k^2}{2m} = E_{k+G} = \frac{\hbar^2}{2m} | \vec k + \vec G|$$
	- they have the fprm of a parabola, that are shofted to eachtoher by $\vec G$ (the reciprocal grid vector)
	- because they are periodic everything can be fit into oen [[brillouin zone]] ![[quasi free electron 2026-01-03 12.23.57.excalidraw]]

- two possible solutions
	- wave function is a plane wave and moves along the atomic chain -> electron can be scatterd onto any atom
	- wave vector fulfulls the diffraction condition of $\vec k = \vec G$ => then electron has **Bragg reflexion** -> part waves overlay in a constructive interfereance 
		- Bragg reflexion withthe wave number $$k = \pm \frac{g}{2} = \pm \frac{\pi}{a}$$
		- in this case thw two waves from two sides overlay into a stationary wave and there are then two possible solutions for the wave functions -> this results in the modulated charge density
		- to be noted: a **running wave** would have had a constant wave density 

## case $\overset{\sim}{V}_G \neq 0$ 
-> this means that the potential gets descreased in the neighbourhood of the nucleus because of the [[Coloumb potential]]
	-> electron energy is descreased for $\psi_s$ and increased for $\psi_a$ (where $s$ and $a$  are the two possible solutions)
			=> consequence of the fact that part of the wave goes up and the other down leads to an [[energy band gap]] 

[[Kap. 4 electronic properties of metalls]]