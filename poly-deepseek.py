import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate synthetic data
np.random.seed(0)
x = np.linspace(0, 5, 100)
y = 0.5 * x**3 - 2 * x**2 + x + np.random.normal(0, 2, 100)

# Step 2: Create polynomial features (degree=n)
def create_poly_features(x, degree):
    X = np.column_stack([x**i for i in range(1, degree+1)])
    X = np.hstack([np.ones((len(x), 1)), X])  # Add intercept term (β₀)
    return X

degree = 2
X_poly = create_poly_features(x, degree)

# Step 3: Train the model (solve β)
beta = np.linalg.inv(X_poly.T @ X_poly) @ X_poly.T @ y

# Step 4: Predict
y_pred = X_poly @ beta

# Step 5: Visualize
plt.scatter(x, y, label='Data', color='green')
plt.plot(x, y_pred, label=f'Degree {degree} Fit', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Step 6: Evaluate
mse = np.mean((y_pred - y)**2)
r2 = 1 - np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2)
print(f"MSE: {mse:.2f}, R²: {r2:.2f}")