"A group is a set with more action" 

Connecting multiple [[Set]]s with an operation makes a group, denoted as $(A, \#)$. This operation is applied to every element of the group and has to fullfill certain conditions - the group axioms

# Group axioms 
1. **Closure**: 
	- all elements and the results of the operation should still be elements of the set. For example $2,3 \in \mathbb{N}$ and also $2+3 = 5 \in \mathbb{N}$. On the other hand the same elements in the case of $2 : 3 = 2/3 \notin \mathbb{N}$
	$$\forall a,b \in A , a \# b \in A$$.
2. **Associativity** $\forall a,b,c \in A$$$(a \# b) \# c = a \# (b \# c)$$
3. **Neutral element** (identity element, null element)$$\exists e \in A \Rightarrow e \# a = a \# e = a$$
4. **Inverse element** $\forall a \in A, \exists b \in A$ $$a \# b = b \#  a = e$$
5. Special case: **Commutative** $\to$ if the group has all the properties from above and is also a commutative, then it is an **Abelian group** $$a \# b = b \# c$$

# Group homomorphism 
It is a [[Map]], that connects two sets, which are themselves bound in a group. $$\psi : G \to H$$ where $(G, \#)$ and $(H, \cdot)$ are groups. This map can be anything, for example $n^2$ or just $n$ 
A good way to check that, is to see if the equality holds: $\psi(n +m) = \psi(a) \cdot \psi(b)$.
If the map is a [[bijective]] homomorphism, we can call it a **group isomorphism**. 
A special and intresting case is the [[Permutation group]] 