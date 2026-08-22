![[explanaition of the analysis 2026-01-05 12.27.07.excalidraw]]


# points of imporvement 
for long distance calls -> thin string is better -> ==bought 1 mm string now => will take a while to arrive== (so we need to do the calculations as if we already had it and then prove it last minute when the string is there)
Just in case I can just prove the point using the comparison of thick, thin and maybe wool string -> then later extend the theory onto the very thin and very unelastic string 


## membrane
https://www.thebangaloredrumshop.com/products/accessories/en-0114-ba~remo-encore-coated-14-batter-drum-head -> better than just metall
make certain modes on the big membrane! discuss at least the beenfit of different options 
-> i have done one hole with two strings
-> two holes with two strings too 

also option of group call
- big membrane with multiple strings going out -> alrady done and measured 
- bridge manifold -> still question how is that better 
- ==group call by having knots along the string line== 

## cans themselves
-  listener can
	- make a ==dampening ring== to decrease the leacadge of sound 
	- inverse funnel? maybe make it remouvable so it can be interchanged from speaker to listener and the other way round 
- ==speaker can -> flared upper part to better give out the sound==, a way to decrease the leacadge of air vibrations 
	- test the ==funnel== and the smaller ==cylinder 

#### ring to reduce enegy loss
-> cloth? 
-> I have foam! just use that 

what matters is the sound pressure onto the membrane! can just holds it
![[explanaition of the analysis 2026-01-05 14.13.10.excalidraw]]

->  won't it give more echo? 


Resonance of the can itself? 
- air cavity of the can


==make length varuable== 
# calculations 
Cross section for 
- thick :$A_{tk} = 5mm^2$
- thin: $A_{tn} = 2mm^2$

velocity of the transmitting of the transversal wave at force of $5N$:
- thick: $v_{tk} = 100 m/s$
- thin: $v_{tn} = 160m/s$

=> thin string acts just as if we had  more force pulling. we can either make string thinner or make the force stronger 



# explanaitions 
## wave movement  
the analysis is in [[analysis results and thoughts]] 

==how does sound get from one can to another?==
sound carrierd by transversal and a but by lingitudinal waves 
![[explanaition of the analysis 2026-01-04 23.56.51.excalidraw]]
tranversal
- string moves side to side => more visible in streched strings 
- the motion of the tranversal waves is mainly given by the movement of the membrane 
- g![[explanaition of the analysis 2026-01-04 22.40.46.excalidraw]]
- the idea is that small misalignements lead to the string to wiggle vertically too -> that's how the string wiggels too 
- this is why it is good to strech the string -> then the wave and therefore the sound can actually travel and not get lost 
- also the receiving membrane then moves because the force from the string 
- the velocoty is then (from wiki https://en.wikipedia.org/wiki/String_vibration) $$\nu = \sqrt{\frac{T}{\mu}}$$ with T being the tention and $\mu$ mass per unit (seen in thickness)
- tranversal modes? 
	- at discrete frequencies  also from wiki https://en.wikipedia.org/wiki/String_vibration $$f_n = \frac{n}{2L}\nu$$

longitudinal:
- the actual stretching and compressing -> which is probably less of a thing in the dyneema 
- with the speed $$\nu = \sqrt{\frac{E}{\rho}}$$
- they travel faster? but are not as good at transfering sounds => a lot of loss of energy 
-


==force==
the modes/overtones are then $$f_n = \frac{n}{2L}\sqrt{\frac{T}{\mu}}$$
increase in tention leads to increase of frequency -> this checks out as the thiner string and the one with more weights better transmitt the higher range 
making the string longer should by this equation decrease the frequency -> I probably compensated it by having more force 


==each length has an according tension== => should be calculated 


##  membrane
-> knot symmetric in the centre -> most energy transfer 
modes on circular membrane http://hyperphysics.phy-astr.gsu.edu/hbase/Music/cirmem.html
apparently modes and frequencies: $$f_{01} = \frac{1}{a} \sqrt{\frac{T}{\mu}}$$where $a$ is the membrane radius and $\mu$ is also the thickness somewhat 
we can see that bigger radius allows smaller frequencies -> maybe good, because voice is mainly is in the lower ranges. better bigger than smaller, so it can collect more energy 
for test values of 5cm radius, 5 N force and 3.8 g/m => 725Hz roughlt, which is good middle 
also bigger membrane has bigger modes -> increase of uncertaintly  if the good place got hit 


# impedance 
-> http://spiff.rit.edu/classes/phys283/lectures/impedance/impedance.html










# measured values 
- RMS (root mean square) level = how loud the value is 
	- how well the whole systems works 
	- $$RMS = \sqrt{\frac{1}{n} \sum_{i} x_i^2}$$
	- maybe it is good to take only the hearing range -> that's why I have mid and high range 
- test if buzzing occurc -> shows if there are any slipping components, 
	- crest factor - extremeness of peaks $$crest \space factor = \frac{x_{peak}}{x_{rms}}$$maybe show how force and the ring help
- loss of energy
	-  that is what I did comparing the sound to the clean slate 
- magnitude frequency 
	- needs chirp((((
	- apparently good for resonance and cavities
- spectral cetroid = brighness 
	- tension, friction visible 
- Q factor $$Q = \frac{f_0}{\Delta f}$$
- decay constant of time -> maybe good to test on membrane and strings for comparison $$A (t) = A_0 e^{-t/ \tau}$$
- decay with length $$A (L ) = A_0 e^{\alpha L}$$ 