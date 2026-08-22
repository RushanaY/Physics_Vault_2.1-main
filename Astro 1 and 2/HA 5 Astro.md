1. Cygnys A 
Gegeben:  Abstand  zu uns $D  =224 Mpc$,  Radio Leuchtkraft $L_R \approx 1.3 \times 10^{38} Js^{-1}$, Winkelabstand am Himmel $\theta = 0.038^{\circ}$ 
Wie land muss der Kern der Galaxie mindestens aktuv sein, um eine solche Radioquelle zu verursachen?
Wenn man annimmt dass sich die Jets mit, im besten und schnellsten Fall, mit  Lichtgeschwindigkeit bewegen, dann ist die Mindesdauer der Aktivität die Zeit die die Jets  Jets gebraucht haben, um um den Winkel $\theta$ auf dem Himmel die Strecke hinter sich zu legen. $$t_{min} = \frac{\text{distance from nucleus to the lobe}}{c}$$
![[Astro HA 5 2025-11-17 14.58.48.excalidraw]] 
Der Abstand zwischen dem Ende der Lobe und Kern 
$$J = D \cdot \frac{\theta}{2} = 224 Mpc  \cdot 0,038^{\circ} \cdot \frac{\pi}{180} \cdot \frac{1}{2} = 0,07 pc= 2,3 \times 10^{21} m$$
Daraus die Mindestzeit: 
$$t_{min} = \frac{2,3 \times 10^{21}m}{3 \times 10^8 m/s} = 7,6 \times 10^{12}s \approx 2,4 \times 10^5 yr $$

Wie viel Mateire müsste hier im Laufe jener Zeit in Energie umgesetzt worden sein? Wie viel Masse in Form von Sternen würde hierzu bei einer Effizienz der Kernfustion von $\epsilon = 0.008$ benötigt?
Umsetztung von Energie mit der Annahme, dass die Leuchtkraft die ganze Zeit konstant gewesen ist: $$E = L_R \cdot t_{min} \approx 1,0 \times 10^{51}J$$
Die umgesetzte Mateire ist aus $E= \epsilon mc^2 \Leftrightarrow m = \frac{E}{\epsilon c^2}$ 
Zunächst ohne den Koeffiezent $m = 3.333*10^{42} kg= 1,7*10^{12}$ sonnenmassen?
Mit koeffizient $m=4,16*10^{44}$ 

![[Astro HA 5 2025-11-18 13.11.30.excalidraw]]
![[Astro HA 5 2025-11-18 13.11.47.excalidraw]]


2. Kollistion elliptischer Galaxien
keine Kollistion/keine Reibung => kein Energieverlust durch Wärme 
-> $E_{in} = E_f$ 
-> wir vernachlässigen Masseverlust durch Auswerf von Gas und Staub, kinetische Energie der dunklen Materie 
$$\overline U = -\frac{GM^2}{r_g}$$wobei $r_g = \langle r \rangle$ ist der mittlere Abstand
$$\overline K = \frac{1}{2} M \langle v^2 \rangle$$wobei hier von einer Geschwindigkeitsdispersion gesprochen wird

Mit dem Viraltheorem, wo die Terme der kinetischen und potentiellen Energie eingesetzt werden, bekommt man die Ausdrücke für Geschw. dispersion und Energie $$\langle v^2 \rangle = \frac{GM}{r_g}$$$$E = -\frac{1}{1} M \langle v^2 \rangle = - \frac{GM^2}{2 r_g}$$

Anfangszustand
$R \to \infty \space (E_{orb} =0) \Rightarrow E_i (t =0) = -\frac{1}{2}M_i \langle v^2_i \rangle, E_a (t=0) = -\frac{1}{2} M_a \langle v_a^2 \rangle$
$E_{in} = E_i + E_a = - \frac{1}{2} M_i \langle v_i^2 \rangle (1 + \eta \epsilon)$ (keine Initialgeschwindigkeit der Masse)

Endenergie: $E_f = -\frac{1}{2} M_f \langle v_f^2 \rangle = - \frac{1}{2} (1 + \eta ) M_i \langle v_f^2 \rangle$

Energieerhaltung: $E_f = E_{in} \Rightarrow (1 + \eta )\langle v_f^2 \rangle = (1 + \eta \epsilon) \langle v_i^2 \rangle$ =>$$\frac{\langle v_f^2 \rangle}{\langle v_{in}^2 \rangle} = \frac{1 + \eta \epsilon}{1+\eta}$$

effektiver Radius: $r_g = \frac{GM}{\langle v^2 \rangle}$
=> $r_{g,f} = \frac{GM_f}{\langle v_f^2 \rangle }= \frac{GM_i}{\langle v_i^2 \rangle} \cdot \frac{(1+ \eta)^2}{1 + \eta \epsilon}$ => $$\frac{r_{g,f}}{r_{g,in}} = \frac{(1+ \eta)^2}{1 + \eta \epsilon}$$

Mittlere Dichte: $\overline \rho \propto \frac{M}{r_g^3}$ => $$\frac{\overline \rho_f}{\overline \rho_{in}} = \frac{(1 + \eta \epsilon)^3}{(1 + \eta)^5}$$

Bei Verschmelzung zweier Galaxiesn gleicher Masse $\eta =1$ und $\epsilon =1$ 
-> $\langle v_f^2 \rangle = \langle v_i^2 \rangle$
-> $r_{g,f} = 4 r_{g,i}$
-> $\overline \rho_f = \frac{8}{32} \rho_i = \frac{1}{4} \rho_i$ 

3. M87
- $T =  2 \pi \sqrt{\frac{r^3}{GM}} =8,87 \cdot 10^{16} s = 2,8 \cdot 10^9 yr$ -> mit dem Alter des Universums kann man sehen, dass der Stern etwas 5 Umläufe gemacht hat
- allg. ist Viralsatz gut anwendbar für geschlossene Systeme mit konservativen Kräften (z.B. gravtiativ gebunden); es gilt be "relaxed" Systemen
	- sterne/galaxien haben viele Umläufe gemacht
	- Geschwindingkeitsverteilung ist stabil
	- Grav. pot. ändert sich nicht mehr stark
	- wenn es viele dynamische Zeiten erlebtt hat
-=> bei M87 ist die Umlaufzeit sehr klein, somit kann der  Viralsatz nur eingeschränkt anwendbar 
- $v = \sqrt{\frac{GM}{r}} = 656 km/s$
- aus $\frac{3}{2} kT = \frac{1}{2} mv^2$ => $T= \frac{mv^2}{3k} = 1,73 \cdot 10^7K$ 

Diskussion
im inneren ist gravitation sehr stark und dort entsteht das schwarze Loch. In äußeren Bereichen der Scheibe ist gravitation des Loches schwächer -> nicht so viel Materie kann in das schwarze Loch reinfallen. 
schwarzes Loch und buldge werden zu etwas der gleichen Zeit erzeugt und nehmen in gleichem Maße die Masse an. Sobald das scharze Loch anfängt Jets zu bilden, bläst es den dazu kommenden Gas zur Scheibe, weg. Das kann dazu führen, dass im der Scheibe weniger Gas ist
Das wird auch mit dem AGN Feedback bezeichnet und Scheibe, Halo sind nicht damit verbunden und deshalb nicht beeinflusst. 

Im M87 ist aber beides sehr massenreich, was überraschend. 



Akkretionsscheibe ist sehr hell und kann stärker als die Galaxie leuchten. Beim Reinfallen gibt das Teilchen die Hälfte seiner Masse ab und die Häflte wird in energie umgewandelt. Diese Energie, gemäß dem $E=mc^2$ hat eine Proportionelle Leuchtkraft. Deshalb ist das Zentrum so hell. 

