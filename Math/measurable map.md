map goes between sets, where both of them have an algebra to them 
If the preimage is measurable, then the function itself is too. This allows to prove that the composition of two m. maps is also measurable 

For testing purpuses a [[characteristic function]] is used 


- if the map is pointwise convergent, then it is measurable $$f= \lim_{n \to \infty} f_n$$
- For a $(X, \mathcal{A})$ being a [[measurable space]], $f: X \to Y$ a measurable map, then: 
	- the following expressions are also measurable (functions are a sequence) $$\sup_{n \in \mathbb{N}} f_n (x)$$$$\limsup_{n \in \mathbb{N}} f_n (x)$$$$\inf_{n \in \mathbb{N}}f_n(x)$$$$\liminf_{n \in \mathbb{N}}f_n(x)$$
			Proof: take the specific definition of the [[supremum]] and [[infimum]] and this is the properties by which we choose the sets into our algebra. So it is enough to show that that definition holds for all three properties of the [[sigma algebra]]. 
	- both [[positive part]] and [[negative part]] are also measurable 
		- $f_+ (x) := \max \{0, f(x)\}$
		- $f_- (x) := \max \{0, -f(x)\}$
	- the function is an $\mathcal{A}$- [[step function]] 
		- if $f(X)$ is a [[finite]] set 
		- if there are pairwise different $\alpha_i$ and [[disjunction|disjunct]] sets $A_i$ so that holds: $$f = \sum_{k=1}^n \alpha_k \mathbb{1}_{A_k}$$