import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

# Load dataset
file_path = "/Users/valerio/Desktop/Courses/PythonAntologia/PythonAntology/Salary_dataset.csv"
df = pd.read_csv(file_path)

# Extract features and target variable
x = df[['YearsExperience']].values  # Independent variable
y = df['Salary'].values  # Dependent variable

# Train the model
model = LinearRegression()
model.fit(x, y)

# Get the slope (beta) and intercept (alpha)
alpha = model.intercept_
beta = model.coef_[0]

# Compute the x-axis intersection (where y = 0)
x_intercept = -alpha / beta

# Print the regression equation
print(f"Equation: y = {alpha:.2f} + {beta:.2f}x")
print(f"The regression line crosses the x-axis at x = {x_intercept:.2f}")

# Predict values
y_pred = model.predict(x)

# Plot data and regression line
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_pred, color='red', label='Regression Line')

# Plot the x-axis intersection
plt.scatter(x_intercept, 0, color='green', marker='o', s=100, label='X-axis intercept')

# Labels and legend
plt.axhline(0, color='black', linewidth=0.5)  # X-axis
plt.axvline(x_intercept, color='green', linestyle='dashed', linewidth=1)  # Intercept line
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

# Compute residuals
residuals = y - y_pred  

# Residual Plot
plt.scatter(x, residuals, color='purple', label='Residuals')
plt.axhline(0, color='black', linestyle='dashed', linewidth=1)
plt.xlabel('Years of Experience')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.legend()
plt.show()

# Salary Boxplot
plt.boxplot(y, vert=False)
plt.xlabel('Salary')
plt.title('Salary Distribution')
plt.show()

# Histogram of Residuals with Normal Curve
plt.hist(residuals, bins=10, density=True, color='orange', edgecolor='black', alpha=0.7, label="Residuals")

# Compute mean and standard deviation of residuals
mu, sigma = np.mean(residuals), np.std(residuals)

# Generate x values for the normal curve
x_vals = np.linspace(min(residuals), max(residuals), 100)

# Compute y values for the normal curve
y_vals = stats.norm.pdf(x_vals, mu, sigma)

# Plot normal distribution curve
plt.plot(x_vals, y_vals, color='red', linewidth=2, label="Normal Curve")

# Labels & title
plt.xlabel('Residuals')
plt.ylabel('Density')
plt.title('Histogram of Residuals with Normal Curve')
plt.legend()
plt.show()
