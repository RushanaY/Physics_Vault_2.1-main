also called the **cross product** 
It has two definitions, the geometric being the surface of the spanned area and the algebraic being permutation (of course in [[orthonormal basis]])

A couple words about the geometric formulation. Just the cross product itself is already the area. If we want to compute a volume we multiply the cross product with the third vector, the hight, in a [[scalar product]] $$\text{Vol}(\vec u, \vec v, \vec w) = |(\vec u \times \vec v) \cdot \vec w|$$Which is simply the normal way of finding volume by multiplying the area with the height. Using three vectors like here makes it also a **triple product** 

This **triple product** can also be denoted as a [[determinant]] $\det(\vec u, \vec v, \vec w)$ , as both structures have the geometrical interpretation of being a volume. 
# Properties vector product 
- Perpendicular
	the new vector is perpendicular two both used vectors 
- Orientation
	the new vector can point upwards or downwards, which can be concluded by using the [[right hand rule]] 
- Norm 
	The norm of the cross product gives the area of the parallelogram spanned by the two vectors $$|| \vec v \times \vec w || = || \vec v || \space || \hat w || sin \theta$$
- Properties
	- antisymmetric $$\vec v \times \vec w = - \vec w \times \vec v$$
	- distributive $$\vec u \times (\vec v + \vec w) = \vec u \times \vec v + \vec u \times \vec w$$
	- is not associative $$\vec u \times (\vec v \times \vec w ) \neq (\vec u \times \vec v ) \times \vec w$$

	The vector $\vec v \times \vec w$ is not in the same $\mathbb{E}^3$ as $\vec v$ and $\vec w$ and is therefore a **pseudo vector** or **axial vector** . What is important to understand is, that the vectors we used are made up of the three components of the 3 dimensional Euclidian space, but it is not a vector space. Even if it looks like a vector and behaves like a vector, it is not officially part of the vector space. However the computed vector from the vector product is in the vector space. 
	While the difference feels only formal, it does become important once we start working with [[Tensor]]s. The vector from the vector product is in the vector space that we can call the "covariant tensor of first degree"

# Application
It is a key component in the [[angular momentum]] 
$$\vec L = m \vec r \times \vec v$$
Another one is [[torque]], being the cross product of vector and force.

# Algebraic formulation 
The cross product is on the verge of the vector space and the euclidian space, so therefore it is useful to have an algebraic formulation. 
For labeling we use the [[orthonormal basis]] with numbered vectors going from 1 to 3, what makes them **positively oriented**. It is merely convention and notation, that can be made for any basis by moving the labels around. What it allows is to have the properties of the cross product be more intuitive, like the change of sign when reversing the order (antisymmetry). It should also be clear, that making the cross product of two basis vectors automatically gives the third one, because it is per definition orthogonal to the previous two: $\vec e_i \times \vec e_j = \pm \vec e_k$ 

This is also elaborated on and seen better in the cyclic diagramm, that shows the "right" and reversed order of vector. 
![[cyclic.png]]
This reminds and is identical to the structure of the [[Levi Civita symbol]], which allows to write the cross product as: $$\vec e_i \times \vec e_j = \epsilon_{ijk} \vec e_k$$
And also $$(\vec e_i \times \vec e_j ) \cdot = \epsilon_{ijk}$$
So more generally for any vector $$(\vec u \times \vec w)^k = u^i w^j \epsilon_{ijk}$$
The most general way, considering the correct [[Covariant and contravariant notation|covariant]] ant notation and the [[metric tensor]] $$\vec u \times \vec w = \sqrt{g} \space u^iw^i \epsilon_{ijl} \space g^{lk}\vec v_k$$
# Vector product identities 
## bac cab formular 
$$\vec a \times (\vec b \times \vec c) = \vec b(\vec a \cdot \vec c) - \vec c (\vec a \cdot \vec b)$$ 
## Grassmann identity 
$$\vec u \times (\vec v \times \vec w) = \vec v (\vec u \cdot \vec w) - \vec w (\vec u \cdot \vec v)$$
## Jacobi identity
$$\vec u \times (\vec v \times \vec w) + \vec v \times (\vec w \times \vec u) + \vec w \times (\vec u \times \vec v) = 0$$
## Lagrange identity 
$$(\vec v \times \vec w) \cdot (\vec t \times \vec u) = (\vec v \cdot \vec t) (\vec w \cdot \vec u) - (\vec v \cdot \vec u)(\vec w \cdot \vec t)$$
$$(\vec v \times \vec w)^2 = || \vec v||^2 \space || \vec w ||^2 - (\vec v \cdot \vec w)^2$$