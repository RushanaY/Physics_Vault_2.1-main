WiFI, bluetooth and other communications inhabit the radio frequency spectrum. It is called the ISM for that reason. This is exaclz around 2.45GHz which is specific for communication 
Looking at WiFi, there is a channel every couple MHz
So the probability to hit a WiFi channel perfeclty is not zero.
EMI (electromagnetic interference) has higher porbability , because it is harder to cut off the low noise. 

Types of interference: 
- co channel interference 
	- many wireless users use the same frequency channel 
	- it can be seen, if you shut up the transmitter of intrest adn tune a spectrum analyzer to the same frequency. I guess you can then see it on the spectrum itself 
- Out of band interference 
	- imporper filtering, non linearity, signal leakadge of wireless systems 
	- a transmitter that radiates in the higher frequency band -> that might be the cavity 
	- measure the harmonics by looking for higher harmonics with spectrum analyzer 
- Adjacent channel interference
	- when transmitter splatters into other frequency bands 
	- happens when transmitter starts or stops -> plasma ingition changes the transmission properties for sure and also happend in a short time 