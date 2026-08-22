# Subspace
Is part of a space and denoted with $\subset$, for example $W \subset V$. 

In case of 3 dimentional vector spaces those can be planes, lines, dots. 

# Vector space 
Analogous to the [[Group]]s and [[Field]]s, we also can make a space with ridged rules for vectors. 
A vector is simultaneously a geometric object represented by an arrow and also an algebraic one, that allows to make this connection to [[Linear Algebra]]. 
In physics the most often used space is the [[standard vector space]] $\mathbb{R}^n$, where n denotes the [[dimension]] of the vector space. 
## Formal definition 
It is a field with two operations:
- **Vector addition** $$+ : V \times V \to V, \space (\vec v, \vec w) \mapsto \vec v + \vec w$$
- **Multiplication with scalars** $$\cdot: \mathbb{F} \times V \to V, \space (a, \vec v) \mapsto a \cdot \vec v \equiv a \vec v$$
	where $\mathbb{F}$ is just any set of numbers. It can be the real numbers, complex or any of similar kind. 

## Vector space axioms
- Distributivity of a scalar addition $$(a + b ) \vec v = a \vec v + b \vec v$$
- Distributivity of vector addition $$a( \vec v + \vec w) = a \vec v + a \vec w$$
- Associativity of scalar multiplication$$(ab) \vec v = a(b \vec v)$$
-  neutral element leaves vector invariant $$1 \vec v = \vec v$$
	- the neutral element for the scalar is already defined in the field ($\mathbb{R}, + . \cdot$ ) 


## Linear combination
$$a,b,c \in \mathbb{F}, \vec u, \vec v, \vec w \in V: a \vec u + b \vec v + c \vec w$$
where $\mathbb{F}$ is just any set of numbers. It can be the real numbers, complex or any of similar kind. 


## [[Covariant and contravariant notation]]

# Affine space 
This is a mathematical word for an infinitely spread $d$ dimentional space. The elements of this space are points, that are connected with arrows = vectors. 
Any vector space is an affine one, if their neutral element, the $\vec 0$ is the same as the origin point. 
# Euclidian space 
$$V = \mathbb{R}^n$$ then we can denote the d dimensional Euclidian space $\mathbb{E}^d$ 

# Functional spaces
The elements of this space are functions, instead of vectors. Probably it is the easiest to look at a [[polynomial]] 