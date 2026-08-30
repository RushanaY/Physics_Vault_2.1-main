```table-of-contents
```

<mark style="background: #FFB86CA6;">ToDo/to look up </mark>
<mark style="background: #ADCCFFA6;">my own comments</mark> 

hydrogen -> make experiments to prove fundamental constants from QED 
-> measure transition frequency (energy)
<mark style="background: #FFB86CA6;">**go to E4 script form bloch to remember the terms**</mark>
-> important constants is [[Rydeberg constant]] and [[proton radius]] (theses are fundemental and are calculated precisely in QED)
1S-3S transition 


for good measurement of the transition we need stable hydrogen flow => need a way to quantify the population of atomic hydrogen 
before: only plasma fluorescence - Balmer and Fulcher lines indicative of atomic hydrogen percentage 
addition surhabi: Calorimetric Wire Detector (near the place where the actual measurement occurs) 

Detector: 
-  thin tungsten wire 
- temperature change is the sign of atomic hydrogen 

Goal of thesis: FIND atomic signal (she doesn't say that there is one, so I can argue even further on what the resistance jump might be)
<mark style="background: #ADCCFFA6;">so my results are only good and indicative of atomic hydrogen, if they are backed up by Malte's spectroscopy data
me and Malte </mark>




# Motivation: Determine fundamental constants 
- hydrogen atom = 2 level system 
- spectroscopy data from hydrogen helps develop quantum mechanics
## History
- Angstrom (just mentioned,<mark style="background: #FFB86CA6;"> what did he actually do for the hydrogen?</mark>)
- Balmer -> formular for discrete transitions
- Balmer's formulars improved by Rydberg $$\frac{1}{\lambda} = R_{\infty} ( \frac{1}{n_1^2} - \frac{1}{n_2^2})$$
- Bohr -> explains experiments with theory (structure of atom) -> Quantization
	- coulombic interactions
	- stable orbits 
	- discrete radii
	- angular momentum 
- Bohr's quantization-> Schrodinger's matter wave theory 
	- Balmer's equations with principle quantum number $n$ + angular momentum $l$ and $m$ 
- Dirac -> electron spin orbit coupling ->  fine structure 
- Lamb Shift shift + hyper fine structure (<mark style="background: #FFB86CA6;">by whom?</mark>) -> energy levels (1.2 equation) of Quantum electrodynamics => cool picture with the energy levels and the energy level splitting (from Schrodinger to hyper fine structure)
		<mark style="background: #FFB86CA6;">look up the simple theory from Bloch just for the general understanding and the big picture</mark>

### modern development and link to MPQ lab - proton radius puzzle
- measure 2 transitions in atomic hydrogen => Rydberg constant and proton charge radius 
	- 1S-2S  -> best known transition frequency
- a third transition -> test QED 
- compare the radius from different transitions (muonic hydrogen, 1S-3S , 2S-6P,2S-4P and so on) = **proton radius puzzle** 
		- -> GOAL: get as close as possible to the muonic value, as it's one with the smallest uncertainty (<mark style="background: #FFB86CA6;">why? is that even comparable? do they want to get closer to that value? LKB and CODATA 2014 are miles away from that</mark>)
- <mark style="background: #FFB86CA6;">what is sigma in the uncertainty way?</mark>
- latest update: 2S-6P transition => solves puzzle and proves QED again 
#### improvement by 1S-3S: 
- test out ways to make a new measurement even more precise 

# 1S-3S at MPQ
## frequency comb spectroscopy and its benefits 
- before: limited by frequency reference system (<mark style="background: #FFB86CA6;">what is that?</mark>) -> fixed by frequency comb (conversion from optical to radio frequencies) (<mark style="background: #FFB86CA6;">and now in more fundamental terms?</mark>)
- <mark style="background: #ADCCFFA6;"> in simple terms: a way to very precisely calibrate a frequency </mark>
- <mark style="background: #ADCCFFA6;">IMPORTANT: mention Hansches Nobel prize </mark>
- usage:
	- reference the final measurement 
	- drive transition 
- need two photon transition ($205nm$), because in normal way it is forbidden (<mark style="background: #FFB86CA6;">remember the Hunds rules of transition! </mark>)
- use all pairs of comb lines whose frequencies sum to the 1S-3S transition (<mark style="background: #FFB86CA6;">same, what does that mean?)</mark>
- instead of CW laser use the two photon frequency comb excitation (results in the same excitation rate)
- same AC start shift (it depends on power and not peak power of pulses)
- transition linewidth - dependant on comb modes and not really the spectral envelope (<mark style="background: #FFB86CA6;">what is the significanse of this?</mark>)
- higher peak powers are good? -> more efficient nonlinear frequency conversion -> more power at deep UV wavelengths 
- two counter propagating photons for excitation -> Doppler shift is here suppressed (<mark style="background: #FFB86CA6;">I need this in simpler and more fundamental words</mark>) => signal is doppler free 
- specific repetition rate of comb => all available transitions are inside $f_{rep}/2$ interval (<mark style="background: #FFB86CA6;">I don't understand this either</mark>)
### Laser system in our specific set up 
<mark style="background: #ADCCFFA6;">
-> this is the picture we can take directly from Derya or Alexei 
</mark>
### Spectroscopy Chamber 
<mark style="background: #ADCCFFA6;">-> ask for another picture of the main set up chamber from Charlie 
</mark>
<mark style="background: #FFB86CA6;">stuff to look up, the rest is just retelling. not much can change here :
- sigma polarisation 
- pulse in a laser 
- faraday cage</mark> 

- <mark style="background: #FFB86CA6;">PCV: pulse collision volume </mark>

- atomic hydrogen from microwave plasma discharge -> Teflon tube -> nozzle 
- laser + discharge => 1S-3S transition -> fluorescence of 3S-2P decay (Balmer alpha, 656nm goes to PMT) -> decay 2P-1S (Lyman alpha, 121nm)
- PMT gets doppler free signal <mark style="background: #FFB86CA6;">-> that is debated ? what is a chirped laser? </mark>
- doppler broadened signal measured on the other side of cryogenic nozzle (<mark style="background: #FFB86CA6;">I don't understand the set up here</mark>)
- <mark style="background: #FFB86CA6;">what? the transition is actually 1S-3D ???? </mark>


### ways to characterise the atomic hydrogen beam 
<mark style="background: #ADCCFFA6;">
-> know for sure that there is always a lot of atomic hydrogen</mark>
<mark style="background: #ADCCFFA6;">this is probably also the main topic of Grinin paper </mark> -> so it is better so summarize myself , but here are the main points 
- RGA Residual Gas Analyser (comparing flux with and without plasma) 
	- observe atomic hydrogen =? unreliable signal, overestimation due to the way the RGA works 
	- observe reduction of molecular hydrogen => 5-10% drop = **5% degree of dissociation** 
	- Problem:  RGA too far from beam => underestimation of atomic hydrogen 
- compare temperature dependance of measured count rates on resonance with Monte Carlo <mark style="background: #FFB86CA6;">(assuming initial 100% dissociation) (I need chat GPT to explain this to me)</mark>
- -> that seems to have too much unknown interaction, like between temperature, recombination coefficient of atomic hydrogen on copper, Teflon 

#### Improvements
- use Optical Emission Spectroscopy
- use Calorimetric Wire Detector in the direct path of the beam


# Optical Emission Spectroscopy
<mark style="background: #ADCCFFA6;">
this will be really just a broad overview to know the basic key words </mark>
- measure the produced atomic hydrogen population 
- plasma emission <=> species populations 
- specifically Balmer and Fulcher -> their proportion 
## Set up 
- Microwave cavity! <mark style="background: #FFB86CA6;">how the hell does it work </mark>
- here she describes all the technical data 
	- Pyrex discharge tube -> <mark style="background: #ADCCFFA6;">did we change it?</mark>
	- Evenson microwave cavity -> <mark style="background: #ADCCFFA6;">we changed that </mark>
	- Microwave power 30 W of 2.45GHz 
	- discharge 0.37mln/min
	- 1-3 mbar pressure inside discharge tube -> <mark style="background: #ADCCFFA6;">with the factor for hydrogen it's actually closer to 2-6 mbar</mark>
	- goal: less than 1% of power reflected -> <mark style="background: #FFB86CA6;">is that the case? we should calculate to be sure</mark>
	- 200-400 $\mu m$ orfice in the glass tube (needed to build up the pressure to sustain plasma)
	- tube cooled with air, that is cooled with liquid nitrogen -> assume that temperature of discharge tube is the same as the outgoing air <mark style="background: #FFB86CA6;">(how does thermalisation happen? how many collisions does it take?)</mark> -> <mark style="background: #ADCCFFA6;">also the temperature sensor was changed in position a bit, to better stick through the beam of air</mark> 
		- cooled -30 to -10 C <mark style="background: #FFB86CA6;">(probably I should do more measurements with better cooled nozzle or only take the data with well cooled nozzle)</mark>
- then she describes how to operate the set up -> maybe I can use my lab book notes \

### hydrogen plasma 
#### important variables 
- $T_e$ electron temperature 
- $n_e$ electron density
- low temperatrue, low pressure (0.001-10mbar in the plasma region)
- assume ion density $n_i$ to be the same as $n_e$  
- assume $n_i = n_e << n_n$ with $n_n$ the neutral particles 
- due to that $T_n \approx T_i << T_e$ temperatrue  
- mean energy of electrons in plasma is lower than ionisation threshilda of netrual species 

#### optical emission 
- bright magenta = Balmer alpha emission  and comes from atomic hydrogen
- Fulcher band = molecular hydrogen 
	- come from vibrational and rotational transitions (<mark style="background: #FFB86CA6;">what??</mark>)

### Fulcher band 
<mark style="background: #FFB86CA6;">-> understanding only after reading Bloch script </mark>
<mark style="background: #ADCCFFA6;">same for generally plasma, although there is probably no deep understanding is needed yet </mark>







# Wire detector , yay
