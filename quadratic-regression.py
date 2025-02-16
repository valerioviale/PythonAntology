"""
Linear Regression: This example uses sklearn
to fit a straight line to the data.
It generates data with a linear trend and adds some noise.
The plot shows the data points and the fitted line.
The intercept and coefficient are also printed.
"""
import numpy as np
import matplotlib.pyplot as plt

# Example quadratic coefficients (you'd estimate these from your data)
a = 1
b = -5
c = 6

# Calculate the roots using the quadratic formula
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    x1 = (-b + np.sqrt(discriminant)) / (2*a)
    x2 = (-b - np.sqrt(discriminant)) / (2*a)
    print(f'Roots: x1 = {x1}, x2 = {x2}')
else:
    print("No real roots exist.")
    x1 = None
    x2 = None

# Plot the quadratic function
x = np.linspace(-1, 6, 100)
y = a*x**2 + b*x + c

plt.plot(x, y, label='Quadratic Function')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Function and Roots')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis

if x1 is not None and x2 is not None:
    plt.scatter([x1, x2], [0, 0], color='red', label='Roots')  # Mark the roots

plt.legend()
plt.grid(True)
plt.show()