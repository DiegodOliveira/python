# Importe as bibliotecas necessárias
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Carregue o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

# Divida o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Crie um modelo de árvore de decisão binária
clf = DecisionTreeClassifier(max_depth=2)

# Treine o modelo com o conjunto de dados de treinamento
clf.fit(X_train, y_train)

# Faça previsões com o conjunto de dados de teste
y_pred = clf.predict(X_test)

# Calcule a precisão do modelo
accuracy = clf.score(X_test, y_test)

# Crie o gráfico da árvore de decisão
plt.figure(figsize=(10, 8))
plot_tree(clf, filled=True)
plt.show()

# Exiba a precisão do modelo
print("Precisão:", accuracy)
