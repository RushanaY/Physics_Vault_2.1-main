The matrix is the representation of a linear map and has therefore similar structure. 
General notation would look like this: 
$$\vec x \mapsto A \vec x$$
The vector is the argument, that is "put through" the matrix by multiplying them and getting out another vector, that is denoted as: $$A^i_jx_j$$
## [[kernel]]
On of the parameters of the matrix is the kernel, which is a set of all vectors that become zero, if out through the matrix. The kernel is used in the [[dimension formular]], that can quickly give the dimension of the kernel and the vector space itself. 

## [[rank]] 
The rank of the matrix is the dimension, basically the number of rows and columns. 

## [[trace]] 
The trace of a matrix, which is the sum of diagonal elements of the matrix

## [[determinant]]
This allows the geometric interpretations. It is also used heavily in order to derive characteristics about the matrix and expecially the linear map. 

Writing down the matrix using the [[Einstein summation convention]]:  
 $$A = \{A_j^i\}$$

- $i$ - rows,
- $j$ - columns 

Using this in practise we can look at two boundary cases. The first one is $m \times 1$, having $m$ rows and $1$ column, which makes it a vector. The reverse of that would be $1 \times m$, that has $1$ row and $m$ columns, which makes a thing, that looks like a transposed vector. It is important to remember, that it is not a vector, but actually just one row of a matrix. Interpreting it the wrong way will lead to confusion with covariance


# Actions 
## multiplication of vector and matrix 
the easiest way is to imagine that you put the vector horizontally onto the matrix and move downwards, multiplying all the numbers and adding them up row wise. 

Linear maps defined by their action on the [[standard basis]]  vectors: $$A \vec e_j = A_j$$ ![[matrix vector multiplication.png]]
## Matrix multiplication
It can also be imagined as the matrix [[composition of maps]] $$C = A \circ B$$In index notation using the [[Einstein summation convention]]$$C^k_j = B^k_iA^i_j$$
![[matrix multiplications.png]]

The properties of this multiplications are it being **associative, distributive, NOT commutative** and an extra is the factor reversing $$(A \cdot B)^T = B^T \cdot A^T$$

## Transpose matrix 
$$(A^T)^i_j = A^i_j$$ Take the diagonal from the upper left corner to the lower right corner and flip the matrix along this line upwards. 

## Adjoint matrix 
$$A^{\dagger} = \overline A^T$$This is only important if the matrix has [[Numbers#Complex numbers|complex]] numbers, because the **imaginary component** gets its sign reversed
$$+ 2i \to - 2i$$
# Inverse of a matrix
The definition of the inverse has its roots in the criterias for [[Group]]s, that states that there must be an element, which is the inverse. To be exact, the matrix is the element of the group, that is equipped with matrix multiplication. What that means here is, that multiplying with this element will make the [[neutral element]] : $$A^{-1}A = AA^{-1} = \mathbb{1}$$
In the case of the matrix, the neutral element is the [[unit matrix]] 

The matrix is basically a linear map, which is why its inverse matrix has the same idea as the inverse map. The same way if has to be [[bijective]] in order to do that. In case of a matrix the bijectivity and therefore it is invertible if:
1. is a square matrix ($A: \mathbb{C}^n \to \mathbb{C}^n$) 
2. the vectors of the basis remain a basis after being put through the matrix or the non zero vector is mapped to non zero $$\forall \vec v \neq 0: A \vec v \neq 0$$3. check if [[kernel]] is made up only out of the zero vector 

Or you can check the [[determinant]]. If it's not zero, then the matrix is invertible. 

In order to compute the inverse, there are multiple methods, but none are simple


# Application equation
Solving **system of linear equations**  
General form of the equations: $$A \vec x = \vec b$$
- $b=0$ : homogenous 
- $b \neq 0$ : inhomogenous

The simplest case is the homogenous case, which can be expanded into a system of linear equations, each of which is equal to zero, making them very easy to solve. In the end we find a vector $c \vec x$, which fulfils the equation $A \vec x =0$. 

Although not every equation is solvable uniquely or even at all. 
Most importantly the number of equations should be the same as the number of variables, then the solution is unique. 

If there are fewer equations than variables, then the solution is under determined and we can't express all the variables uniquely.

And the last option is to have more equations than variables, which makes it over determined and doesn't allow any solutions. 

# Application 
[[The square]] 
[[Coordinate change using a matrix]] 
[[Change of matrix representation]] 

# [[Matrix diagonalization]]
As known from above, the matrix is only a representation of a linear map. There can be any kind of representation and therefore we are free to choose the simplest. Matrix diagonalization is the method of finding such matrix. 


# linear group  
This is a set of matrices with non vanishing [[determinant]]s. It can be either 
- **[[general linear group]]**$$GL(n, \mathbb{C})$$
- **[[special linear group]]** $$SL(n, \mathbb{C})$$ 

