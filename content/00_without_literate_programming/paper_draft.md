# Estimating the number PI

## Monte Carolo method

The area of a unit circle is $\pi$:
$$
\int\limits_{x^2 + y^2 < 1.0}{\rm d}x{\rm d}y = \pi
$$

We can approximate this integral using $N$ randomly chosen positions $x$ and $y$:
$$
\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{n=1}^N ((x_n^2 + y_n^2) < 1) = \pi
$$
with uniform random values of $x_n\in[-1, 1)$ and $y_n\in[-1, 1)$.

Using rotational symmetry, we can reduce this to the quarter circle:
$$
4 \cdot \lim_{N\rightarrow\infty} \frac{1}{N}\sum_{n=1}^N ((x_n^2 + y_n^2) < 1) = \pi
$$
with uniform random values of $x_n\in[0, 1)$ and $y_n\in[0, 1)$.

## Implementation

See [this script](run_simulation.py) for details.

## Results


_TBD_