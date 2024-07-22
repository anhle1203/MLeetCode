# Principal Component Analysis (PCA) Implementation (Medium)

Write a Python function that performs Principal Component Analysis (PCA) from scratch. The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. The function should standardize the dataset, compute the covariance matrix, find the eigenvalues and eigenvectors, and return the principal components (the eigenvectors corresponding to the largest eigenvalues). The function should also take an integer k as input, representing the number of principal components to return.

# Learn
Principal Component Analysis (PCA) utilizes the concept of eigenvalues and eigenvectors to identify the principal components of a dataset. Here's how eigenvalues fit into the PCA process:
Eigenvalues and Eigenvectors: The Foundation of PCA
For a given square matrix $A$, representing $\lambda$ the covariance matrix in PCA, eigenvalues and their corresponding eigenvectors $v$ satisfy:

**$A*v$ = $\lambda * v$**

## Calculating Eigenvalue
The eigenvalues of matrix $A$ are found by solving the characteristic equation:
$det(A- \lambda * I) = 0 $

## Role in PCA
In PCA, the covariance matrix's eigenvalues represent the variance explained by its eigenvectors. Thus, selecting the eigenvectors associated with the largest eigenvalues is akin to choosing the principal components that retain the most data variance.

## Eigenvalues and Dimensionality Reduction
The magnitude of an eigenvalue correlates with the importance of its corresponding eigenvector (principal component) in representing the dataset's variability. By selecting a subset of eigenvectors corresponding to the largest eigenvalues, PCA achieves dimensionality reduction while preserving as much of the dataset's variability as possible.

## Practical Application
1. Standardize the Dataset: Ensure that each feature has a mean of 0 and a standard deviation of 1.
2. Compute the Covariance Matrix: Reflects how features vary together.
3. Find Eigenvalues and Eigenvectors: Solve the characteristic equation for the covariance matrix.
4. Select Principal Components: Choose eigenvectors (components) with the highest eigenvalues for dimensionality reduction.

Through this process, PCA transforms the original features into a new set of uncorrelated features (principal components), ordered by the amount of original variance they explain.
