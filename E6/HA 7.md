1. Umklappsteruung 
	Gegeben: two photons, cubic lattice with grid constant $a = 0.25 nm$,one photon - [001] direction, with wave vector $|\vec k| = 1.15 \times 10^8 cm^{-1}$ , the other photon - [011] direction 
	1. claculate the wave vector 
		wave vector of photon 1: $\vec k_1 = (0,0,k_1) = (0,0,1.15 \times 10^8) cm^{-1}$
		wave vector of photon 2: direction vector $\hat e_{[011]}=\frac{1}{\sqrt{0^2 + 1^2 + 1^2}}(0,1,1) = \frac{1}{\sqrt{2}} (0,1,1)$ => $\vec k_2 = k_2 \hat e_{[011]} = (0, \frac{k_2}{\sqrt{2}}, \frac{k_2}{\sqrt{2}}) = (0, 4.07 \times 10^7, 4.07 \times 10^7)cm^{-1}$ 
		their sum is then $\vec k_{sum} = \vec k_1 + \vec k_2 = (0, 4.07 \times 10^7, 1.56 \times 10^8) cm^{-1}$ 
		a Brillouinzone has the Randbedingung for all sides $|k_x|, |k_y|, |k_z| \leq \frac{\pi}{a}$ => our summed vector is not inside the zone 
		Better solution with the Quasiimpuls erhaltung we calculate the vector though $\vec k_{res} = \vec k_1 + \vec k_2 - \frac{2 \pi}{a} (0,0, \frac{2 \pi}{a})$ where the last part is a reziproker Gittervektor => $k_z' = k_z - \frac{2 \pi}{a} \approx 1.56 \times 10^8 - 2.51 \times 10^8 \approx - 9.57  \times 10^7 cm^{-1}$ 
		=> $\vec k_{res} = (0, 4.07 \times 10^7 , - 9.57 \times 10^7)cm^{-1}$  
	2. case that the second photon is [010] 
		$\vec k_2' = (0,k_2,0) = (0,0.575 \times 10^8, 0) cm^{-1}$  => $\vec k_{sum} = \vec k_1 + \vec k_2' = (0, 0.575 \times 10^8, 1.15 \times 10^8) cm^{-1}$  
		Die kombination zweier orthogonaler Phononen in jedem Gitter ist **nicht** immer in der ersten Brillouizone. Ob die Summe der Wellenvektoren  in der Zone hängt von der Form und Orientierung der Yone im k Raum ab und auch von den Beträgen der Vektoren
		es kann passieren, dass die Vektoren seperat in den Zonen sind, aber deren Summe nicht 

2. Miller indicies 
	1. (100) a plane in the cube , {100} miller inidzies family of planes that are equivalent because of symmetry, [100] family of directions like negative symmetry planes 
	2. (101), (002), ((110), (112)  
	3. [[Wigner Seitz cell]]
		1. ![[HA 7 2025-11-30 17.12.47.excalidraw]]
		das Vorgehen: ![[HA 7 2025-11-30 20.25.16.excalidraw]]
		![[HA 7 2025-11-30 20.56.35.excalidraw]]
		2. Brillouzone ![[HA 7 2025-11-30 20.15.25.excalidraw]]
		3. surface area is then $\frac{4 \pi}{a^2}$ because the area is always the same (can be seen from the first to the second zone )

3. Phononen in the Debye modells 
	1. calculate the number of atoms in a chain $N = \int_0^{\omega_0} D(\omega) d \omega = w_0 D = 1.01 \times 10^9$ atoms => Gitterabstand $a = \frac{L}{N} \approx 2.98 \times 10^{10}m = 2.98 \overset{\circ}{A}$ 
	2. die gegebene Formel umstellen" $K = m  (\frac{v_s}{a})^2 = 49.8 \times 10^{-3} kgs^{-1}$
	3. Innere Energie $$u = \frac{1}{\pi v_S}$$Substitution mit $x = \beta \hbar \omega = \frac{\hbar \omega}{k_B T} \Rightarrow \omega = \frac{k_B Tx}{\hbar}$ so that ableiten of both sides with x  $d \omega = \frac{k_B T}{\hbar}dx$ , mit den oberen Grenze von $x_D = 64$ $$u = \frac{1}{\pi v_S} \frac{k_B^2 T^2}{ \hbar} \int_0^{64} dx \frac{x}{e^x -1}$$mit dem Hinweis für das Integral resultiert $$u = \frac{1}{\pi v_S} \frac{k_B^2}{\hbar} \cdot 1.64$$alle Werte reintun $u = 1.18 \times^{-15} Jm^{-1}$ 