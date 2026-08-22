We have a [[measurable space]] and we define the **measure** $$\mu: \mathcal{A} \to [0, \infty]$$
==it is a way to determine the "volume" of the set. It takes in an elements of the algebra and gives a positive number -> volume is basically the [[integral]]
It is important, that the== [[range]] is always the intervall, while the starting set can be anything== 
# Properties:
- $\mu (\emptyset) = 0$ - volume of empty set is zero
- all measures added up makes the whole set again = [[sigma additivity]]$$\mu (\bigcup_{n \in \mathbb{N}} A_n) = \sum_{n \in \mathbb{N}} \mu (A_n)$$
- paired with a [[measurable space]] we get the [[measure space]] $(X, \mathcal{A}, \mu)$ 

- for $A, B \in \mathcal{A}$ 
	- $\mu (A \cup B) + \mu(A \cap B) = \mu (A) + \mu (B)$ 
	- $A \subseteq B \Rightarrow \mu(A) \leq \mu (B)$ 
	- $A \subseteq B, \mu (B) < \infty \Rightarrow \mu(B/A) = \mu(B) - \mu(A)$ 
	- [[sigma subadditivity]] $$\mu (\bigcup_{n \in \mathbb{N}} A_n) \leq \sum_{n=1}^{\infty} \mu  (A_n)$$

- Equalities: for a [[measurable space]], a [[generator]] $\mathcal{E} \subseteq \mathcal{P}(X)$ of $\mathcal{A}$ and a [[sequence]] $(E_n)_{n \in \mathbb{N}}$ in $\mathcal{E}$ with their union being in $X$  we have two measures $\mu_a : \mathcal{A} \to [0, \infty]$ and $\mu_2: \mathcal{A} \to [0, \infty]$  :
	- $\forall A \in \mathcal{E}: \mu_1 (A) = \mu_2 (A)$ 
	- $\forall n \in \mathbb{N}: \mu_1 (E_n) = \mu_2(E_n) < \infty$ 
	- ==basically this ensures that our volumes is the same in the same definitions and also that the seperate parts are finite and sensible== 

# types of measures
- if $\mu(X) =1$: 
	- $\mu$ is a [[probabilty measure]]
	- $(X, \mathcal{A}, \mu)$ the [[probability space]]
- if $\mu (X) < \infty$ :
	- $\mu$ is a [[finite measure]] 
- [[sigma finite measure]] if there is a finite sequence $(A_n)_{n \in \mathbb{N}}$  in the [[sigma algebra]] $\mathcal{A}$ with $A_1 \subseteq A_2 \subseteq ...$ we have $$\forall k \in \mathbb{N}: X = \bigcup_{n \in \mathbb{N}} A_n , \space \mu(A_k) < \infty$$
- there is also a [[Borel measure]] , using the [[Borel sigma algebra]] and a [[compact]] set $$\mu: \mathcal{B}(X) \to [0, \infty ]$$with $\mu (K) < \infty$  
- [[counting measure]]  
- [[Dirac measure]] 
- [[Bildmaß(push forward measure)]] 
- [[Lebesque measure]] 




# Examples 
![[measure 2025-12-06 15.07.25.excalidraw]]



# Application