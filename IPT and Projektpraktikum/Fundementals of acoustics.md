starting with simple oscillator, being harmonic, using Hookes law as approx 
initial conditions -> time, displacement, speed and arbitary constants 
energy of vibration 
complec exponential method of solution 
dampend oscillator -> opposite force acting against displacement 
forced oscillations -> has external force 
mechanical ohms in $N \cdot \frac{s}{m}$, the actual equation $$Z = \frac{f}{u}$$
	$f$ is the driving force 
	$u$ resulting speed (at the point where the force is being applied)
decay transient
- when driving force abrubtly stopped -> is important for good microphone/loudspeaker
- it's the best, when there is no "hangover" of sound 

Power relations
- power per one vibration -> average power per time of one vibration
# mass controlled system: 
- frequency quite homogenous over a large interval
Linear combinations of simple harmonic vibration
- linear superposition 
- analysis using Fourier trafo - addition of many harmonic functions 

Fourier Transform 


# Transverse waves on a string 
- displacement through strtching 
- speed of propagation of the disturbance $$c = \sqrt{\frac{T}{\rho}}$$
	- $T$ is tentioni in N 
	- $\rho$ is linear density in kg/m 
- if it's travelling = transverse traveling wave (but they look at the option, where you pinch the string
- phase speed: a specific value propagates 
- dissipative forces distord the wave shape (= dampening, esp in flexible strings) 

reflection at boundary? at the membrane, is that really somehting that is happening ? 

# wavelength $$\lambda = \frac{2 \pi}{k}$$
# phase speed $$c = \lambda f$$
# mechanical impedance
-> is characterisitc only of the string! depends on the tenstion and length per unit $$Z = \frac{f}{u(0,t)}$$ or the infinite case $$Z= \rho c $$

# Forced vibration of string of finite length
-> reflection happens 
Case 1: one side fixed, other driven => standing wave 
Case 2: mass loaded string (mass of string is $m = \rho L$)
- if mass low, then approx to forces, free string 
- if mass big, then approx to fixed string 
Case 3: moving dashpot? sounds like the membrane


# Overtones and harmonics 
- lowest natrual frequency = fundemental 
- higher frequencies = overtone => only there if string is tight 
- 

Strings = transversal
Bar = longitudinal 
stress on a cros sectional area $$stress = \frac{f}{A}$$ -> here Young modulus comes in play 
in this case phase of speed $$c^2 = \frac{Y}{\rho}$$ with $Y$ is young modulus 
$$\frac{f}{A} = - Y \frac{\Delta l}{l}$$Wait, what if my carbon fiber is the case of torsional waves ! = twisting waves 
==sound = longitudinal== 

and now back to the membrane 
# Vibration of a plane surface 
- my membrane is not streched - it has a fixed rim => Bessel functions are the solutions to the wave equation for 2dim planes? 

# Decibels 
$$IL = 10 log (\frac{I}{I_{ref}})$$
# sound pressure level
$$SPL = 20log (\frac{P}{P_{ref}})$$
where $$I = \frac{P^2}{\rho_0 c}$$ $P$ being effective pressure 
Reference for airborne sound 
![[Pasted image 20260510192429.png]]


actual table of values
![[Pasted image 20260510192507.png]]


# Absorbtion and attenutation of sound 
maybe absorbtion by air is important => it changes from length of can 
so can does reverbations and absrobeiton from air 
![[Pasted image 20260510193644.png]]

# Cavities 
pulse/sound travels through waveguid (cavity) at group speed $$c_g= \frac{d \omega}{dk_z}$$
phase speed is still $$c_p = \frac{\omega}{k_z}$$
# pipes, resonators and filters 
we can call my can a pipe, I think 
Resonance frequency of an open ended pipe is $$f_n = \frac{n}{2} \frac{c}{L+ \frac{8}{3}\pi a}$$$a$ is the radius of the pipe!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
the reasonably assume the effectife length of unflanged pipe being $$L_{eff} = L + 0.6a$$resonances are harmonics only if $\lambda >> a$ 
my case: 
using $\lambda = \frac{c}{f}$ and a good middle frequency of $400Hz$ we get $\lambda = 0.85m$ and pipe radius being $0.05m$ => nice, it holds 
cut off frequency being around $7000Hz$ 

# low pass filter 
allows only lower frequencies through 
same for High pas filters 
and band stop filters

# noise 
spectral density $$R = \frac{\Delta I}{\Delta f}$$
where it is the intesity within a frequency interval

# bandwidth 
intervall between two chosen frequencies 

# ISL: intensity spectrum level 
$$ISL = 10 lig (R \cdot \frac{1Hz}{I_{ref}})$$
$$IL = ISL + 10log \omega$$ 
# PSL: pressure spectrum level
$$SPL = PSL +10 log \omega$$
band level = SPL and IL (Intensity level)
# DT: detection threshold over bandwidth
$S$ is signal power 
$N$ is noise power 
=> all inside the same bandwidth $\omega$ 
$$DT = 10 log (\frac{S}{N}) = DT_1 - 10 log \omega$$
where $$DT_1 = 10 log (\frac{S}{\frac{N}{\omega}})$$
is the detection threshold over 1Hz bandwidth 


# Loudness 
the Power rule applies 
![[Pasted image 20260510202515.png]]

$N$ : subjective loudness
$L_N$: loudness level 

General relation $$N = 0.046 \times 10^{\frac{L_N}{30}}$$

# pitch 
determined by frequency, intensity, waveform 

# voice 
ranges from lowest 70Hz (bass) to 1300Hz (sopranos)
- unvoiced sounds => fricative consonants (f,h,s,sh)
- unvoiced stop consonants (k, p, t)

power
- conversational is $10 \mu W$ 

# Reverbations = Time Sabine !!!!
$T$ : reverbation time = time required for the level of sound to drop by 60dB 
$A$: metric sabin uding speed of sound in air 
Sabine reverbation formula $$T = 0.161 \frac{V}{A}$$
average Sabine absorptivity $\overline a$ $$\overline a = \frac{A}{S}$$
$A$ is the total absorbtion 

Considering acoustic losses in volume of air, then $$T = \frac{0.161V}{S \overline a + 4mV}$$

# sound absorption materials 
- porous materials 
- panel absorbers 
- cavity resonators 
- people and furniture 
![[Pasted image 20260510203913.png]]

