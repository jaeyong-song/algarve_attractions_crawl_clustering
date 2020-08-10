import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns; sns.set()
import csv

X_weighted = pd.read_csv('./result.csv')


# K_clusters = range(1,10)
# kmeans = [KMeans(n_clusters=i) for i in K_clusters]
# lat_long = X_weighted[X_weighted.columns[2:4]]
# weight = X_weighted[X_weighted.columns[1]]
# sample_weight = weight
# score = [kmeans[i].fit(lat_long, sample_weight = weight).score(lat_long) for i in range(len(kmeans))]
# plt.plot(K_clusters, score)
# plt.xlabel('Number of Clusters')
# plt.ylabel('Score')
# plt.title('Elbow Curve = Weighted')
# plt.show()

kmeans = KMeans(n_clusters = 7, max_iter=1000, init ='k-means++')
lat_long = X_weighted[['longitude', 'latitude']]
lot_size = X_weighted[X_weighted.columns[1]]
weighted_kmeans_clusters = kmeans.fit(lat_long, sample_weight = lot_size) # Compute k-means clustering.
X_weighted['cluster_label'] = kmeans.predict(lat_long, sample_weight = lot_size)
centers = kmeans.cluster_centers_ # Coordinates of cluster centers.
labels = X_weighted['cluster_label'] # Labels of each point
X_weighted.plot.scatter(x = 'longitude', y = 'latitude', c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()
