```table-of-contents
```

# Probablities
Main idea is that we have empirical, non perfect observations, that are used to deduct results. Because the initial facts have an uncertaintly, the resulst can also be done only with a finite certainty. How to esimate those will be looked at in this chapter about probabilities. 

### Proposition  $$\omega(A) = T \qquad \qquad \omega(A) = F$$
with T for true and F fro false 
		- we know that something is true or false with a certainty or uncertainty = degree of belief 
		- set of all propositions = **web of belief** => is a good foundation for descisioin making 
	(*Bayesian school of thought*)
- **hypthesis H** -> $\omega(A)$ can be asserted with a degree of uncertainty 
- **data D** -> facts about empirical observations => $\omega(A) =T$ 
- **information I** (like the maxwell equations, that also have already a truth value assigned to them) -> accepted theories that always have as a true value 


### **Degree of belief**:  $$\mathcal{B} (A|I)$$
- this is the degree of belief = probability of the proposition $A$ under having the information $I$ 
	- ![[Axioms for probability]] 
- ![[Calculus rules for probabilities]] 



## types of porbablilites 
### sampling probability 
$$\mathcal{P} (D|H)$$
-> probability to observe data, assuming hypothesis is true   
-> is the genuine probability 
### inferential probability 
$$\mathcal{P} (H|D)$$
-> probability of hypotheiss being true, if data is observed 

## [[Probability calculus rues]]
### updating probabilities 
in case when we get new information $I$, that changes the previous assumption and data 
$$P^{after}(A) = \frac{P(B|AI)}{P(B|I)} \cdot P^{prior} (A)$$

- prior $P^{prior} (A) : = P(A|I)$: probability of A before information B 
- posterior $P^{after}(A) : = P(A|BI)$ : probability of A after information B
- likelihood $P(B|AI)$: probability of A after information B
- evidence $P(B|I)$: probability of B 

**No hypothesis, however unlikely, should be excluded from the beginning unless there is a logically cogent reason** 

### example 
infection $0.01 \%$ 
test :
- if sick -> $99\%$ positiv 
- if not sick -> $2 \%$ positiv 

$P(A_{sick}) = \frac{1}{10000}$
$P(\overline A) = 0.9999$ 
$B$ = test is positive 

$P(B|A) = 0.99$ 
$P(B|\overline A) = 0.02$ -> false positive and is what we really want to know 
$P(\overline B|A) = 0.01$ 
$P(\overline B|\overline A) = 0.98$ 

$P(A|B) = P(B|A) \frac{P(A)}{P(B)} = 0.0049$ -> around 0.5% 
$P(B) = P(BA) + P(B \overline A) = 


## Monty Hall problem 
![[Pasted image 20261013140952.jpg]]


# Stochastic independance 
Probability for A is independent from probability of B, if $P(A|BI) = P(A|I)$        $$P(AB|I)=P(A|I) \cdot P(B|I)$$

![[Lecture 0 2026-10-13 14.15.46.excalidraw]]

Take out 2 balls, one after another, without putting them back and we get the folowing possible outcomes: $\{(B_2,B_1), (B_2, W_1), (W_2, B_1), (W_2, W_1)\}$
The probabilities are now: 
- first pick 
$$P(B_1) = \frac{r}{n}$$
- second pick depends on the first one 
$$P(W_1) = \frac{n-r}{n}$$
- other probabilities:
$$P(B_2B_1) = \frac{r}{n} \cdot \frac{r-1}{n-1} \qquad \qquad P(B_2W_1) = \frac{n-r}{b} \cdot \frac{r}{n-1}$$
$$P(W_2B_1) = \frac{r}{n} \cdot \frac{n-r}{n-1} \qquad \qquad P(W_2W_1) = \frac{n-r}{n} \cdot \frac{n-r-1}{n-1}$$

From there we can work out: $$P(B_2) = P(B_2(B_1 + W_1)) = P(B_2B_1) + P(B_2W_1) = \frac{r}{n}$$
$$P(W_2) = \frac{n-r}{n}$$
To consider, that all the other pick depend on the information form the previous pick: $$P(B_2|B_1 I) = \frac{P(B_2B_1|I}{P(B_1|I)} = \frac{r-1}{n-1} \neq \frac{r}{n} = P(B_2|I)$$
here also to mention that in all of the equations above the $I$ is just dropped, but implied.
However: 
$$P(B_1|B_2I) = \frac{P(B_2B_1|I)}{P(B_2|I)} = \frac{r-1}{n-1} \neq \frac{r}{n} = P(B_1|I)$$
which is derived from Bayes' theorem. It means that the probability to get a black ball in the first pick changes, if we know what will be in the second one! this is kind of liek seeing the future. Those picks don't depend on eachother casually, the balls have not been picked yet, however just the knowledge changes the probabilities. In real life this is similar to making an assumption to what will happen. 

# Probability distribution 
## Stochastic variable 
Consider a die: 
- possible outcomes $\omega$ 
- set of all oucomes $\Omega$ 
- a **stochastic (random) variable** $X$ $$X: \quad \Omega \to \mathbb{R}$$$$\omega \quad \mapsto 
\quad x:= X(\omega)$$

### cumulative distribution function (CDF) F(x) 
-> probability of the proposition $A(x)$ , that $X$ doesn't get bigger than a certain $x$ :
$$F(x) := P(A(x)|I) \quad \text{with} \quad A(x) : \{-\infty < X \leq x\}$$
If $X$ has distribution $F$, then $X \sim F$ and for $F(x)$ we have: 
- $0 \leq F(x) \leq 1$ 
- $$\lim_{x \to - \infty}F(x) =0 \quad, \quad \lim_{x \to + \infty} F(x) =1$$
- $F(x)$ is right continous $$\lim_{x \to x_0^+}F(x) = F(x_0)$$
- $F(x)$ is monotonnically increasing $$F(x_2) >= F(x_1) \quad \forall x_2 > x_1$$

To differentiate: **discrete** and **stochastic** variables: 