there is homework sheet -> no need to deliver solution, only appear at tutoriums 
```table-of-contents
```


# My physics (me being Thomas Udem)
![[thomad udems physics map]]

## Notes to the whole physics map 
- waves (usually) prevent things from becoming infinetly small (infinite points would lead to inifine energy densities , like a black holes) 
- waves sometimes are called quantum and sometimes classical 
- wave + boundary conditions (the thing that creates modes) => resulsts in quantization (of modes) (i.e. standing waves) with the quantized energy$$\Delta E = \hbar \omega$$
- may ignore wave structure $>>$ $\lambda, L_c$ or $k T >> \hbar \omega$ (not always the case)
- wave => probability for "click (is more of an interpretation, Copenhagen interpretation to be clear) 
- $g^{(1)}$ : **field correlation function (=interference) = "classical" 
	- (describes if two events are correlated to eachother in space or in time, that's unclear)
- $g^{(2)}$ : **intensity correlation function = particle correlation = "quantum"
	- correlations the click at different times , so actually a particular click, not a mean value over all the clicks in a field
- optics:  1) -no name-> 2) -"field quantization"-> 3) $$1) \overset{\text{no name}} \rightarrow 2) \overset{\text{"field quantization}} \rightarrow3)$$
	- $\lambda \approx \mu m$ => interference observed  $\sim$ 1800 (Young)
- mechanics $$1) \overset{\text{"quantization}} \rightarrow 2) \overset{\text{"2nd quantization"}} \rightarrow 3)$$
	- $\lambda \approx nm$ => interference observed 1920s 
	- that's the interference of "big objects"


# From Ray optics to wave optics 
## A ray in free space 
![[Lecture 0 2026-10-12 08.59.37.excalidraw]]

## transformation by a thin lens 
![[thin lens case]]


## mirrors 
### flat mirror 
![[flat mirror]]

### curved mirror 
![[curved mirror]]

### multiple components 
![[multiple components]]

#### Resonator or cavity (or farby perot ? stuff)
![[resonator or cavity]]
#### Confined rays (it's beam in the script)
$$\begin{pmatrix} r_{n+1} \\ r_{n_1}'\end{pmatrix}$$
![[solving DEQ for confined ray]]

Two cases:
- $(\frac{A+D}{2})^2 >1$ => $e^{i \phi}$ is real 
	- => $|e^{i \phi}|^2 > 1$ for
		- "$+$" solutions $A+D >0$ 
		-  "$-$" $A+D <0$ 
			- => one of the solution diverges 
- $(\frac{A+D}{2})^2  \leq 1$ => $e^{i \phi}$ is complex 
	- real solution $r_n = \frac{1}{2} (r+o e^{in\phi} + r_o^* e^{-in \phi}) = Re (r_0 e^{in\phi}) = |r_0| \cos ( n\phi + \alpha)$ => cavity is stable (an introduced pertubation does not increase)