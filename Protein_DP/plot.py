import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import csv

def kmeans_clustering(data, num_clusters):
    # Perform k-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(data)

    # Get cluster centers and labels
    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    # Return cluster centers and labels
    return cluster_centers, labels

def visualize_clusters(data, cluster_centers, labels, data_labels=None):
    # Scatter plot of the data points with different colors for each cluster
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=10)

    # Plot cluster centers
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='X', s=10, c='red', label='Cluster Centers')


    # Add text labels for each data point
    for i, row in enumerate(data_labels):
        for j, label in enumerate(row):
            plt.text(data[i][j], 0, f'{label}', fontsize=10, ha='center', va='bottom')

    plt.title('K-Means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    # # Limit x and y-axis to a range of 50
    # plt.xlim(50, 75)
    # plt.ylim(0, 40)
    plt.show()

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Skip the header if it exists
        # next(csv_reader)
        
        for row in csv_reader:
            data.append(row)

    return data

def get_data(csv_file_path = 'scores.csv'):
    # Specify the file path
    # csv_file_path = 'scores.csv'
    # csv_file_path = 'scores_rho_0.3.csv'

    # Read from CSV
    csv_data = read_csv(csv_file_path)

    data = []
    index = []
    # Print the data
    for i, row in enumerate(csv_data):
        row_data = []
        row_index = []
        for j, cell in enumerate(row):
            if(cell == ''):
                row_data.append(0)
                # continue
            else:
                row_data.append(float(cell))
                row_index.append(str((i, j)))
        data.append(row_data)
        index.append(row_index)
        # print(row_data)
    # print(data)

    data = np.array(data)
    index = np.array(index)
    
    # rows, cols = data.shape
    # for i in range(rows):
    #     for j in range(i + 1, cols):
    #         data[j, i] = data[i, j]
            
    # print(data)
    
    return data, index

def main():
    data, index = get_data()
    # Number of clusters
    k = 5

    # Perform k-means clustering
    cluster_centers, labels = kmeans_clustering(data, k)

    # Visualize clusters
    visualize_clusters(data, cluster_centers, labels, index)

    # # Print results
    # print("Original Data:")
    # print(data)
    # print("Cluster Centers:")
    # print(cluster_centers)
    # print("Labels:")
    # print(labels)

if __name__ == "__main__":
    main()
