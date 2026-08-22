# Transport und elektrische Leitfähigkeit 
1. Herleitung 
Metall mit el Field, $\vec F =  \overset{\cdot}{\vec p}$   um zeitliche Änderung des mittleren rezriproken Vektors zu finden $$\frac{\partial <\vec k > }{\partial t}|_{el}$$
solutions: 
$$\hbar \frac{\partial <\vec k>}{\partial t}|_{el} = \frac{\partial <\vec p>}{\partial t} = - e \vec E => \frac{\partial <\vec k > }{\partial t}|_{el} = -\frac{e}{\hbar} \vec E$$
2. warum konstanter Stromfluss, obwohl in der Formel beschelunigung erkennbar
	weil Elektronen streuen -> das relaxiert den mittleren Impuls in Richtung Gleichgewich. Feld getriebener Aufbau der Verschiebung der Fermi Kugel = Relaxation = >konstante Driftgeschwindigkeit => konstanter Strom 

3. el Feld aus =>verschiebung der  Fermi Kugel mit $\delta \vec k \propto e^{-t/\tau}$ $$\frac{\partial <\vec k>}{\partial t}|_{relax} = \frac{d \partial \vec k}{d t} = - \frac{1}{\tau} \partial \vec k$$
4. Gleichgewichtsbedingung fur den Stromfluss -> es ist bei $\partial_t < \vec k> =0$ $$\frac{\partial < \vec K>}{\partial t}|_{el} + \frac{\partial < \vec k>}{\partial t}|_{relax} = 0 \Rightarrow \delta \vec k - \frac{e \tau}{\hbar} \vec E$$
5. Herleitung der Gelichung für den Stromfluss 
	bei freinen Elektronen ist $\vec v = \frac{\hbar \vec k}{m}$, sodass ein Verschiebung der Fermi Kugel um $\delta \vec k$ die mittlere Geschwindigkeit wird sein:$$\vec v_d = \frac{\hbar}{m} \delta 
	\vec k$$
	Stromdichte $$\vec J_{el} = - n e \vec v_d = - ne \frac{\hbar}{m} \delta \vec k = - \frac{ne \hbar}{m} \delta \vec k$$
	ich ersetzte $\delta \vec k = - \frac{e \tau}{\hbar}\vec E$ => $\vec J_{el} = \frac{ne^2\tau}{m} \vec E$ 
	aus der Angabe sehe ich, dass man den Bruch mit $\sigma_{el}$ ersetzten kann und somit auf die Formel kommt 


# Temperaturabh'ngigkeit der elektrischen Leitfähigkeit 
1. aus mittleren Streuzeit ergibt sich mittlere freie Weglänge. Warum Fermi Geschwindigkeit angesetzt? 
	also warum wird nicth Driftgeschwindigketi bentuzt 
	Driftgeschwindigkeit  = kommt wegen der Assymetrie der Besetzung 
	aber zwsichen Stößen bewegt sich Elektron mit mit Fermi Geschwindigkeit -> ist größer und hat mehr einfluss 
2. gegeben ist Länge des Metall Drahtes, Querschnittsfäche udn Elektronendichte, angelegte Spannung und gemessene Stromdichte -> mittlere Weglänge ist:
		Widerstand ist $R = \frac{U}{I} = 0.020 \Omega$
		spezifischer Widerstand : $\rho =R \frac{A}{L} = 4.0 \cdot 10^{-8} \Omega m$ => $\sigma = \frac{1}{\rho} = 2.5 		\cdot S/m$ 
		Aus Drude wir haben $\sigma = \frac{n e^2 \tau}{m}$ => $\tau = \frac{\sigma m }{ne^2}$ und mit $m = m_e$ ich bekomme $\tau \approx 1.77 \cdot 10^{-14} s$ 
		die Fermi geschwindigkeit bei freiem Elektronengas $v_F = \frac{\hbar k_F}{m}$ mit $k_F = (3 \pi^2 n)^{1/3} = 1.14 \cdot 10^{10}m^{-1}$ ist dann $v_F 1.32 \cdot 10^6 m/s$ 
		somit ist die Freie Weglänge $l = v_F \tau = 2.34 \cdot 10^{-8} m$ 
3. ich benutze die Fromeln wie in der b) und mache eine lienare ampassugn $\rho(T) = aT + b$ 
	$\rho_1= 4.00 \cdot 10^{-8} \Omega m$ 
	$\rho_2 = 6.49 \cdot 10^{-8} \Omega m$ 
	$\rho_3 = 9.01 \cdot 10^{-8} \Omega m$ 
	=> $T_0 = - \frac{b}{a} = 220K$
4. lineares Modell nimmat an, dass bei kleinen Temperaturen der Widerstand verschiwndet, obwohl in Realität noch Photonenstreuung und Defekte übrig bleiben 
	bei unreinen Metallen = Legierung gibt es eine Sättigung $\rho (T) = \rho_0 + \rho_{ph} (T)$ 


# Hall Sonde 
Herleitung der Formel zur Berechnung der magnetischen Flussdichte 
aus Gleichgewicht $|\vec F_L| = | \vec F_E|$ <=> $e v_d B = e E_H$ => $E_H = v_d B$ 
Hallspannung über Breite b: $U_H = E_H b = v_d B b$ 
Strom entlang der Strom richtung in dem Querschnitt $A=bd$  : $J = \frac{I}{bd}$ 
über die Ladungsträger $\vec J = - ne \vec v_d$ => $v_d = \frac{J}{ne}$ -> diesen Ausdruck in die Hallspannung einsetzen, wobei das $J$ aus der allgemeinen Stromfluss kommt  => $U_H =  \frac{I}{ned} B$ 
Mit dem gegebenen Hallkoeffizienten aus der Angabe, der den Bruch ersetzt und dann nach der gesuchten magnetischen Flussdichte umstellen : $B = \frac{U_H d}{R_H I}$ 







# are you hungry? want to go mensa? willst du mensa ? mensa?