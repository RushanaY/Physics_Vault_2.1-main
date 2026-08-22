# 14.1. [[sigma algebra]] and [[measurable map]]
## 14.1.1.  definition of [[sigma algebra]] 
"$\mathcal{A}$ is a  $\sigma$ - algebra on set X" => $(X, \mathcal{A})$ the short notation and is a [[measurable space]]  (a space X with a measure acting on it)

*collection of measurable subsets of a set X
those sets can be chosen to be together. We take only the ones that with the specific measure we want
properties about what kinds of sets should be inside*:
1. emtpy set and set itself $$\emptyset, X \in \mathcal{A}$$
2. complement of the set $$X/A \in \mathcal{A}$$
3. the union of all the subsets is also inthe algebra $$\bigcup_{n\in \mathbb{N}} A_n \in \mathcal{A}$$
## 14.1.2. remark 
$$\bigcap_{n \in \mathbb{N}} (X/V_n) = X/ (\bigcup_{n \in \mathbb{N}} V_n ) \in \mathcal{A}$$
$$\bigcap_{n\in \mathbb{N}} V_n = \bigcap_{n \in \mathbb{N}} (X/ (X/V_n)) = X/ (\bigcup_{n \in \mathbb{N}} (X / V_n) ) \in \mathcal{A}$$
*any intersection, no matter how is still part of the algebra*
## 14.1.3. examples 
for $X \neq \emptyset$ :
- $\mathcal{A}_1 =\{ \emptyset, X \}$ 
- $\mathcal{A}_2 = \mathcal{P} (X)$
- $\mathcal{A}_3 = \{ U \subset X: \text{U countable or X/U countble}\}$ 
are sigma algebras on X

### Proof: 
![[Pasted image 20260226195222.jpg]]
## 14.1.4 examples 
If $\mathcal{A}$ is a [[sigma algebra]] onto X, then: 
- is $Y \subseteq X$, then $$\mathcal{A}_Y : = \{ Y \cap V: V \in \mathcal{A} \} \subseteq \mathcal{P} (Y)$$
- is $T :Z \to X$ a map, then $\{ T^{-1} (V) : V \in \mathcal{A} \} \subseteq \mathcal{P} (Z)$ is a sigma algebra on Z 
- is $f: X \to Y$ a map, then $$\mathcal{C} : = \{ V \subseteq Y :f^{-1} (V) \in \mathcal{A}\}$$a sigma algebra onto Y 
*what having a set, equipped with an algebra means for our actions. what will a subset do, what will the map do, where this special set is a domain or a range*
### Proof 
![[Pasted image 20260226195144.jpg]]
## 14.1.5. Lemma 
If X is a set, $\mathcal{A}_i, i \in I$ a family of sigma algebras onto X, then $$\bigcap_{i \in I} \mathcal{A}_i = \{ V \subseteq X :V \in \mathcal{A}_i \space for \space alle \space i \in I \}$$
is also a sigma algebra
![[Pasted image 20260226195539.jpg]]
## 14.1.6. Definition
Is X a set, $\mathcal{E} \subseteq \mathcal{P}(X)$, so we call $$\sigma (\mathcal{E})  := \bigcap_{\mathcal{E} \subseteq \mathcal{A} \subseteq \mathcal{P}(X)} \mathcal{A}$$
a [[generated sigma algebra]] (erzeugte sigma algebra).
*this is the smallest possible sigma algebra, having only the neccecary parts*
Is $(X, \mathcal{O})$ a [[topological space]], then $$\mathcal{B} = \mathcal{B} (X) : = \sigma (\mathcal{O})$$
a [[Borel sigma algebra]] 
*the special thing about this algebra is really only that it is in a topological space with all the cool stuff of the topologal porperties*
## 14.1.7. Remark 
If $\emptyset = X$ a set, $\mathcal{E}, \mathcal{F} \subseteq \mathcal{P}(X)$. Per definition of the [[generated sigma algebra]], the $\sigma (\mathcal{E}$ ) is the smallest possible sigma algebra onto X and has also the set system $\mathcal{E}$ -> this can be shown by $\{ \emptyset, X \} \subseteq \sigma (\mathcal{E}) \subseteq \mathcal{P} (X)$ 

More so, for every algebra per definition true:  $\sigma (\mathcal{A}) = \mathcal{A}$ 
this means also $\sigma (\mathcal{E}) = \sigma (\sigma (\mathcal{E}))$  

If nothing further is implied, then we assume the [[Borel sigma algebra]]


## 14.1.8. 
we have a [[topological space]] and $\mathcal{A}  := \{ X/V: V \in \mathcal{O}\}$ the [[closed set|closed]] subset of X and $\mathcal{K} : = \{ K \subseteq X :\text{K compact}\}$ the set of [[compact]] subsets of X, then: 
- $\mathcal{B} (X) = \sigma (\mathcal{A})$
- if $\mathcal{E}$ is a [[countable]] basis of the [[topology]] $\mathcal{O}$, then $\mathcal{B} (X) = \sigma (\mathcal{E})$ 
- is X [[hausdorff]]ian  and there exists a [[sequence]] $(K_n)_{n\ in \mathbb{N}}$ of [[compact]] sets with $X = \bigcup_{n \in \mathbb{N}} K_n$ , then we have $\mathcal{B} (X) = \sigma (\mathcal{K})$ 

### Proof 
![[Pasted image 20260226204800.jpg]]

## 14.1.9. Definition of A-B meausrability 
we have two [[measure space]]s $(X, \mathcal{A}), (Y, \mathcal{B})$, then the [[Map]] $$f: X \to Y$$$\mathcal{A} - \mathcal{B}$ - measurable ([[A-B mesurable]]), only if $f^{-1} (B) \in \mathcal{A}$ for each $B \in \mathcal{B}$ 

## 14.1.10. Example 
If $(X, \mathcal{A})$ a [[measure space]], $A \subseteq X$, then is $A \in \mathcal{A}$ exacly when :$$\mathbb{1}_A :X \to \mathbb{R}$$
is also measurable 
-> $x \mapsto 1$ if $x \in A$ 
-> $x \mapsto 0$ if $x \in X/A$ 
![[Pasted image 20260226205323.jpg]]

*show that a subset is inside the algebra*

## 14.1.11 Satz
we have two [[measure space]]s $(X, \mathcal{A}), (Y, \mathcal{B})$ and $\mathcal{E} \subseteq \mathcal{P}(X)$ with $\sigma (\mathcal{E}) = \mathcal{B}$, then the following are equivalent 
- $f: X \to Y$ is [[A-B mesurable]] 
- for every $B \in \mathcal{E}$ is $f^{-1} (B) \in \mathcal{A}$ 

### Proof 
![[Pasted image 20260226205735.jpg]]  

*those are some truths we can use, as soon as we have something measurable*


## 14.1.12. Korollar  
![[Pasted image 20260228115436.jpg]]


*definition of the Borel measurable, nothing more than obvious facts stated by zenk*


## 14.1.13 lemma 
![[Pasted image 20260228115510.jpg]]
![[Pasted image 20260228115531.jpg]]

*definitions of generating systems -> it beongs on the cheat sheet*

## 14.1.1.4 Lemma 
![[Pasted image 20260228120823.jpg]]

### Proof 

![[Pasted image 20260228120900.jpg]]
![[Pasted image 20260228120946.jpg]]

*what a nice definition, and what a long proof. good to find questions ans answers with zenk using it*


## 14.1.15 Lemma 
![[Pasted image 20260228121131.jpg]]

### Proof 
![[Pasted image 20260228121146.jpg]]


## 14.1.16. Korollar 
![[Pasted image 20260228121235.jpg]]

### Proof 
![[Pasted image 20260228121252.jpg]]


## 14.1.17. Korollar 
![[Pasted image 20260228121354.jpg]]

### Proof 
![[Pasted image 20260228121420.jpg]]


## 14.1.18. Remark 
![[Pasted image 20260228121452.jpg]]


## 14.1.19. Korollar 
![[Pasted image 20260228121515.jpg]]


## 14.1.20. Definition 

![[Pasted image 20260228121538.jpg]]


## 14.1.21. Remark 
![[Pasted image 20260228121616.jpg]]


## 14.1.22 Satz 
![[Pasted image 20260228121642.jpg]]

### Proof 
![[Pasted image 20260228121703.jpg]]

------

# 14.2. [[measure]]
## 14.2.1. Definition of measure 
![[Pasted image 20260228121814.jpg]]


## 14.2.2. Example 
![[Pasted image 20260228121901.jpg]]
![[Pasted image 20260228121912.jpg]]



## 14.2.3. Remark 
![[Pasted image 20260228121958.jpg]]


### Proof 
![[Pasted image 20260228122019.jpg]]



## 14.2.4 Definition
![[Pasted image 20260228122122.jpg]]


## 14.2.5. Lemma 
![[Pasted image 20260228122148.jpg]]

### Proof
![[Pasted image 20260228122215.jpg]]
![[Pasted image 20260228122234.jpg]]



## 14.2.6. Remark 
![[Pasted image 20260228122259.jpg]]


## 14.2.7 Definition
![[Pasted image 20260228122429.jpg]]

![[Pasted image 20260228122445.jpg]]


## 14.2.8. Satz
![[Pasted image 20260228122512.jpg]]



## 14.2.9. Satz 
![[Pasted image 20260228122617.jpg]]



## 14.2.10 Satz
![[Pasted image 20260228122657.jpg]]



## 14.2.11 Lemma
![[Pasted image 20260228122719.jpg]]



## 14.2.12. Lemma
![[Pasted image 20260228122749.jpg]]



## 14.2.13. Satz 
![[Pasted image 20260228122814.jpg]]



## 14.2.14. Remark 
![[Pasted image 20260228132701.jpg]]



## 14.2.15. Remark 

![[Pasted image 20260228132724.jpg]]



## 14.2.16. Definition 
![[Pasted image 20260228132745.jpg]]



## 14.2.17. Lemma 
![[Pasted image 20260228132809.jpg]]
### Proof
![[Pasted image 20260228132854.jpg]]
![[Pasted image 20260228132911.jpg]]



## 14.2.18. Definition

![[Pasted image 20260228132930.jpg]]

----
# 14.3. Integration of non linear function 
## 14.3.1. Lemma 
![[Pasted image 20260228133215.jpg]]

### Proof 
![[Pasted image 20260228133227.jpg]]



## 14.3.2. Definition 
![[Pasted image 20260228133245.jpg]]



## 14.3.3. Lemma 
![[Pasted image 20260228133301.jpg]]



## 14.3.4. Lemma 
![[Pasted image 20260228133318.jpg]]

### Proof 
![[Pasted image 20260228133332.jpg]]
![[Pasted image 20260228133342.jpg]]



## 14.3.5. Lemma 
![[Pasted image 20260228133359.jpg]]

### Proof 
![[Pasted image 20260228133416.jpg]]
![[Pasted image 20260228133426.jpg]]



## 14.3.6. Definition 
![[Pasted image 20260228133442.jpg]]



### 14.3.7. Lemma 
![[Pasted image 20260228133506.jpg]]

### Proof 
![[Pasted image 20260228133524.jpg]]



## 14.3.8. Satz 
![[Pasted image 20260228133547.jpg]]

### Proof 
![[Pasted image 20260228133605.jpg]]



## 14.3.9. Korollar 
![[Pasted image 20260228133628.jpg]]

### Proof 
![[Pasted image 20260228133641.jpg]]



## 14.3.10. Remark 
![[Pasted image 20260228133704.jpg]]



## 14.3.11. Lemma 
![[Pasted image 20260228133722.jpg]]

### Proof 
![[Pasted image 20260228133737.jpg]]
![[Pasted image 20260228133750.jpg]]

----
# 14.4. Integrable complex function 
## 14.4.1. Remark 
![[Pasted image 20260228133830.jpg]]
![[Pasted image 20260228133842.jpg]]



## 14.4.2. Definition 
![[Pasted image 20260228133905.jpg]]


## 14.4.3. Remark 
![[Pasted image 20260228133922.jpg]]



## 14.4.4. Lemma 
![[Pasted image 20260228133941.jpg]]

### Proof 
![[Pasted image 20260228134006.jpg]]
![[Pasted image 20260228134020.jpg]]
![[Pasted image 20260228134035.jpg]]
![[Pasted image 20260228134050.jpg]]



## 14.4.5. Satz
![[Pasted image 20260228134118.jpg]]


### Proof 
![[Pasted image 20260228134138.jpg]]
![[Pasted image 20260228134152.jpg]]



## 14.4.6. Satz 
![[Pasted image 20260228134214.jpg]]


### Proof 
![[Pasted image 20260228134229.jpg]]

![[Pasted image 20260228134244.jpg]]



## 14.4.7. Korollar 
![[Pasted image 20260228134303.jpg]]


### Proof 
![[Pasted image 20260228134320.jpg]]
## 14.4.8. Lemma 
![[Pasted image 20260228134349.jpg]]


### Proof 
![[Pasted image 20260228134404.jpg]]
----------
# 14.5. Banach space
## 14.5.1. Remark 
![[Pasted image 20260228134455.jpg]]



## 14.5.2. Definition 
![[Pasted image 20260228134511.jpg]]



## 14.5.3 
![[Pasted image 20260228134527.jpg]]


### Proof 
![[Pasted image 20260228134537.jpg]]



## 14.5.4. Definition 
![[Pasted image 20260228134556.jpg]]



## 14.5.5. Lemma 
![[Pasted image 20260228134615.jpg]]


## 14.5.6. Satz 
![[Pasted image 20260228134634.jpg]]


### Proof 
![[Pasted image 20260228134648.jpg]]
![[Pasted image 20260228134658.jpg]]



## 14.5.7. Lemma 
![[Pasted image 20260228134713.jpg]]


### Proof 
![[Pasted image 20260228134731.jpg]]

![[Pasted image 20260228134744.jpg]]



## 14.5.8. Lemma 
![[Pasted image 20260228134757.jpg]]


### Proof 
![[Pasted image 20260228134816.jpg]]




## 14.5.9. Satz 
![[Pasted image 20260228134835.jpg]]


### Proof 
![[Pasted image 20260228134848.jpg]]


## 14.5.10. Satz 
![[Pasted image 20260228134903.jpg]]


### Proof 
![[Pasted image 20260228134918.jpg]]
![[Pasted image 20260228134939.jpg]]



## 14.5.11. Satz 
![[Pasted image 20260228134959.jpg]]

### Proof 
![[Pasted image 20260228135017.jpg]]

------
# 14.6. Integration of Banach functions 
## 14.6.1. Definition 
![[Pasted image 20260228135053.jpg]]



## 14.6.2. Satz 
![[Pasted image 20260228135108.jpg]]



## 14.6.3. Korollar 
![[Pasted image 20260228135125.jpg]]



## 14.6.4. Definition 
![[Pasted image 20260228135144.jpg]]



## 14.6.5. Lemma 
![[Pasted image 20260228135203.jpg]]



## 14.6.6. Remark 
![[Pasted image 20260228135225.jpg]]



## 14.6.7. Lemma 
![[Pasted image 20260228135244.jpg]]




## 14.6.8. Definition 
![[Pasted image 20260228135302.jpg]]



## 14.6.9. Satz
![[Pasted image 20260228135318.jpg]]


## 14.6.10. Remark 
![[Pasted image 20260228135342.jpg]]



## 14.6.11. Satz 
![[Pasted image 20260228135401.jpg]]



## 14.6.12. Korollar 
![[Pasted image 20260228135416.jpg]]



## 14.6.13. Satz 
![[Pasted image 20260228135433.jpg]]
