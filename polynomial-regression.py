# Polynomial Regression: This example uses
# sklearn.preprocessing.PolynomialFeatures to transform the input features
# into polynomial features (e.g., x, x^2, x^3, etc.). Then, it uses
# sklearn.linear_model.LinearRegression to fit a linear model to these
# transformed features. This effectively fits a polynomial curve to the data.
# I use make_pipeline to chain these two operations together. The example
# generates data with a quadratic trend and adds some noise. The plot shows
# the data points and the fitted curve. I've changed the X_plot variable in
# this example to use a different variable to plot the fitted model, so that
# it has a smoother appearance.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Generate some sample data
np.random.seed(0)
X = np.linspace(0, 10, 100)
y = 3 * X**3 - 2 * X**2 + X + np.random.normal(0, 5, 100)
print(X)
print(y)


# Reshape X
X = X.reshape(-1, 1)
print(X)

# Create a polynomial regression model (degree=2 for a quadratic)
degree = 2
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

# Fit the model to the data
model.fit(X, y)

# Make predictions
X_plot = np.linspace(0, 10, 100).reshape(-1, 1) # Use a different X_plot for better visualization
y_pred = model.predict(X_plot)

# Plot the data and the regression curve
plt.scatter(X, y, label='Data')
plt.plot(X_plot, y_pred, color='red', label='Polynomial Regression (degree=' + str(degree) + ')')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Polynomial Regression Example')
plt.legend()
plt.show()
