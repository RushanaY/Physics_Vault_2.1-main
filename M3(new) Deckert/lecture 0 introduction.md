# Implementation
Last topic of M2 was the Riemann integral and now they continue with the Lebeque integral 
look closer at the boundaries, as they are problematic 
expecaillly the Riemannn one is very bad with limits 
$$\lim \int f(x) dx$$ we want to put the lim inside the integral. this is useful, when going form discrete particles to a continuum 
remember the way for the riemann integrall the x axis was divided in aquidistant partitions, which are then later put to infinetly small. this is not ideal, as it only works for regular functions, that behave properly. for anything that doesn't correpsond to the perfect  and well behaved (smooth enough) function, is then done woth Lebesque integral. 
so the Rieman integral was just roughly : $$\sum_i h_k \cdot (x_k - x_{k+1})$$
what is changed on Lebesque:
- partition the y axis and not x axis as it wsa for Riemann -> $f^{-1} ([y_{k-1}, y_k])$ is then the preimage of the new partition along the y axis 
-  for now it is only done for positive funcitons (ones above the x axis)
- the preimage lives on the y axis and takes slices of the function horizontally 
- meausre $\lambda$

why is measure cool: 
- it doesn not depend on the smoothness of the function, there fore any quastions around the limits are not a porblem 

## problem of assigning capacities of eh contimuum
$$(a,b) \to \lambda ((a,b)) : = b-a$$
this is a definition of the intervall in the measure 
it should be possible to define a measure over any intervall and "any" can just start with the power set 
$$\lambda: \mathcal{P} (\mathbb{R}) \to [0, + \infty]$$some properties:
- translational invariance $$\lambda (A+c) = \lambda(A)$$
- the intervall length remains the same 
- if we overlap many meausres over many sets, then the "length" concept still the same and we don't count the overlap twice 
- Inhalt = capacity (can any capcacity be good for a measure?)
	- example where that is baerly not the case : Vitaly set 
		- this is when the beginning of the intervall is glued to its end
		- the capacity if this set doesn't allow a sensible application of a measure 
		- the solution is the sigma algebera
	
