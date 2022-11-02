import numpy as np
from matplotlib import pyplot as plt

# parameters
N = 10_000
output_filename = f"pi_estimate_N-{N:d}.png"

# draw random positions
x = np.random.uniform(size=(N, ))
y = np.random.uniform(size=(N, ))

# check if in circle
r_squared = (x ** 2 + y ** 2)
in_circle = (r_squared < 1)

# estimate PI
pi = 4.0 * in_circle.sum() / N

# visualize and save figure
plt.scatter(x[in_circle], y[in_circle], c='r', s=3)
plt.scatter(x[~in_circle], y[~in_circle], c='b', s=3)
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"N = {N:d}\npi = {pi:.5f}")
plt.axis("square")
plt.savefig(output_filename)