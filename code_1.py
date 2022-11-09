"""
@author: samku
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.labelsize"] = 16

x_array = np.linspace(-5, 5, 500)

k = 1 
v_x = k * x_array ** 2
psi = np.exp(-(x_array+2)**2)

fig, ax = plt.subplots()

ax.plot(x_array, np.abs(psi)**2)
ax.set_xlabel("x [arb units]")
ax.set_ylabel("$|\Psi(x, t=0)|^2$", color="C0")

ax_twin = ax.twinx()
ax_twin.plot(x_array, v_x, color='C1')
ax_twin.set_ylabel("$V(x)$", color="C1")
plt.show()

def f(x):
    """ The function we want to calculate the finite difference for"""
    return np.sin(x)

# Define a grid in x
N = 100
x_array = np.linspace(0, 2 * np.pi, N)

# Loop over the grid and calculate the second order derivative at each point
ypp_method1 = []
h = 0.5
for x in x_array:
    second_order_derivative = (f(x - h) - 2 * f(x) + f(x + h)) / h ** 2
    ypp_method1.append(second_order_derivative)
   
# Plot the results
fig, ax = plt.subplots()
ax.plot(x_array, f(x_array), label="f(x)")
ax.plot(x_array, -np.sin(x_array), label="$y''$ calculated exactly")
ax.plot(x_array, ypp_method1, "--", label="$y''$ calculated numerically")
ax.set(xlabel="x")
ax.legend()
plt.show()