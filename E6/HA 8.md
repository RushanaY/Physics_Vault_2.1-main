1. scattering process in a fermi surface 
	electronic structure of metalls, electrons in quasi free fas, Drude sommerfeld, no temperatre = all states up to fermi energy used and above none, for T>0 used and not used states on teh surface of the fermi sphere, using the fermi dirac distribution => here scattering possible (pauli lrinciple)
	Assuume $E_F = \mu$ (E_F is fermi energy)
		1. take cube $L=1cm$, el. density $n = 5 \cdot 10^{28} 1/m^3$
		find: number of states inside the fermi sphere using the [[fermi wave number]]
		$$(n = \frac{N}{V} = \frac{k_F^3}{3 \pi^2} \Rightarrow) k_F = (3 \pi^2 n )^{1/3} \approx 1.1 \cdot 10^{10}m^{-1}$$
		number of k states inside the fermi spehre, without the spin: 
			one  k state has the "vcolume" $(2\pi/L)^3$ in the k space : $$N_{k-state} = \frac{V}{(2 \pi)^3} \cdot \frac{4 \pi}{3} k_F^3 = \frac{Vk_F^3}{6 \pi^2}\approx 2.5 \cdot 10^{22}$$
			number of electrons: $$N_{electrons} = 2 \cdot nV = 5 \cdot 10^{28} m^{-3} \cdot 10^{-6} m^3 = 5 \cdot 10^{22}$$we can see that it is exacly twice as many, as there are in k state. The reason for that is, that each k state can take two electrons -> spin up und spin down. The k states we did not consider the spind, where as fro the electron number we do 
		2. take the state $(k_F, 0, 0)$ 
		what is probability that it is taken? why tmeperature doesn't matter? 
			using the equataion from fermi dirac we get the probability  $$f(E) = \frac{1}{e^{\frac{E - \mu}{k_BT}}+1} = \frac{1}{e^0+1} = \frac{1}{2}$$using the state we have $E=E_F$ and $E_F=\mu$ 
			it is independant from temperature as long as $E=\mu$ holds![[HA 8 2025-12-07 10.39.41.excalidraw]]
	3. assume that state occupied
	what is probability that scatterring is not forbidden with $\Delta k = 4 \cdot 10^7 \frac{1}{m}$ 
	the scattering is only allowed, if the end state is empty 
	occupation probability (besetzungswahrscheinlichkeit) of the end state $$f_{end} = f(E_F + \Delta E)$$ with $E(k) = \frac{\hbar^2 k^2}{2m_e}$ 
	and therefore $$\Delta E = E(k_F + \Delta k) - E_F \approx \frac{\hbar^2 k_F}{m_e}\Delta k \approx 0.035eV$$
	for room temperature ($T=300K$) we have $k_BT= 0.026eV$ 
	then we can get the $$\frac{\Delta E}{k_BT} \approx 1.3$$
	from that we calculate the fermi function of the end state $$f_{end} = \frac{1}{e^{1.3} +1} \approx 0.2$$
	the probability that the enstate is empty and the scattering is not forbidden is $P = 1 - f_{end} = 0.2$ => $80\%$  



2. electron desity 
	1. sehr konstant und dann abrubted fallen ab einer bestimmten energie => 2D; Abfall siehr idealisiert aus => sehr kalte Verteilung also $T=10K$ 
	2. gross bei kleinem E, monotomes Fallen und abrubter Fall => ähnlich zu $g_{1D} (E) \propto E^{-1/2}$ => 1D DOS entspricht; genau so idealisiert => $T=10K$
	3. ein Maximum ist sichrtbar => passt zu $g_{3D}(E) \propto \sqrt{E}$ was der 3D DOS entsrpicht; Abfall weicher als bei den anderen => höhere Temperatur $T=3000K$ 
	4. S förmige Region erkennbar, insofern ist es identisch zu b), nur mit weicheren Kurven, welche einer höheren Temperatur entsprechen => $T=3000K$ 



3. fermi energy 
	we use because  $$\mu(T) \approx E_F [1 - \frac{\pi^2}{12} (\frac{k_BT}{E_F})^2]$$der Fehler wegen $\mu \approx E_F$ is dann (we want $\frac{E_F - \mu(T)}{E_F} 0.01$) $$\frac{|E_F-\mu(T)|}{E_F} \approx \frac{\pi^2}{12} (\frac{k_BT}{E_F})^2$$ and with the condition that it has to be less than 1% we have $$\frac{\pi^2}{12} (\frac{k_BT}{E_F})^2 < 0.01 \Rightarrow T_{max} \approx 0.11 \frac{E_F}{k_B}$$ which calculated is $T_{max}\approx 4.0 \times 10^3 K$ 



4. derivation of the fermi dirac statistic 
	 1. $\mu = \frac{\partial F}{\partial N_i}$ ist die Änderung der Anzahl der Fermionen um eine kleine Menge 
		 wie viel extra energie brauch man pro extra  fermion um es in das Niveau zu packen 
		 Im Gleichgewicht ist $\mu$ gleich für alle Niveaus, weil F minimal ist 
	2. Grundidee: wir wollen N teilchen auf D zustaände vertielen, ohne das zwei im gleichen Zustand istzen (nach Pauli Prinzip), was der in der KOmbinatorik üblichen schreibweise entspricht $$\Omega_i = \begin{pmatrix} D_i \\ N_i \end{pmatrix} = \frac{D_i!}{N_i! (D_i - N_i)!}$$
	3. calculate $\frac{\partial S}{\partial N_i}$ 
		total number of configurations $\Omega = \prod_i \Omega_j$ => $S = k_B \ln \Omega = k_B \sum_j \ln \Omega _j$ => $\frac{\partial S}{\partial N_i} = k_B \frac{\partial}{\partial N_i}\ln \Omega$
		using the $\Omega_i$ ffom b) and the Stirling formel we get $$\ln \Omega_i \approx \ln D_i! - \ln N_i! - \ln (D_i - N_i)! = D_i \ln D_i - N_i \ln N_i - (D_i - N_i) \ln (D_i - N_i)$$
		ableiten nach $N_i$ $$\frac{\partial}{\partial N_i} \ln \Omega_i = 0 (\ln N_i +1) - [- \ln (D_i - N_i) -1]=\ln (\frac{D_i - N_i}{N_i})$$
		=> $\frac{\partial S}{\partial N_i} = k_B \ln (\frac{D_i - N_i}{N_i})$ 
	4. we put the equation for the derivative into the given formel, the Besetzungswahrscheinlichkeit ist $f_i = \frac{N_i}{D_i}$ => $\frac{D_i}{N_i} -1 = \frac{1-f_i}{f_i}$ 
		=> $\mu = E_i - k_BT \ln (\frac{1 - f_i}{f_i})$ => $\frac{1-f_i}{f_i} = exp(\frac{E_i - \mu}{k_B T})$ => $$f_i (E) = \frac{1}{\exp (\frac{E_i - \mu}{k_BT})+1}$$
 