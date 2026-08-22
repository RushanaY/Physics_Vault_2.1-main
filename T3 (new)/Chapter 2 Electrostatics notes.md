flux and charges stationaries 
stationary fields: $$\frac{\partial \phi}{\partial t} =0, \qquad \frac{\partial \vec A}{\partial t}=0$$
$$\vec E = - \vec \triangledown \phi - \frac{\partial \vec A}{\partial t} = - \vec \triangledown \phi$$
$$\vec B = \vec \triangledown \times \vec A$$ $$\frac{\partial \vec B}{\partial t} =0$$
in electrostatics we have $$\vec J = \vec A =0$$
in magnetostatics we have $$\rho = \phi= 0$$
## 2.1. Poisson equation

 ![[Poisson equation]] 

*the field $\phi(t, \vec x)$ has only one missing [[gauge transformation]]. So taking only the electrostatical case it's possible to define the missing transformation

Show that the solutions to the electrostatical case are unique ("eindeutig")
=> for each [[charge density rho(x)]] there is only one solution of the [[Poisson equation]] 
(the condition being
- $\phi(x) \to 0$ for $|x| \to \infty$ 
- $|x| \space |\phi(x)|<const$ 
- $|x||\triangledown \phi| \to 0$ for $|x| \to \infty$) 


## 2.2. [[point charge]] and [[Greens function]]

taking the simplest case of a point charge with the simplest definition of [[charge density rho(x)]] is good to solve [[electrostatics]] problems 

*what the hell is greens function?*

Defined a partial differential operator $$\hat O G (\vec x, \vec x') = \delta (\vec x - \vec x')$$
-> make inhomogenous DGL


# 2.3. Force and interaction energy
-> energy of charged particle in stationary case (only electrical field )
-> expanding it to two charged particles 
-> case of external field (like through another charged particle => [[coloumb law]])
-> for [[multipol]], quadropol and point charge 
[[energy density]]
[[dipol moment]] 
use the lorentz force 

I guess this is being continued in [[Chapter 3 Dielectrical mediums#3.3. forces and interactioin energy]] 
# 2.4. multipol expantion 
greens function describes the point charge
describing more than one points charge and its potential in total 

# 2.5. Cavities 
-> [[Microwave cavity (MW)]] haha
mirror charges?
different kinds of hollow spaces with electrical fields 
dirchlet, greens, poisson all have some theorems for that 
Neumann problem 

I guess those are all subcases of the big cavity problem and each can be solved by using their own theorem 

