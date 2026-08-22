# Euclidian scalar product 
A defining property of Euclidian geometry is the scalar product. Here the scalar product or dot product is used because we call it the standard scalar product of a standard space. The more general notation would be inner product. 
It is a function that takes in two vectors and gives a number $$\langle \space , \space \rangle :\mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$$$$(\vec v, \vec w) \mapsto \langle \vec v, \vec w \rangle \equiv v^1w^1 + v^2w^2 + ...+ v^nw^n$$
In [[Einstein summation convention]]  in [[Covariant and contravariant notation|covariant]] notation$$\langle \vec v, \vec w \rangle = v^iw_i = v_i w^i$$

It is a very powerful instrument in geometry, as it allows to depict geometric ideas in mathematical language. Giving us the most important tools being the lengths and angles. 
The  geometric length is defined by the [[norm]] of a vector $$|| \vec v || = \sqrt{\langle \vec v, \vec v\rangle}$$
The angle is defined using the  [[Cauchy Schwartz inequality]] $$|\langle \vec v, \vec w \rangle \leq ||\vec v || \space || \vec w ||$$
from this we get an [[angle between two vectors]] $$\langle \vec v, \vec w \rangle = cos (\angle (\vec v, \vec w) ) ||\vec v || \space ||\vec w ||$$

## Properties of scalar product 
1. Symmetry $$\langle \vec v, \vec w \rangle = \langle \vec w, \vec v \rangle$$
2. Linearity $$\langle a \vec v, \vec w \rangle = a \langle \vec v, \vec w \rangle$$$$\langle \vec u + \vec v, \vec w \rangle = \langle \vec u, \vec w \rangle + \langle \vec v, \vec w \rangle$$
3. Positive definiteness $$\langle \vec v, \vec v \rangle > 0, \space \forall \vec v \neq 0$$
## Inner product 
This is a synonym for scalar product, but is more general
If a vector space has inner product, then it is a normed vector space or Euclidian vector space. 


## Normalization
In simple words is a coefficient you have to multiply your vector with in order to make its norm be equal to 1
$$|| \hat w|| = 1$$
$$\hat w \equiv \frac{w}{||w||}$$ 

### orthogonality 
If this relation holds, then the vectors are orthogonal : $\langle \vec v, \vec w \rangle =0$


The **decomposition** of a vector in a scalar product gives two parts of the vector that are defined through the scalar product itself. One part is the **projection** onto the other vector and the **orthogonal complement** being the other part of the first vector.  ![[scalar decomposition.png]]

The definition of the separate parts of the decomposed vector are: 
$$v_{||} = \hat w \langle \hat w, \vec v \rangle$$$$v_{\bot} = \vec v - \hat w \langle \hat w, \vec v \rangle$$
Where the first term is made up from the unit vector, that gives the direction and the scalar product that gives the magnitude, which together gives a new vector - the parallel component. 

# Orthonormalization 
Putting together [[Euclidian geometry#Normalization|normalization]] and [[Euclidian geometry#orthogonality|orthogonality]] we can make an [[orthonormal basis]] out of not orthonormal vectors. This can be done by using the 
# Gram Schmidt orthonormalization
all vectors are orthogonal to eachother and have length one. We go from the vector set $\{\vec v_j\}$ into a standard basis $\{\vec e_j \}$ 
1. Choose any vector $v_1$as the starting point
2. normalize the $v_1$ into $\hat v_1$
3. Subtract $\hat v_1 \langle \hat v_1, \vec v_2 \rangle$ from $\vec v_2$ and normalize the resulting $\hat v_2$ 
4. every next vector that is then also subtracted the scalar product of all the previous normalized vectors in the same manner as in step 3. 

# Metric tensor 
$$g_{ij} \equiv \langle \hat v_i, \hat v_j \rangle_V$$
In case the metric tensor is symmetric, it can be denoted as $g_{ij} = g_{ji}$ 
For a trivial, orthonormal basis the tensor is equal to a [[Kronecker delta]]  $g_{ij} = \delta_{ij}$ 
Using this relation we can generalize the scalar product: $$\langle \hat x, \hat y \rangle_V = \langle \vec x, \vec y \rangle_{\mathbb{R}^n} \equiv x^i g_{ij} \space y^j$$
Another role it plays is in the [[Covariant and contravariant notation]] 
## index lowering
$$x_j \equiv x^i g_{ij}$$
## index raising 
$$x^i = x_j g^{ji}$$
## inverse metric tensor
$$g_{ki}g^{ji} = \delta_k^i$$ 
## expansion of vectors 
take a contravariant basis vector $\hat v^i$ 
$$\hat v^i \equiv g^{ij} \hat v_j$$ in order to define **any** vector x: $$\hat x = \hat v_i \langle \hat v^i, \hat x \rangle_V$$
*This is very interesting and not talked enough about. So the answers will come from doing the exercising*

Definition of an orthonormal basis $$\eta_{ij} = \langle \hat e_j, \hat e_j \rangle_V$$
where this symbol $\eta$ the same as the metric tensor or kronecker delta, but specifically for the **orthonormal basis** 
As it is defined through the inner product and is defined for the specific vector space, so it is actually not normal to have a standard vector space with an orthonormal basis. It is a set of a very specific conditions, that are hidden in the definitions of the standard scalar product, orthonormality, normalization. The simplest case and also the most desirable one is $g_{ij} = \eta_{ij} = \delta_{ij}$. 
In this case we get the simplest definition of any vector $$\hat x = \vec e_j x^i$$
A couple lines above there was a general definition of any vector using the inner product, which was also used here, but we were able to shorten the notation because of the simplicity. 
