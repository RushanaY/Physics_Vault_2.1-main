- extention of the [[Propositional logic]] to quantify the used language 
- [[expression]] $\phi (x_1,...)$ is dependant on the  [[free variable]]s $x_1, ...$  and can be joined by [[logical connective]]s -> the expression has still be interpreted and using your own common sense desided if the value is truth or false 
- [[Quantifier]]s $$\exists x \phi(x)$$$$\forall x \phi(x)$$
$$\exists ! x \in D: \phi(x) \equiv \exists x \in D: (\phi(x) \land (\forall y \in D: \phi(y) \to y=x))$$


- in notation  these are equivalent, but it is probably good for proof to be able to work with logal connections of [[conjuction]]and [[subjunction]] $$\exists x \in D:  \phi (x) := \exists x (x \in D \land \phi(x))$$$$\forall x \in D: \phi(x): = \forall x (x \in D \to \phi (x))$$
	- about notation:  $\forall x \in D \phi (x)$ is a short notation  
- if quantor works onto expression with free variables, these variables become [[bound variables]] (makes sense, quantors are are truthful for certain variables, which is why we can't choose them, they are defined for us), important - only the varibale that is bound by the variable becomes a bound varuable. expression can have as many as it wants and those remain free 
- [[de Morgan's rule]] $$\neg (\# x \space \phi(x)) \equiv \overline \# x \neg \phi(x)$$
	- [[dMr for predicate logic]] $$\neg (\# x \in D : \psi (x)) \equiv \overline \# x \in D: \neg \psi (x)$$
	- [[general dMr for predicate ]] $$\neg (\#_1 x_1 ...\#_nx_n : \psi (x_1, ..., x_n)) \equiv \overline{\#}_1 x_1...\overline{\#}_n: \neg \psi (x_1,...x_n))$$

# Calculus 
[[Proof strategies]] 