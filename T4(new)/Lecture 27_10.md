# Ideal gas 
most important equations for that: $$PV = NRT$$
with
- $N$ being the number of particles per [[mol]] 
- $R$ is te [[gas constant]]
- $k_B$ is the [[boltzmann constant]]  
$$E(T) = ZRTN$$
with: 
- $Z$ being the freedom degrees 
	- -> $Z = \frac{3}{2}$ for mono atomic particles 
	- -> $Z = \frac{5}{2}$ for diatomic particles 

# 1. law of thermodynamics 
$$\Delta U = \Delta Q + \Delta W$$
with: 
- $U$ being the [[internal energy (TD)]]
- $Q$ the heat
- $W$ the work (is the only thing that can be actually measured)
Both internal energy and heat are depenand on the path

We define the [[Gibbs space]] $$\mathcal{G} = \{X\}$$
it coollects all the possible states $X$ 

## Processes 
Processe can be of different types
### reproducable process 
the endpoint of a process has to lie inside the Gibbs space 
$$\Gamma : X_1 \in \mathcal{G} \to X_2 \in \mathcal{G}$$$$X_{1E} \to X_{2E}$$
One of the parameters of the enrgy function can be held constant : 
- [[isobar]] 
- [[isochor]]
- [[isotherm]] 

## internal energy 
in the notation $E(\overline X) := U$  

We take a system with impermeable walls (no particles can escape).
We look at an [[adiabatic]] system 
### adiabatic process 
$$\Gamma : X_1 \overset{a} \to X_2$$
There are states that are adiabatecly accesible and are denotes with: 
$$X_1 \preceq X_2$$
## quasi stationary process 
-> at any point in time the state is in equillibrium 

## (ir-)reversible 
A process is revesible exacly when there is a path back. There are two subcases: 
- adiabatically reversible -> when surrounding don't change $$X_{1 \mathcal{E}} = X_{2 \mathcal{E}}$$
- reversible -> surroundings change $$X_{1 \mathcal{E}} \neq X_{2 \mathcal{E}}$$
**Every reversible process is quasi stationary, but not the other way round** 

## looking at the piston moving 
![[Lecture 27_10 2026-10-27 20.44.24.excalidraw]]

looking at process $II$ -> is adiabatic
process $I$ and $III$ are not 

![[Lecture 27_10 2026-10-27 20.46.26.excalidraw]]

$$\text{adiabaticly reversible }: X_1 \preceq X_2 \lor X_2 \preceq X_13$$
$$\text{adiabatic} : X_1 \preceq X_2 \land X_2 \preceq X_1 \Rightarrow X_1 \cong X_2$$
$$X_1 \preceq X_2 \land X_2 \npreceq X_1 \Rightarrow X_1 <X_2$$

## Energie Bestimmung 
Reference state $X_0 \to E(X_0)$
$$\Gamma : X_0 \overset{a} \to X$$
$$E(X) = E_0 + W(X_0 \overset{a} \to X)$$
where the only measurable part is the Work

# Heat 
$$Q(X_1 \to X_2) = W(X_1 \cong X_2) - W(X_1 - X_2)$$
