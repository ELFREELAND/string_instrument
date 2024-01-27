# string_instrument

## The classical wave equation

Waves are traditionally represented by the *wave equation*, a 2nd-order linear PDE:

$$\frac{\partial^2u}{\partial t^2}=c^2\frac{\partial^2u}{\partial x^2}$$

$u(x,t)$ represents the displacement of the string at position $x$, time $t$. This equation relates the acceleration of the string to its curvature. The constant $c$ is the propagation speed of a wave in the string, and it is equal to the square root of the tension divided by the linear density of the string:

$$c=\sqrt{\frac{T}{\rho}}$$

This equation is well-studied and we can solve it without a ton of trouble (see any differential equations or physics textbook for a walkthrough). After imposing the boundary condition that the string is fixed at both ends, we get solutions of the form:

$$u(x,t)=A\sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{n\pi ct}{L}\right)$$

If we introduce damping into the system, the classic wave equation becomes:

$$\frac{\partial^2u}{\partial t^2}=c^2\frac{\partial^2u}{\partial x^2}-\mu\frac{\partial u}{\partial t}$$

where $\mu$ represents the strength of damping. This version is much harder to solve analytically.

## The numerical approach

We are going to simulate a vibrating string. Specifically, I'd like to simulate the E string on a bass guitar. An analytical solution is possible for some simple cases, but I would like to simulate damping, specifically nonuniform damping which results from palm muting. This rules out an analytic solution, so we are going to take some help from a computer.

We're going to discretize the problem. Instead of a continuous string of constant linear density $\rho$, let's consider a massless string loaded with uniformly spaced point masses of mass $m$ spaced distance $\Delta x$ apart, such that $\frac{m}{\Delta x}=\rho$. The acceleration of each particle depends on how far it is from each of its neighbors, which gives a discrete version of the second derivative:

$$\frac{d^2u_i}{dt^2}=c^2\frac{u_{i+1}+u_{i-1}-2u_i}{\Delta x^2}-\mu_i\frac{du_i}{dt}$$

If the displacement of particle $i$ is exactly halfway between its neighbors, it will experience zero acceleration (save for that caused by damping). If its displacement is greater or less than the average of its neighbors, it will experience an acceleration towards their average. The particle will also experience an acceleration proportional to the magnitude of its velocity and opposite its direction, due to damping.

## Initial condition


## Damping

The effect of damping on the string's behavior is one of the more interesting 

Palm muting is an important guitar technique, especially in rock and metal music, which involves the guitarist holding the side of their picking hand against the strings near the bridge to mute them. This can be approximated by a small value of $\mu$ near the end of the 