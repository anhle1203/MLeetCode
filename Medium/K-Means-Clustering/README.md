# K-means Clustering

Write a Python function that implements the k-Means algorithm for clustering, starting with specified initial centroids and a set number of iterations. The function should take a list of points (each represented as a tuple of coordinates), an integer k representing the number of clusters to form, a list of initial centroids (each a tuple of coordinates), and an integer representing the maximum number of iterations to perform. The function will iteratively assign each point to the nearest centroid and update the centroids based on the assignments until the centroids do not change significantly, or the maximum number of iterations is reached. The function should return a list of the final centroids of the clusters. Round to the nearest fourth decimal.


# Learn 
k-Means clustering is a method to partition `n` points into `k` clusters. Here is a brief overview of how to implement the k-Means algorithm: 
1. **Initialization**: Start by selecting `k` initial centroids. These can be randomly selected from the dataset or based on prior knowledge. 
2. **Assignment Step**: For each point in the dataset, find the nearest centroid. The "nearest" can be defined using Euclidean distance. Assign the point to the cluster represented by this nearest centroid. 
3. **Update Step**: Once all points are assigned to clusters, update the centroids by calculating the mean of all points in each cluster. This becomes the new centroid of the cluster. 
4. **Iteration**: Repeat the assignment and update steps until the centroids no longer change significantly, or until a predetermined number of iterations have been completed. This iterative process helps in refining the clusters to minimize within-cluster variance. 
5. **Result**: The final centroids represent the center of the clusters, and the points are partitioned accordingly. This algorithm assumes that the `mean` is a meaningful measure, which might not be the case for non-numeric data. The choice of initial centroids can significantly affect the final clusters, hence multiple runs with different starting points can lead to a more comprehensive understanding of the cluster structure in the data.