from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

iris = datasets.load_iris()

plt.figure(figsize=(12,6))
plt.title("Cluster Hierárquico: Dendograma")
plt.xlabel("Índice")
plt.ylabel("Distância")
linkage_matrix = linkage(iris.data, method='ward')
dendrogram(linkage_matrix, truncate_mode='lastp', p=15)
plt.axhline(y=7, c='gray', lw=1, linestyle='dashed')
plt.show()
