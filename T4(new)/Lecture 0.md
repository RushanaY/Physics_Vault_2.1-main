L.Pollet, a newbie, cute 
zentralubung may be of friday 10-12 
Inhalt:
- Schollwock script (all 50 chapters?)
- probability theory
- thermodynamics
- statistical mechanics 

```table-of-contents
```

# Probablity 
- **Aussage (proposition = "atatement")**  A can true or not true $$\omega(A) = T \qquad \qquad \omega(A) = F$$
	with T for true and F fro false 
		- we know that something is true or false with a certainty or uncertainty = degree of belief 
		- set of all propositions = **web of belief** => is a good foundation for descisioin making 
	(*Bayesian school of thought*)
- **hypthesis H** -> $\omega(A)$ can be asserted with a degree of uncertainty 
- **data D** -> facts about empirical observations => $\omega(A) =T$ 
- **information I** (like the maxwell equations, that also have already a truth value assigned to them) -> accepted theories that always have as a true value 


## types of porbablilites 
### sampling probability 
$$\mathcal{P} (D|H)$$
-> probability to observe data, assuming hypothesis is true   
-> is the genuine probability 
### inferential probability 
$$\mathcal{P} (H|D)$$
-> probability of hypotheiss being true, if data is observed 

## Probability rules
### positivity
$$P(A|B) >= 0 \qquad \forall A,B$$
### Additivity
$$P(A_1 \lor A_2|B) = P(A_1|B) + P(A_2 |B)$$
$$\forall A_1, A_2 \space with \space \omega(A_1 \land A_2|B) = F$$
$F$ means false 
### Normalization 
$$P(A \lor \neg A|B)=1$$
### Product rule 
$$P(A \lor B|C) = P(A|B\land C) \cdot P(B|C)$$

### sum rule   n
$$P(A_1 + A_2|B) = P(A_1|B) + P(A_2|B) - P(A_1A_2|B)$$
where $A_1+A_2 =: A_1 \lor A_2$ and $A_1A_2 =: A_1 \land A_2$ 
### Marginalization rule 
$$\mathcal{P}(A|C) = \mathcal{P} (AB|C) + \mathcal{P}(A \neg B|C)$$ 
==🔵*(Reasoning under uncertainty; going from uncertain facts to some conclusions and being alright with the uncertainty of those; degrees of belief -> how to estimate how much you trust the results from uncertain sources)*==  

### Bayes' theorem 
$$\mathcal{P}(B|AI) \cdot \mathcal{P}(A|I) = \mathcal{P} (A|BI) \cdot \mathcal{P}(B|I)$$
with $\mathcal{P}(A|BI) \neq \mathcal{P} (B|AI)$

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