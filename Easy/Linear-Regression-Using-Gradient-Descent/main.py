import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Parameters:
    X (np.ndarray): The input features matrix (m x n), where m is the number of samples and n is the number of features.
    y (np.ndarray): The target values vector (m x 1), where m is the number of samples.
    alpha (float): The learning rate.
    iterations (int): The number of iterations to perform gradient descent.

    Returns:
    np.ndarray: The learned parameters (n x 1), rounded to 4 decimal places.
    """
    m, n = X.shape  # Get the number of samples (m) and number of features (n)
    theta = np.zeros((n, 1))  # Initialize the parameters (theta) to zeros
    
    # Perform gradient descent for the specified number of iterations
    for _ in range(iterations):
        predictions = X @ theta  # Compute predictions (X * theta)
        errors = predictions - y.reshape(-1, 1)  # Calculate the errors (predictions - actual values)
        updates = X.T @ errors / m  # Compute the gradient updates
        theta -= alpha * updates  # Update the parameters using the learning rate (alpha)
    
    return np.round(theta.flatten(), 4)  # Return the learned parameters rounded to 4 decimal places


# Example
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000

output = np.array([0.1107, 0.9513])
# reasoning: The linear model is y = 0.0 + 1.0*x, which fits the input data after gradient descent optimization.
result = linear_regression_gradient_descent(X,y,alpha,iterations)

print("Expected:", output)
print("Actual: ", result)
