1. **[[Bragg relation]]** 
Damit es zu einer konstruktiven Interfrenz kommt, muss die resultierende Weg differenz ein  ganzes Vielfaches de Wellenlänge sein -> $\Delta s = n \lambda$
Aus dem Bild kann man die Beziehung für den Winkel herstellen: $\sin \theta = \frac{g}{d}$  
Und $g$ ist die Hälfte des Wegunterschiedes, weshab man statt g auch $g = \frac{1}{2} n \lambda$ ein sezten kann
Daraus kommt die Bragg beziehung $$\sin \theta = \frac{n \lambda}{2d} \Rightarrow n \lambda = 2d \sin \theta$$
2. **Diffraktogramm** 
Die Bragg Beziehung aus 1. und $n=1$  nehmen. Ebenfalls den Abstand aus Wiki für [[Millersche Indizies]] $$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$ 
Es wird in die Bragg Beziehung eingesetzt und umgestellt $$h^2 + k^2 + l^2 = \frac{4 a^2 \sin^2 \theta}{\lambda^2}$$ i) $h^2 + k^2 + l^2 = 1,9 \approx 2$ => $(110)$
ii) $\approx 4$ => (200)
iii)$5,99 \approx 6$ => $(211)$
iv)$8,1 \approx 8$ => $(220)$
v)$10,24 \approx 10$ => $(310)$

[[Structure factor ]]ist definiert als $$F_{hkl} = \sum_{j=1}^N = f_j e^{-2 \pi i (h x_j + ky_j + l z_j)}$$
für eine kubische Einheitszelle: 
um zu prüfen, ob Gitter [[bcc structure (raumzentriert)]]   ist, sieht der Struktur faktor so aus: (N=2 weil 2 Atome, Urpsrung bei (000) und dem zentralen Punkt bei ($\frac{1}{2}\frac{1}{2}\frac{1}{2}$), $f$ ist der gleiche Faktor weil es kubisch ist und an allen Seiten gleich ist) :$$F = f + fe^{- 2\pi (h \frac{1}{2}+ k\frac{1}{2} + l\frac{1}{2})}= f (1 + (e^{-i \pi})^{h+k+l})= f(1+ (-1)^{h+k+l})$$ Sodass bei $F_{hkl}=2f$ bei geraden Exponenten und $F_{hkl}=0$ wenn sie ungerade sind

Dazu passen alle Gitter 


Um zu prüfen, ob es ein [[fcc structure (flächenzentriert)]] ist, gilt für den Strukturfaktor $F_{hkl} = 4f$  falls all gerade oder alle ungerade und $F_{hkl}=0$ in andern Fällen

Dazu passen die Gitter (220)


Das heißt es ist ein **bcc** gitter


3. [[Schottky Defect]] 
Schottky Defekt - kation und anion verlassen Kristall => zwei Leerstellen enstehen ![[HA 4 2025-11-09 21.00.53.excalidraw]]
[[Frenkel defekt]] - Ion geht in die Zwischen gitterlücke => eine Lücke und ein extra Ion im zwischengitter bereich ![[HA 4 2025-11-09 21.01.28.excalidraw]]

Temperaturabhängigkeit von Defekten über ide Minimierung der Gibbst Freien Eenrgie erkärt $$G = H - TS$$ defekt increases entalphie $H= H_0 + n \Delta H_s$ and if there are no defects, then $H=H_0$ 
If $T-0$, then $G = H = H_0 + n \Delta H_S$ and G is minimised, if there are no defects $G= H_0$ 
If temperature increses, then more entropy (because more option to position, instead of the orderd lattice), but 
every defect adds onto the enthalpie by the factor $n \Delta H$, but at the same time decreases G by the factor $TS$, as both the factors increas

$S = k_B ln[\Omega] = k_B ln[(N \space n)]$
But considering it is a schottky defect, every defect actually uses two ions (kation and anion), therefore we twice as many options 

Rewriting Gibbs energy with the terms from b and c: $$G = H_0 + n \Delta H_s + 2 TS k_B ln[(N \space n)]$$
in order to get the minimum of G: $$\frac{dG}{dn} =0 \Rightarrow \Delta H_S - 2 TS \space k_B \space ln \frac{N}{n}$$which rearrranged gives the formular from the question


To get the number of defects: 
$N = \frac{V}{a^3}\cdot 4$ 
because a unit cell is a [[fcc structure (flächenzentriert)]] crystal and has therefore 4 atoms/pairs. 

$\frac{n}{N} = e^{- \frac{\Delta H_S}{2 k_B \space T}}$ => $n = 2,05 \cdot 10^{21}$ für $T=100K$ und $n= 2,7 \cdot 10^{14}$ für $T=900K$ 
