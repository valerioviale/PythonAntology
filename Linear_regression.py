# Linear Regression: This example uses sklearn
# to fit a straight line to the data.
# It generates data with a linear trend and adds some noise.
# The plot shows the data points and the fitted line.
# The intercept and coefficient are also printed.


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate some sample data
np.random.seed(0)
X = np.linspace(0, 10, 100)  # Independent variable
y = 2 * X + 1 + np.random.normal(0, 2, 100)  # Dependent variable with noise

# Reshape X to be a 2D array, as required by scikit-learn
X = X.reshape(-1, 1)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Plot the data and the regression line
plt.scatter(X, y, label='Data')
plt.plot(X, y_pred, color='red', label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.legend()
plt.show()

# Print the model's coefficients
print(f'Intercept: {model.intercept_}')
print(f'Coefficient: {model.coef_[0]}')