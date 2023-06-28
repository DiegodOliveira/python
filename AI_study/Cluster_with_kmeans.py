from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

iris = datasets.load_iris()

def plot_clusters(data, labels, title):
  colors = ['red','green','purple','black']
  plt.figure(figsize=(8,4))
  for i,c,l in zip(range(-1,3), colors, ['Noise','Setosa','Versicolor','Virginica']):
    if i == -1:
      plt.scatter(data[labels == i, 0], data[labels == i, 3], c=colors[i], label=1, alpha=0.5, s=50, marker='x')
    else:
      plt.scatter(data[labels == i, 0], data[labels == i, 3], c=colors[i], label=1, alpha=0.5, s=50)
  plt.legend()
  plt.title(title)
  plt.xlabel('Comprimento da Sépala')
  plt.ylabel('Lárgura da Pétala')
  plt.show()

kmeans = KMeans(n_clusters=3,n_init='auto')
kmeans.fit(iris.data)
print(kmeans.labels_)
resultados = confusion_matrix(iris.target, kmeans.labels_)
print(resultados)

plot_clusters(iris.data, kmeans.labels_, "Cluster KMeans")
