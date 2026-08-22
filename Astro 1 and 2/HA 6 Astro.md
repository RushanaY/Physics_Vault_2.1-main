1. Aufgabe 
Spektren integreiren, um Verbindung zwischen Gesamtleuchtkraft und Konstanten zu schaffen 
$$L = \int_{V_{min}}^{V_{max}} C \nu^{-1} d \nu$$
mit $\nu \in [10^{10} Hz, 10^{25}]$ 
=> $5 \cdot 10^{39} W = C [\ln (\nu)]^{10^{25}}_{10^{10}}$   <=> $C = 1.45 \times 10^{38}W$ 


Es muss gelten: $\ln \nu >= E_k$ 
$$E_k = 13.6 eV = 2.18 \times 10^{-18}J$$
Berechnete Frequenz, die der Ionisationsenergie entspricht: $$\ln \nu >= E_k \Leftrightarrow \nu_k >= \frac{E_k}{k} = \frac{2.18 \times 10^{-18}J}{6.626 \times 10^{-31}Js} = 3.29 \times 10^{15}s^{-1}$$
Berechnete Photonenzahl: 
$$\overset{\cdot}{N} = \int_{V{min}}^{V_{max}} \frac{L_{\nu}}{k \nu} d \nu = ... = 6.65 \times 10^{55} \text{photonen/sekunde}$$


Radius ist damm $$R_S = \sqrt[3]{\frac{3}{4} \frac{\overset{\cdot}{N}}{\pi \alpha u^2}} = 8 \times 10^{17} m$$



2. Ein extremer Quasar 
	- Article :
		- Scientist as at ESO and VLT have discoverd the fastest growing black hole, that has ever been found. This quasar with the number J0529 -4351 has the mass of 17 billion suns and is consuming the equivalent of one sun a day. The way it is formed is by having a very massive black hole attract matter and form a very hot accretion disk, which is very well visible because of it high luminocity. However this quasar was discoverd using the X shooter spectrograph on ESO's VLT and machine learning models, to sort accurately through all the data. In the further plans this quasar can be used by the interferometer  GRAVITY+, that is designed to measure the mass of back holes and also it can be a target for the planed ELT telescope, which together can allow to explore the early Universe.
	- Calculate AGN
		use equation from the lecture: $$\overset{\cdot}m = \frac{L}{\epsilon c^2} \Leftrightarrow L = \overset{\cdot} m \epsilon c^2 = 2.2 \times 10^{25} \frac{kg}{s} \cdot (3 \cdot 10^8 \frac{m}{s})^2 \cdot \epsilon = 1.8 \times 10^{42} \frac{kg m^2}{s^3} \epsilon = 1.8 \times 10^{41} W$$
	- Calculate  the [[Eddington luminocity]] 
		use the equation from WIki: $$L_{Edd} = \frac{4 \pi GM m_p c}{\sigma{T}} \approx 33.000 \frac{M}{M_{\circ}} L_{\circ} = 33.00 \cdot 17 \times 10^9  \cdot 3.828 \times 10^{26}W = 2.15 \times 10^{41}W = 5.61 \times 10^{14} L_{\circ} =2.15 \times 10^{48} erg/s$$
			$1 \frac{erg}{s} = 1 \times 10^{-7} W$
			Man kann sehen, dass die beiden Werte nich weit von einander liegen. Die Eddington Leuchtkraft ist etwas größer.  

Diskussion
- bei der Überlagerung von Schwarzkörperspektren verschiedenner Temperaturen ist das resultierende Spektrum kein perfekter Schwarzkörper. Er wird breiter, weill hier sowohl heiße als auch kalte Spektren reinfließen. Man nennt dies auch oft das "multi colored temperature blackbody". Das resultierende Spektrum mathematisch ist $$F_{\nu} = \int \omega (T) B_{\nu} (T) dT$$ wo $\omega(T)$ die Fläche/Leistung jeder Temperatur ist. 
	- In der Vorlesung wird der perfekte Fall angesprochen, während es hier eher eine Näherung ist 
- Solche Überlagurengen können vokommen bei
	- Thermiosche Emission der Akkretionsscheibe auch der "big blue bumb" genannt -> eine dünne Scheibne um ein sehr sehr schweres Schwarzes Loch.  Innen ist sehr heiß und kalt außen. Quasi jeder Radius der Scheibe hat eine andere Temperatur . Dies führt zum starken optisch und UV Kontinuum
	- Staubige Torus Struktur um den kern -> Staub wird von dem Kern erhitzt, während die äußeren Schichten dieser Gaswolke die Temperatur verlieren. Dies ist als ein IR Bump sichtbat 
	- Sterne im Bulge -> viele Sterne mit verschiedener Temperatur zusammen sind ein Stellarkokntinuum

- Es ist überraschend, weil solche Schwarzen Löcher nicht erwarted wurden. LIGO ist von der Hälfte dieser MAsse ausgegangen, da diese am often vorkommt und typisch für solche Objekte ist, was bereits in anderen Beobachtungen etabliert wurde. Auch braucht man für solche großen Löcher sehr massive Sterne, die jedoch viel wahrscheinlicher viel schneller ihre Masse verlieren oder als Supernova enden, bevor zum SL zu werden. 
- Dies kann erklärt werden druch
	- SL (schwarzese Loch) entstehut in Umgebung mit niedriger Metallizität -> die massive Sterne verlieren hier nicht so viel Masse und kollabieren wenn sie noch sehr groß sind 
	- Verschmelzung aus zwei kleineren SL, was besonders wahrscheinlich wird, wenn man den Bereich mit dichten Sternhaufen betrachtet. 
	- Spekulation, dass die ersten Sterne im Universum metallarmer gewesen sind
	- größere SL sind aus größerer Entfernung sichtbar und deshalb kann man annehmen, dass LIGO vielleicht einfach mehr von den massiven Objekten misst und die kleineren übersieht. Das ist dann nicht aussagekräftig über die tatsächliche Proportion von den Größen, sondern ist die Empfindlichkeit des Apparats