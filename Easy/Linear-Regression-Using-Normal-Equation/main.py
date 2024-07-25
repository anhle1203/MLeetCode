import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Convert to numpy array for matrix calculation
    X = np.array(X)
    y = np.array(y).reshape(-1,1)

    #Find transposed matrix
    X_T = X.T
    
    '''
    np.linalg.inv(): find inverse function
    np.dot(): find dot product between two matrix
    np.round(): round theta to nearest 4th digit in the decimal.
    flatten(): convert matrix to 10-d array
    tolist(): convert array to list
    '''
    theta = np.linalg.inv(X_T.dot(X)).dot(X_T).dot(y)
    theta = np.round(theta,4).flatten().tolist()
    return theta


# Example:
#input: 
X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]
# output: [-0.0, 1.0]

result = linear_regression_normal_equation(X,y)

print("Expected: [0.0, 1.0]")
print("Output: ", result)

print("---------------------------------------")

# Example 2:
print("Expected: [4.0, -1.0, -0.0]")
print("Output: ", linear_regression_normal_equation([[1, 3, 4], [1, 2, 5], [1, 3, 2]], [1, 2, 1]))
