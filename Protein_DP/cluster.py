import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from plot import get_data
from tao_test import calculate_tpr_and_fpr

def process_one_file(filename, k, plot = 0):
    # Assuming 'data_matrix' is your matrix of numbers
    # Replace this with your actual data
    # data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    data_matrix, index = get_data(csv_file_path=filename)
    # Specify the number of clusters (k)


    # Standardize the data before clustering
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_matrix)

    # Create a KMeans instance
    kmeans = KMeans(n_clusters=k, random_state=42)

    # Fit the model to your scaled data
    kmeans.fit(scaled_data)

    # Get the labels assigned to each row
    labels = kmeans.labels_

    # Create a DataFrame for the clustered data
    import pandas as pd
    clustered_data = pd.DataFrame(data_matrix)

    # Adding a column for the cluster labels
    clustered_data['Cluster'] = labels

    # # # Set the figure size
    # plt.figure(figsize=(10, 20))
    if(plot == 1):
        clustermap = sns.clustermap(
            clustered_data.iloc[:, :-1],
            col_cluster=False,
            cmap='viridis',
            figsize=(12, 16),
            # row_labels=clustered_data.index,  # Use the DataFrame index as row labels
            
        )
        # sns.clustermap()
        # # # Label every row with its index
        # # clustermap.ax_heatmap.set_yticklabels(clustered_data.index)
        # clustermap.ax_heatmap.set_axis_off()
        # plt.show()
        
        plt.savefig("rho_0.3_k_4_t.png")

    clusters = []
    print(filename)
    print("Rows within each cluster:")
    for cluster_label in clustered_data['Cluster'].unique():
        cluster_rows = clustered_data.index[clustered_data['Cluster'] == cluster_label]
        print(f"Cluster {cluster_label}:", cluster_rows.tolist())
        clusters.append(cluster_rows.tolist())

    (tpr, fpr) = calculate_tpr_and_fpr(clusters)
    print("tpr:", tpr, "fpr:", fpr)
    return (tpr, fpr)
    
    
def main():
    filenames = [
                "scores_rho_0.05_2.csv",
                "scores_rho_0.1_2.csv",
                 "scores_rho_0.15_2.csv",
                 "scores_rho_0.2_2.csv",
                 "scores_rho_0.25_2.csv",
                 "scores_rho_0.3_2.csv",
                 "scores_rho_0.35_2.csv",
                 "scores_rho_0.4_2.csv",
                 "scores_rho_0.45_2.csv",
                 "scores_rho_0.5_2.csv",
                 "scores_rho_0.55_2.csv",
                 "scores_rho_0.6_2.csv",
                 ]
    f = open("accuracy.txt", "w")
    for k in range(3, 10):
        print("k", k)
        f.write("k="+str(k)+"\n")
        for fn in filenames:
            t = process_one_file(fn, k)
            f.write(fn+": " + str(t)+"\n")
    f.close()
    
    
def plot_one():
    fn = "scores_rho_0.3_2_t.csv"
    k=4
    t = process_one_file(fn, k, 1)
plot_one()
# main()

# print(sklearn.__version__)