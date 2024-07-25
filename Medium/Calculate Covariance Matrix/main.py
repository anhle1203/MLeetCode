def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    """
    Calculate the covariance matrix for a given list of vectors.

    Parameters:
    vectors (list[list[float]]): A list of lists, where each inner list represents a feature vector.

    Returns:
    list[list[float]]: The covariance matrix.
    """
    n_features = len(vectors)  # Number of features
    n_observations = len(vectors[0])  # Number of observations
    covariance_matrix = [[0 for i in range(n_features)] for j in range(n_features)]  # Initialize the covariance matrix with zeros

    # Calculate the mean of each feature vector
    means = [sum(feature) / n_observations for feature in vectors]

    # Calculate the covariance for each pair of features
    for i in range(n_features):
        for j in range(i, n_features):
            covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n_observations)) / (n_observations - 1)
            covariance_matrix[i][j] = covariance_matrix[j][i] = covariance  # Covariance matrix is symmetric

    return covariance_matrix


# Example 
vectors = [
    [2.1, 2.5, 3.6, 4.0],
    [8.0, 7.5, 6.7, 6.0],
    [1.1, 0.8, 0.6, 0.4]
]

# Calculate the covariance matrix
cov_matrix = calculate_covariance_matrix(vectors)

# Print the output covariance matrix
print("Covariance Matrix:")
for row in cov_matrix:
    print(row)