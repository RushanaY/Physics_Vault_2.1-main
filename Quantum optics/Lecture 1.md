```table-of-contents
```


# Gaussian beams 
going from wave equation $$\frac{\partial^n \psi}{\partial t^n} + \alpha \frac{\partial^m \psi}{\partial z^m} =0$$

dispersion relation: $$k(\omega) = \pm i \sqrt[m]{- \frac{(- i \omega)^n}{a}}$$
phase velocity: $\frac{\omega}{k}$ and group velocity $\frac{\partial \omega}{\partial k}$ 

wave equation with [[Maxwell equations]] ; taking case of no free charges$$\vec \triangledown^2 \vec E - \frac{n^2}{c^2} \overset{\cdot \cdot} E =0$$
These are the conditions of a Gaussian beam
- paraxial beams: separation of spatial derivatives 
- times dependence monochromatic : $\vec E \sim e^{+ i \omega t}$ 
- fixed polarization $\vec E \to E$ 
$$\triangledown_t^2 E + \frac{\partial^2}{\partial z^2} E + \frac{\omega^2}{c^2} n^2 E^2 =0$$
the translversal comes from $$\triangledown_t^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$$
using the ansatz for a plane wave (only distributed in z direction): $$E = E_0 \psi(x,y,z) e^{- ikz}$$ we end up at the equation which without the approximation looks liek this: $$\triangledown_t^2 \psi - z ik \frac{\partial \psi}{\partial z} + \frac{\partial^2 \psi}{\partial z^2}$$

Now we take the [[paraxial]] case, where $\frac{\partial \psi}{\partial z} \approx const$ in $\Delta z = \frac{\lambda}{2 \pi}$ and we get the equation for the [[paraxial wave equation]]:
$$  \triangledown_t^2 \psi - 2ik \frac{\partial \psi}{\partial z} =0$$

##  ![[Gaussian beam]] 

## Discussion 
![[Pasted image 20261026114342.jpg]]
### Wavefront curvature
- with the [[Wavefront curvature]] for the plane wave: $$R (z=0) = R(z = \pm \infty) = \infty$$
![[Lecture 1 2026-10-26 11.44.36.excalidraw]]
### far field divergence $$w(z \to \infty) = \omega_0 \sqrt{1 + (\frac{z}{z_0})^2} \quad \to \quad \omega_0 \frac{z}{z_0} = \frac{\lambda z }{\pi \omega_0}$$
- the last part is being defined as the 'angle of the divergence' $$\Theta = \frac{\lambda}{\pi \omega_0}$$ 

### uncertinty relation 
$$\frac{\Delta P_r}{P_z} = \Theta$$
where $P_r$ and $P_z$ are the radial and longitudinal momentum 
with $\Delta x = \omega_0$ the relation becomes: $$\Delta P_r \Delta x = p_z \Theta \omega_0 = \frac{h}{\lambda} \cdot \frac{\lambda}{\pi \omega_0} \cdot \omega_0 = 2 \hbar$$
Comments:
- $\omega_0 \Theta = const$ is a property of **wave mechanics**
- one can view the electric field as a **wave function of one photon** 


### Gouy phase 
![[Lecture 1 2026-10-26 11.53.22.excalidraw]]
$$arctg (\frac{z}{z_0}) \to \pm \frac{\pi}{2} \qquad for z \to \pm \infty$$
total phase shift of $\pi$ (the whole wave literally flips)
![[Lecture 1 2026-10-26 12.00.59.excalidraw]]

### focus site 
![[Lecture 1 2026-10-26 12.13.29.excalidraw]]
$$2 \Theta = \frac{2 \lambda}{\pi \omega_0} \approx \frac{d}{f} = N.A. (\text{Numerical aperture}) \quad \Rightarrow \quad \omega_0 \approx \frac{\lambda}{N.A.}$$
in good optics: $N.A. \approx 1 \Rightarrow \omega_0 \approx \lambda$. This is the giving the diffraction limit, that stops the paracial wave optics to reach infinite intensity

### higher order Gaussian modes 
-> rectangular symmetry: $TEM_{m,n}$ $$E_{m,n}(x,y,z) \sim H_m (\frac{\sqrt{2} x}{\omega(z)}) H_n (\frac{\sqrt{2}y}{\omega(z)}) \times e^{- \frac{r^2}{\omega^2(z)} - i \frac{k r^2}{2 R(z)} - i (kz - (1 + m + n) arctg(\frac{z}{z_0}))}$$
with $H_m(n)$ is the [[Hermite polynomial]]: 

-> rotatinal symmetry: $TEM_{l,p}$ 
$$E_{l,p} (x,y,z) \sim (\frac{r}{\omega(z)})^l \space e^{-ilp} L^l_p (\frac{2 r^2}{\omega^2(z)}) \times e^{- \frac{r^2}{\omega^2(z)} - i \frac{k r^2}{2 R(z)} - i (kz - (1+l+2p) arctg(\frac{z}{z_0}))}$$

Both fields are orthonormal functions and the power that is proportional to $\int EE^* dx dy = E_0^2 \frac{\pi \omega_0^2}{2}$ , making power independent of z. 