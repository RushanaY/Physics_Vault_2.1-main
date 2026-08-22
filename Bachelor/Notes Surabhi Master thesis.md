(here notes from notebook)
some values 
- Evanson [[Microwave cavity (MW)]] 
	$$30W \text{ at } 2.45 GHz$$
	- best starting power is $20$W? (any more power gets "radiated" away)
- flow: $$0.37mln/min$$ 
- pressure :$$1-3 \space mbar$$
- orfice in glass tube $$200 - 400 \mu m $$
- discharge temperature $$-30 - (-10)^{\circ} C$$
- assumed $90\%$ of disassociation 
For plasma: 
- [[Yacora modell]] gives the parameters 
- Plasma depends on temperature and density of electrons (but for relative measurements it's not important)

--------
notes from Thesis itself 

# Hydrogen plasma 
=> what is it and terminology 
using primarily (only) spectrum as data 
main stuff: 
0 temperature 
density of species (atoms or ions)
electron temperature 
electron density 


we have: **low pressure + low temperature plasma in lab (assumed)**
magenta glow -> from Balmer alpha emission = atomic hydrogen
Fulcher alpha = molecular hydrogen population 



# Wire detector himself 
start cooling even before the plasma starts 
 Four wire resistance measurements ?
 background pressure e-4 from [[Pfeiffer MPT200 Pressure Gauge]] 
 hydrogen dissoaciator similar to one from main set up 
 Hydrogen -> Pyrex tube (dosing valve) -> MW cavity (30W, 2.45GHz, 0.37mln/min)  ([[Bronkhost EL-Flow Select Mass Flowmeter]])
 pressure discharge 1-3mbar ([[Pfeiffer PKR251 Compact Full Range gauge]])
Cooling of nozzle
- water cooled 
- TEX element -> **this is one of the things that can be improved, because currently is nothing that works right now** 
- changes beam gas temperature => not too much impact from heat of plasma 
- Peltier element (wow, -20C possible) 
- measured [[HP34401A multimeter]] (in volt)

Recombination release energy per molecule $$2 E_{rec} = 4.6eV = 7.136 \times 10^{-19}J$$
Kinetic energy of hydrogen molecule $$E_{kin} = 1.0291 \times 10^{-20}J$$
Using the [[Four wire method]] to measure resistance 
- Tungsten wire from Goodfellow Advanced Materials 
- 5 to 25 $\mu m$, the longer the better 
- soldered to [[PCB]] 
- [[HP34401A multimeter]] 
- probe current -> **maybe change ?**$$I_{probe} = 1 mA$$
- resolution $$0.5 m \Omega$$
- [[PCB]] only z direction movement, electrically and thermally isolated 
- what is the [[KF40 vacuum flange]]? 
- $5mm$ distance between wire and nozzle 

GOAL: decoupling from all other thermal signal sources (only recombination is left)  


## Atomic hydrogen beam
-> good data to compare to is the thesis from Grinin

....



# Sources of resistance change on wire
positive = heating up of wire 
negative = cooling of wire 

