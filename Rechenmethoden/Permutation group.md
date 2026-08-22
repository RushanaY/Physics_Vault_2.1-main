- denoted as $S_n$ with n number of objects 
- permutation = rearranging of those objects 
- there are $n!$ different possible arrangements 
- it can be logically shown, that  a permutation is really a group 
- also called a symmetric group 
- but non ableian (the logic is that when doing two switches, it does matter which one is made first.  different order of switches leads to different results)
- there are different kinds :
	- **signum** $sgn(P)$ , where it is positive if P is even and negative if P is odd 
	- sgn(P) = sgn(P^-1) => why? 
	- show that this is a group homomorphism 
	- this is also used in the **Levi Civita symbol** 
yeah, no , that is too strange

Permutations generally permutate only between two elements, making them a pair. Therefor the notation of $[4,2,1,3]$ means, that we change the pair, going in this given order. As it is noted, permutations are not ableian and are not commutative. Therefore this notation$$[1234] \mapsto [4213]$$ can be also denoted on the $[4213]$. It means that we switch $4 \leftrightarrow 1$, $2 \leftrightarrow 2$ , $3 \leftrightarrow 1$, $4 \leftrightarrow 3$. Following this orders will lead to the wanted results. 
The same numbers can go through multiple amount of those kinds of permutations. Here it can be differentiated between odd and even ones. Denoted in the signum sign with P being the number of permutations:
$$sgn(P) = +1 \space for \space P \space even$$$$sgn(P) = -1 \space for \space  P \space odd$$
Using this notation, we can define the [[Levi Civita symbol]] 
$$\epsilon_{i_1, i_2...j_n}^{j_1, j_2,...j_n} \equiv sgn(P_{i_1, i_2...j_n}^{j_1, j_2,...j_n} )$$
The way it can be understood is to say that the $j_n$ and $i_n$ are the beginning and end sequence that we expect. The amount of permutations we need to get from one to another is then counted and it can be determined if it's odd or even. 