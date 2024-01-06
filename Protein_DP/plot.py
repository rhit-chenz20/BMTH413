import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def kmeans_clustering(data, num_clusters):
    # Perform k-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(data)

    # Get cluster centers and labels
    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    # Return cluster centers and labels
    return cluster_centers, labels

def visualize_clusters(data, cluster_centers, labels):
    # Scatter plot of the data points with different colors for each cluster
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')

    # Plot cluster centers
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='X', s=200, c='red', label='Cluster Centers')

    plt.title('K-Means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()

def main():
    # Example 2D array of float numbers
    data = np.array([[1.2, 2.3],
                     [2.5, 3.8],
                     [3.1, 4.2],
                     [4.8, 5.5],
                     [5.5, 6.7],
                     [6.2, 7.4],
                     [7.0, 8.1],
                     [8.3, 9.6],
                     [9.1, 10.0]])

    # Number of clusters
    k = 3

    # Perform k-means clustering
    cluster_centers, labels = kmeans_clustering(data, k)

    # Visualize clusters
    visualize_clusters(data, cluster_centers, labels)

    # Print results
    print("Original Data:")
    print(data)
    print("Cluster Centers:")
    print(cluster_centers)
    print("Labels:")
    print(labels)

if __name__ == "__main__":
    main()
