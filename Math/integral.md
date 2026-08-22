Here we define it though a [[measure]] and a [[step function]] $u$ 
$$\int_X u d \mu = \int_X u(x) d \mu(x)  := \sum_{k=1}^n \alpha_k \mu(A_k)$$
# Properties
1. the connection from the measure to the integral$$\int_X \mathbb{1}_A d \mu = \mu(A)$$
2. $\forall 0 \leq \alpha :\int_X (\alpha u) d \mu = \alpha \int_X u  d \mu$ -> multiplying with a positive coefficient can be out ourside from the integral 
3. Additivity $$\int_X (u + v) d \mu = \int_X u d \mu + \int_X v d \mu$$
4. Integral behaves just like the function when comparing sizes $\forall x \in X: u(x) \leq v(x) \Rightarrow \int_X u d \mu \leq \int_X v d \mu$



# Convergence
- for a monotonically decreasing [[sequence]] of non negative [[step function]]s and all of them have [[points wise convergence]]  to zero with $\forall n \in \mathbb{N}: \int_X f_n d \mu < \infty$, then: $$\lim_{n \to \infty} \int_X f_n d \mu =0$$ ==imagine a function that always falls and on a big scale its area will be very small== ![[integral 2025-12-13 23.53.53.excalidraw]]
- if we have two sequences of non negative step functions with, being monotinically increasing and having the same limit, then the supremums of their integrals are also the same 
- If there is a measurable function in a measure space, then there is a monononically increasing sequence of non negative step functions -> define ==integral of non negative and measurable functions f== $$\int_X f d \mu : = \sup \{ \int_X f_n d \mu :n \in \mathbb{N} \} = \lim_{n \to \infty} \{ \int_X f_n d \mu \} \in [0, \infty]$$
	- ==relation between integral, convergence and a supremum== 
	- Properties -> the usual ones that we know from actually calculating with integrals and are the same as for the [[integral]]