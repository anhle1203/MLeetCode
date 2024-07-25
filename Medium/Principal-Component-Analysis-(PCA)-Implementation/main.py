import numpy as np

def pca(data: np.ndarray, k: int) -> list[list[int | float]]:
    """
    Perform PCA on the given data and return the top k principal components.

    Parameters:
    data (np.ndarray): The input data matrix (m x n), where m is the number of samples and n is the number of features.
    k (int): The number of principal components to return.

    Returns:
    list[list[int | float]]: The top k principal components as a list of lists.
    """
    # Step 1: Center the data by subtracting the mean of each feature
    mean_vector = np.mean(data, axis=0)
    centered_data = (data - mean_vector) / np.std(data, axis = 0)

    # Step 2: Compute the covariance matrix of the centered data
    covariance_matrix = np.cov(centered_data, rowvar=False)

    # Step 3: Compute the eigenvalues and eigenvectors of the covariance matrix
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    # Step 4: Sort the eigenvalues and corresponding eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # Step 5: Select the top k eigenvectors (principal components)
    principal_components = sorted_eigenvectors[:, :k]

    return np.round(principal_components, 4).tolist()


# Example
data = np.array([
    [4, 2, 1],
    [5, 6, 7],
    [9, 12, 1],
    [4, 6, 7]
])
k = 2  # Number of principal components to return

# Perform PCA
principal_components = pca(data, k)

# Print the top k principal components
print("Top k Principal Components:")
for pc in principal_components:
    print(pc)

expected = [[0.6855, 0.0776], [0.6202, 0.4586], [-0.3814, 0.8853]]
print("Expected:")
for expect in expected:
    print(expect)