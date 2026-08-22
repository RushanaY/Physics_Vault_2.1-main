# Galaktisches Zentrum 
1. Berechnung der grosen Halbachse  ![[HA 3 Astro 2025-11-04 10.39.57.excalidraw]]
	Es wird die Distanz vom Peri- und Apizentrum gemessen (an der R.A. Achse abgemessen):
	$r_{peri} = 0.1^"$ and $r_{api}=0.18^"$ 
	grose halbachse berechnen **Wert nicht ganz korrekt und ist zu gross eingeschätzt**: 
	$$a = \frac{r_{api}+r_{peri}}{2} = 0.14^"$$
	Das galaktische Zentrum ist $R_0 = 8000pc$ entfernt. 
	Daraus wird die Formel $a(AU) = a(") \times R_0(pc)$ genutzt, um die grosse Halbachse in AU zu bekommen:$$a(AU) = 0.14" \times 8000pc=1120AU$$
	Dann in parsec: $$a(pc) = \frac{a(AU)}{206256} = \frac{1120}{206256} = 0.005..pc \approx 5 \space \text{kpc}$$

2. Masse des Schwarzen lochs **(korrekte Formel benutzt, Wert aber zu ungenau geschätzt)** 
	Die Formel wird benutzt: $$M = \frac{4 \pi^2 a^3}{GT^2} = \frac{4 \pi^2 \cdot (1120au  \cdot 1.49 \cdot 10^{11}m)^3}{6.67\times10^{-11}m^3kg^{-1}s^{-2} \cdot (3.57 \cdot 10^{8}s)^2}=2.16 \cdot 10^{37}kg=10 \cdot 10^6 M_S$$
	wo $M_S$ die Sonnenmasse ist
	
	Hergeleited aus der Gleichsetzung von Gravitations und Zentripetalkraft, wobei die Geschwindigkeit als $v = \frac{2 \pi r}{T}$ gesetzt wird:  $$F_{grav}=F_{zentripetal}$$ 
	Vergleicht mat den Wert von $M=10 \cdot 10^6 M_S$ mit den, in der Vorlesung, angegebenen Wert von $M=(4.10 \pm 0.03)\times 10^6M_S$ . Man kann erkennen dass die echte Masse kleiner ist , als die berechnete. 
	
3. Geschwindigkeit des Sternes im Perihel 
	Ich nehme die Formel für die spezifische Energie (normale Energie geteilt durch die Massse) $$\epsilon = \frac{1}{2}v^2 + \frac{GM}{r}$$ und nach der Lösung des keplerschen Problems hat man auch die spezifische Energie (Formel aus Wiki): $$\epsilon = - \frac{GM}{2a}$$ Nach dem Gleichsetzen der beiden spezifischen Energien und dem Umstellen nach der Geschwindigkeit: $$v = \sqrt{\frac{2GM}{r}- \frac{GM}{a}}$$Anstatt r kann der Ausruck $r = \frac{a(1-e^2)}{1 + cos \theta}$ aus der Lösung der Bahngleichung und für den Fall des Perihels ist $\theta = 0$, weshalb man es zu $r = a(1 -e^2)$ vereinfachen. $$v = \sqrt{GM (\frac{2(1+e)}{a(1-e^2)}-\frac{1}{a})}=\sqrt{\frac{GM}a{ \frac{1+e}{1-e}}}$$
	Um die Exzentirzität zu berechnen, wird die Formel benutzt: $$e = \frac{r_{apo}-r_{peri}}{r_{apo}+ r_{peri}}=\frac{0.035-0.005}{0.035+0.005}=0.75$$Alle Werte eingesetzt: $$v = 7774 km/s $$
	**Alternativ- Drehimpulserhaltung: $\frac{1}{2}v_a^2 - GM/r_a =\frac{1}{2}v_p^2 - GM/r_p$ mit $r_av_a=r_pv_p$ und daraus umgestellt kommt die Formel $$b_p = \sqrt{GM/4a \frac{1+t}{1-t}}$$  
	4. Umrechnung für echte Umlaufzeit 
		Dadruch ist die echte Masse $$M = \frac{4 \pi^2 a^3}{GT^2} = \frac{4 \pi^2 \cdot (1120au  \cdot 1.49 \cdot 10^{11}m)^3}{6.67\times10^{-11}m^3kg^{-1}s^{-2} \cdot (5.049 \cdot 10^8s)^2} =1 \cdot 10^{37}kg = 5 \cdot 10^6 M_S$$
		Dieser wert ist näher an dem echten Wert
	DIe Umlaufzeit wurde in den vorherigen Berechnungen falsch eingeschätzt. Dies kann daran liegen, dass der Stern und der Beobachter zu einander in Bewegung sind, weshalb die Umlaufzeit kürzer aussieht, als in Relität. Auch kann die Bahnebene des Sternes geneigt sein, was eine visuelle verkürzung der Bahn gibt. Auch wird der Stern durch andere, sehr nahe liegende Sterne im galaktischen Zentrum, beeinflusst,  was die Umlaufbahn beiinflusst. 


# M31
1. 

| parameter   | milky way                     | andromeda                            |
| ----------- | ----------------------------- | ------------------------------------ |
| mass        | $0.7 - 1.5 \cdot 10^{12} M_S$ | $0.8 - 1.2 \cdot 10^{12}M_S$         |
| galaxy type | Balkenspiralgalaxie           | Balkenspiralgalaxie                  |
| diameter    | $100 \space 000 ly$           | $150 \space 000 - 200 \space 000 ly$ |
| sternazahl  | $300 \space Mrd$              | bis zu $1$ Billion                   |
2. Wenn man $\Delta \lambda = \lambda - \lambda_0 = -7 \overset{\circ}{A}$ berechnet, so kann man sehen, dass die Laborwellenlange größer ist als die von Andromeda. Dies zeught von einer **Blauverschiebung** , was bedeutet, dass die Andromeda Galaxie sich auf uns bewegt (was den Literaturwerten aus Wikipedia entspricht)
	Um die Geschwindigkeit zu berechnen, wird der Doppler Effekt genutzt (das Stauchen oder Dehnen einer Welle) mit der Formel für Geschwindigkeit $$v = c (1 - \frac{\lambda_0}{\lambda}) = 3 \cot 10^5 \space km/s (1 - \frac{6563}{6556}) = - 321 \space km/s $$
	Andromeda bewegt sich mit ca. $321 \space km/s$ auf uns

3. Vergleich zu anderen Geschwindigkeiten
	1. Sonnensystem: $30 \space km/s$ Bewegung der Erde um Sonne
	2. innerhalb Milchstrasse: $220-250 \space km/s$ im das Zentrum der Milchstrasse -> verlgeichbarer Wert mit Andromeda geschwindigkeit
	3. innterhalb Galaxiehaufen: $1000-2000 \space km/s$ -> viel schneller
4. Galaxien kollidieren in $$t = \frac{s}{v} = \frac{2.6 \space mio \space ly}{321 \space km/s}= \frac{2.46 \cdot 10^{18}km}{321 \space km/s}=7.38 \cdot 10^{15}s$$In Jahre umgerechnet: $$t = \frac{7.38 \cdot 10^{15}s}{3.15 \cdot 10^7 s/yr}=2.3 \cdot 10^8 yr$$Im Vergleich zum Universum, welches $13.8 Mrd$ Jahre alt ist, kann man sehen, dass es 5 mal so gross ist, wie die Kollisionszeit 

**Alternativ :auch Gravitationsanziehung mit berechnen -> verkürzung um 0.3 Mrd Jahre** $$v(r)=\sqrt{v_0^2 + 2GM (\frac{1}{r} - \frac{1}{r_0})}$$und dann $$t = \int_0^{r_0} \frac{dr}{v(r)}$$

 
# Rotation der Milchstrasse 
Given: a rough modell of the density distribution and the rotation on the inside (inside being the inside $\approx 1 kpc$ ). In the centre, there is a black hole with a $4.1 \times 10^6 M_S$ and all the rest of the mass has the isothermical orifile with $\rho \propto r^{-2}$ 
1. Wir haben/definieren: 
	- $dM = \rho(r) \cdot A \space dr = \rho(r) \cdot 4 \pi r^2 dr$
	- $\rho(r) = \rho_0 r^{-2}$ 
	Die Masse innerhalb des Radius durch Integral berechnet: $$M(r) = M_0 + \int_0^r \rho(r') \cdot 4 \pi r^{2'} dr' = M_0 + 4 \pi \rho_0 \int_0^r dr = 4 \pi \rho_0 r + M_0$$wo $4 \pi \rho_0r =k$ die Konstante ist 
2. Bahngeschwindigkeit im Abstand r wird aus dem Gleichstellen von Gravitationskraft und Zentripetalkarft hergeleitet: $$G \frac{m M(r)}{r^2} = \frac{m v^2}{r} \Rightarrow v(r)=\sqrt{G \frac{M_0 + kr}{r}}$$
3. Um k zu finden, wird die oben hergeleitete Formel genutzt und umgeformt, sodass k gefunden werden kann: $$k = \frac{v^2}{G} - \frac{M_0}{r} = \frac{(110 \cdot 10^3 m/s)^2}{G}-\frac{4.1 \cdot 10^6 \cdot 2 \cdot 10^{30}kg}{2 \cdot 3.08 \cdot 10^{16}m} = 4.81 \cdot 10^{19} \space kg/m \approx 7.40 \cdot 10^4 \space M_S/pc$$
4. ![[HA 3 Astro 2025-11-04 23.40.23.excalidraw]]


# Diskussion
![[HA 3 Astro 2025-11-04 23.47.26.excalidraw]]
![[HA 3 Astro 2025-11-04 23.47.53.excalidraw]]