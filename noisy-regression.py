import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)
x_values = np.linspace(-2, 5, 100)
y_values = 0.5 * x_values**3 - 2 * x_values**2 + x_values + np.random.normal(0, 2, 100)

# Create polynomial features
def create_polynomial_features(x_values, degree):
    polynomial_features = np.column_stack([x_values**i for i in range(1, degree+1)])
    polynomial_features = np.hstack([np.ones((len(x_values), 1)), polynomial_features])
    return polynomial_features

degree = 4
polynomial_features = create_polynomial_features(x_values, degree)

# Train the model
coefficients = np.linalg.inv(polynomial_features.T @ polynomial_features) @ polynomial_features.T @ y_values

# Predict
predicted_values = polynomial_features @ coefficients

# Evaluate
mse = np.mean((predicted_values - y_values)**2)
r2 = 1 - np.sum((y_values - predicted_values)**2) / np.sum((y_values - np.mean(y_values))**2)
print(f"MSE: {mse:.2f}, R²: {r2:.2f}")

# Add noise to the data
noisy_y_values = y_values + np.random.normal(0, 1, 100)

# Re-train the model with noisy data
noisy_coefficients = np.linalg.inv(polynomial_features.T @ polynomial_features) @ polynomial_features.T @ noisy_y_values

# Predict with noisy data
noisy_predicted_values = polynomial_features @ noisy_coefficients

# Evaluate with noisy data
noisy_mse = np.mean((noisy_predicted_values - noisy_y_values)**2)
noisy_r2 = 1 - np.sum((noisy_y_values - noisy_predicted_values)**2) / np.sum((noisy_y_values - np.mean(noisy_y_values))**2)
print(f"Noisy MSE: {noisy_mse:.2f}, Noisy R²: {noisy_r2:.2f}")

# Visualize noisy data and predictions
plt.scatter(x_values, noisy_y_values, label='Noisy Data', color='blue')
plt.plot(x_values, noisy_predicted_values, label=f'Degree {degree} Noisy Fit', color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
