there is homework sheet -> no need to deliver solution, only appear at tutoriums 
```table-of-contents
```


# My physics (me being Thomas Udem)
![[thomad udems physics map]]

## Notes to the whole physics map 
- waves (usually) prevent things from becoming infinetly small *(infinite points would lead to inifine energy densities , like a black holes)* 
- waves sometimes are called quantum and sometimes classical 
- wave + boundary conditions (the thing that creates modes) => results in quantization *(of modes) (i.e. standing waves, which are used in hydrogen atom, fiber optics ...)* with the quantized energy$$\Delta E = \hbar \omega$$
- may ignore wave structure $>>$ $\lambda, L_c$ or $k T >> \hbar \omega$ (not always the case)
- wave => probability for "click (is more of an interpretation, Copenhagen interpretation to be clear) 
- $g^{(1)}$ : **field correlation function (=interference) = "classical" 
	- (describes if two events are correlated to eachother in space or in time, that's unclear)
- $g^{(2)}$ : **intensity correlation function = particle correlation = "quantum"
	- correlations the click at different times , so actually a particular click, not a mean value over all the clicks in a field
- optics: $$1) \overset{\text{no name}} \rightarrow 2) \overset{\text{"field quantization}} \rightarrow3)$$
	- $\lambda \approx \mu m$ => interference observed  $\sim$ 1800 (Young) *(here they mean the de Brogli wavelength of a particle)*
- mechanics $$1) \overset{\text{"quantization}} \rightarrow 2) \overset{\text{"2nd quantization"}} \rightarrow 3)$$
	- $\lambda \approx nm$ => interference observed 1920s 
	- that's the interference of "big objects"


# From Ray optics to wave optics 
## A ray in free space 
![[Lecture 0 2026-10-12 08.59.37.excalidraw]]
$$\begin{pmatrix} r \\ r' \end{pmatrix} = \begin{pmatrix} \text{distance to axis} \\ \text{slope } \frac{dr}{dz} \end{pmatrix}$$
free space transformation" $$r_2 = r_1 + dr_1' \qquad  \qquad r_2' = r_1'$$
$$\begin{pmatrix} r_2 \\ r_2'\end{pmatrix} = \begin{pmatrix} 1 & d \\ 0 & 1 \end{pmatrix} \begin{pmatrix} r_1 \\ r_1'\end{pmatrix}$$
This is called the ABCD matrix: 
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} 1 & d \\0 & 1 \end{pmatrix}$$
and this is the [[ABCD matrix for the free space]]  


## transformation by a thin lens 
![[thin lens case]]

The [[ABCD matrix for thin lenses]] :
$$\begin{pmatrix} r_2 \\ r_2' \end{pmatrix} = \begin{pmatrix} A & B \\C & D \end{pmatrix} \begin{pmatrix} r_1 \\ r_1' \end{pmatrix} \Rightarrow A =1; \space B =0$$

## mirrors 
### flat mirror 
![[flat mirror]]

### curved mirror 
![[curved mirror]]
This is the [[ABCD matrix for a curved mirror]]:
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ - \frac{2}{R} & 1 \end{pmatrix}$$

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
	=> any real valued solution is bound 

#### Stability diagramm:  
$$(\frac{A+D}{2})^2 \leq 1 \Leftrightarrow 0 \leq \frac{A+D+2}{4} \leq 1$$
$$\begin{aligned}
\frac{A+D+2}{4} &= \frac{1}{4} (1 - \frac{d}{f_2} - \frac{d}{f_1} + (1 - \frac{d}{f_2})  (1  -\frac{d}{f_1}) + 2) \\
&= 1 - \frac{d}{2 f_1} - \frac{d}{2 f_2} + \frac{d^2}{1 f_1 f_2} \\
&= (1 - \frac{d}{2f_1})(1 - \frac{d}{2f_2}) \\
&= g_1g_2
\end{aligned}$$
And here we define $$g_i \equiv 1 - \frac{d}{R_i}$$

![[Pasted image 20261016172625.jpg]] 
iterating half round trips; 
![[Pasted image 20261016181701.jpg]]


#### Astigmatism 
it comes from two main sources" 
- Brewester plate ![[Pasted image 20261016181838.jpg]]
- mirror/lens ![[Pasted image 20261016181907.jpg]]
	- saggital: $$f_y = \frac{f}{\cos \theta} \qquad \qquad f_y = (\frac{\sqrt{n^2 - \sin^2 \theta}}{\cos \theta})^{-1} \frac{f}{\cos \theta}$$
	- tangential $$f_x = f \cos \theta \qquad \qquad f_x = (\frac{\sqrt{n^2 - \sin^2 \theta}}{\cos \theta})^{-1} f \cos \theta$$
Just for the understanding of what saggital and tangential (meridional) means:
![[Pasted image 20261021220708.jpg]]


