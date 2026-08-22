==good for explaining the results==
==information on the tension on the string==

Fundemantals of acoustics (4th edition) -> sounds like the better book
# chapter 1 
- -> let's see if it is not too simple 


- sound range of a young person is 20Hz - 20.000Hz 
- simple oscillator 
	- mass on a spring with a displacement -> $F = -sx$ being the foroce with $s$ being the spring constant 
		**if intresting, then we can revise how the whole wave equation got derived** 
- dampend oscillator -> we have an extra oppposed force for dampening $F_R = -R_m \overset{\cdot}{x}$ with $R_m$ being the mechanical resistance 
- forced oscillator -> external applied force 
- resonance frequency $\omega_0$ 
- addition of multiple harmonic vibration -> linear superposition by adding the phases 
- using fourier theorem for overlaying harmonic functions $$A_n = \frac{2}{T} \int_0^T f(t) \sin n \omega t dt$$
- **if intrested, then understand what fourier transform and sequence is** 


# chapter 2 

- -> here comes the string, very important chapter , epsecially the modes and the realistic cases 


- case: string and we pinch it 
	- disturbance travels with the velocity of $c = \sqrt{\frac{T}{\rho_L}}$ , where $T$ is tenstion in Newton and $\rho_L$ is the linear density (mass kg per unit of length m)
	- transverese traveling wave 
- **=> definetly not our case, as our waves are longitudinal** 





# chapter 3 
-> longitudinal suff, what is that, s that important, there are stll good boundary conditions 

- now that's our case => is the compression of the string material ![[Acoustics 2025-12-08 13.57.38.excalidraw]]
- notation: positive force = compression, negative force = tension 
- stress on the cross section: $$\text{stress} = \frac{f}{S}$$
	- usually known as the Hooke's law $$\frac{f}{S} = - Y(\frac{\partial \xi}{dx})$$
		- ==Y is **Young modulus** -> shows how elastic the material is and applicable **only on thing bars** 
		- ==phase speed is therefore==$$c^2 = \frac{Y}{\rho}$$
			- *the bigger the Young coefficient and smaller density, the bigger phase speed. Although the question is, if we want the hoght phase speed*
	- case of a bar being fixed at **both ends** 
		- natural mode of vibration $\omega_n = \frac{n \pi c }{L}$ or $f_n = \frac{n/2}{c/L}$  
	- tuning fork = free bar with a bend 






# chapter 4 
-> vibration on surfaces is probably good for the cup part of the telephone 

- two dimensional system = like michrophone, yes, we need that 
- look at the stretched membrane with density $\rho_S$ and membrane tension in Newton per meter $\mathcal{T}$ in two dimentions 
- phase velocity in this case $$c^2 = \frac{\mathcal{T}}{\rho_S}$$
- useful for the wave equation is theHelmholtz equation $$\triangledown^2 \psi + k^2 \psi=0$$
	- solution givesthe modes for **rectangular membrane** -> $$f_{nm} = \frac{\omega_{nm}}{ 2 \pi} = \frac{c}{2} ((\frac{n}{L_x})^2 +  ( \frac{m}{L_z})^2)^{1/2}$$
	- $n \neq m$ is for overtones 
	- solution for **circular membrane**, fixed at the rim -> specifically looks like a cup! 
		- Helmholtz equation is better as the Bessel equation $$\frac{d^2 R}{dr^2} + \frac{1}{r} \frac{dR}{dr} + (k^2 - \frac{m^2}{r^2}) R =0$$
		- solution is $y_{mn} (r, \theta, t) = A_{mn} J_{m} (k_{mn} r) cos (m \theta + \gamma_{mn}) e^{i \omega_{mn} t}$ 
			- natural frequency is $$f_{mn} = \frac{j_{mn}c }{ 2 \pi a}$$where $k_{mn}a = j_{mn}$ -> $j_{mn}$ is a given constant, material spesific? 
	- ==volume displacement amplitude = how much air is displaced bacause of the vibration 
		- =>  ==surface area of the vibrating object $\times$ average displasement amplitude of the surface==
		- this displacement amplitude of the surface it's $\langle \psi \rangle = 0.432A_1$, where A is the amplitude in the centre in the lowest mode 
- upper frequency limit increased, by **increasing the tension** or **decreasing** the **radius of the membrane or the surface density**  
- difference between membrane and thin plate 
	- natural frequencies more spread apart in the plate 
	- displacement near the edges of the plate is smaller => average displacement of the amplitude is smaller (by factor of 1.4 how????) 
	- ==reduced sensetivity in the plate== 




# chapter 5

-> solutions to equations, not sure hoe ioprtant for the practital stuff, but the 5.14 looks funny
- sound level - decibel 
	- in a logarithmic scale the sound in decibles dB $$IL = 10 \log (\frac{I}{I_{ref}})$$
		- with reference intensity $I_{ref}$ and the log in base 10 






- chapter 6 -> aah, refleciton and transmission, damn that is important for the boundary between talking person to air to cup to string 
- chapter 7 -> strange words, maybe read on  that if intersting 
- chapter 8 -> absorbtion is important for the lowering of quality of the sound, maybe skip the part with the water 
- chapter 9 -> chanels? wave guide? sounds like applicable for me 
- chapter 10 -> the question is how much a pipe is a string 
- chapter 11 -> real life application of the voice and how a peron hears 
- chapter 12 -> talks about acousitcs in closed spaces, it is important only if he talks about a cup
- chapter 13 -> noise? very specific, mayeb just a quick stroll worthy 
- chapter 14 -> transduction? is about electrical stuff, but micropphone concept might be nice (although it probably requires electronics)
- chapter 15 -> underwater unimporatnt, skip
- chapter 16 -> non linear stuff is good 
- chapter 17 -> shock wave? is that our case? don't think so 



es wird ein bisschen messy 
er callt es immer, es is so impressive 
das ist was wir basically ausgerechnet haben 

