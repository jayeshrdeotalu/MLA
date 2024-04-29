

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

X = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
Y = [21, 19, 24, 17, 16, 25, 24, 22, 21 ,21]
X, Y

plt.figure(figsize = (4, 3))
plt.scatter(X, Y);

data = list(zip(X, Y))
linkage_data = linkage(data, method = 'ward', metric = 'euclidean')
plt.figure(figsize = (4, 3))
dendrogram(linkage_data);

hierarchical_cluster = AgglomerativeClustering(n_clusters = 2, metric = 'euclidean', linkage = 'ward')
labels = hierarchical_cluster.fit_predict(data)

plt.figure(figsize = (4, 3))
plt.scatter(X, Y, c = labels);
