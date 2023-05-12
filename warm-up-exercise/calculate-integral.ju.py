# %% [markdown]
"""
# This example is for calculate the area of a shape based on Monte Carlo simulation and integral
In this example we will use the area of an equation, which have the equation of
$$f(x,y) = x^2 + y^2$$
Where f(x,y) is the $r^2$, and $x, y <= 1$
- We will generate random example in a uniform manner (n = 10000) and evaluate at each example point
- Calculate the area of the shape by using both integral and Monte Carlo and verify the result
    - Upper bound and lower bound of the area is -1 and 1, and r = 1
    - Equation for Area
# %% [markdown]
""""""$$Area = 2\int_{-r}^{r} r \sqrt{1 - \frac{x^2}{r^2}}$$

"""

# %%
# import library
import numpy as np
import matplotlib.pyplot as plt
import scipy as s
import math

# %%
# Define radius
r = 1


# Calculate the area by Integral
# Define the function for Integral
def area_by_integral(x):
    return 2 * r * math.sqrt((1 - (x**2) / (r**2)))


# Using scipy for integral (deterministic method)
res, err = s.integrate.quad(area_by_integral, -r, r)

res


# %%
# Define the equation of the circle (or the shape)
def k(x, y):
    return x**2 + y**2


# Define the number of sample
n = 10**6
# Generate random sample that satisfy the condition
x_samples = np.random.uniform(-1, 1, n)
y_samples = np.random.uniform(-1, 1, n)
x_samples.shape
# %%
# Pair x,y
x_y = np.array([x_samples, y_samples])
# %% [markdown]
"""
Now this is a tricky part, in order for those point to satisfy the condition of belonging 
to our circle, we need to make sure that those points satisfy a condition of the equation
of the circle. The condition should be 
$$r^2 >= x^2 + y^2$$
"""


# %%
def filter(pair -> ):
    return pair > 0

mask = np.vectorize(filter)(x_y)

# %%
# Plot the generated point
# plt.scatter(x_samples, y_samples, c=f_values, cmap='coolwarm')
plt.scatter(x_samples, y_samples, cmap="coolwarm")
# plt.colorbar()
plt.title("Monte Carlo Simulation of Area Calculation")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %%
# # Evaluate the function at each sample point
# f_values = f(x_samples, y_samples)
# # Calculate the area of the shape
# area = (b - a)**2 * np.mean(f_values)
# # Print the result
# print("The area of the shape is approximately", area)
