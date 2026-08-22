sheet and solutions at [[T3_ÜB_lösung_01.pdf]]
# Problem 1: Vector Calculus 
Useful [[Check list for good identities]] 
$$(1) \space \triangledown \cdot (fg) = f \triangledown \cdot g + g \cdot \triangledown f$$
$$(2) \space \triangledown \times (fg) = f \triangledown\times g - g \times \triangledown f$$
$$(3)\space  \triangledown \times (g \times r) = 2g +r \frac{\partial g}{\partial r} - r (\triangledown \times g)$$
$$(4) \space (v \times \triangledown) \times w - v \times (\triangledown \times w) = (v \cdot \triangledown) w - v (\triangledown \cdot w)$$

for $\vec w = \triangledown \phi$ ([[gradient field]]) and $\triangledown \cdot \vec v = 0$
$\phi (\vec r)$ and $| v (\vec r)|$ decay faster than $\frac{1}{r}$ as $r \to \infty$ 
then
$$\int_{\mathbb{R}^3} d^2 \vec r \vec w \cdot \vec v =0$$
for $\triangledown \times v =0$ , then $$\int_{\mathbb{R}^3} d^3 \vec r \vec w \times \vec v =0$$


# Problem 2: Properties of [[Fourier transform]]
Assume her that [[Dirac \delta distribution]] $\approx$ $\epsilon \to 0$ limit of several continuously differentiable approximations of $\delta_{\epsilon} (x)$
Normal distribution $$\delta_{\epsilon} (x) = \mathcal{C}^{-1} \exp(- \frac{x^2}{2 \epsilon})$$
##  Derive $\mathcal{C}$ for distribution being normalized 
Normalization criteria is $$\int_{\mathbb{R}} dx \space \delta_{\epsilon} (x) =1$$
Use [[Gaussian integral]] $$\int_{\mathbb{R}} dk \space \exp(-\frac{k^2}{2 \epsilon}) = \sqrt{2 \pi \epsilon}$$
=> $$\mathcal{C} = \sqrt{2 \pi \epsilon}$$
