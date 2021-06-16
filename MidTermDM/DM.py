import numpy as np
import matplotlib.pyplot as plt

# x = np.array([2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1])
# y = np.array([2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9])

adjusted_x = np.array([0.69, -1.31, 0.39, 0.09, 1.29, 0.49, 0.19, -0.81, -0.31, -0.71])
adjusted_y = np.array([0.49, -1.21, 0.99, 0.29, 1.09, 0.79, -0.31, -0.81, -0.31, -1.01])

colors = (0, 0, 0)
area = np.pi*3

# Plot
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.scatter(adjusted_x, adjusted_y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot Adjusted data by Maaz Sabahuddin')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# import nltk
# import sklearn
#
# print('The nltk version is {}.'.format(nltk.__version__))
# print('The scikit-learn version is {}.'.format(sklearn.__version__))

# from sklearn.datasets import load_iris
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix
# from sklearn.tree import export_graphviz
# # from sklearn.externals.six import StringIO
# from six import StringIO
# from IPython.display import Image
# from pydot import graph_from_dot_data
# import pandas as pd
# import numpy as np
#
# iris = load_iris()
# X = pd.DataFrame(iris.data, columns=iris.feature_names)
# y = pd.Categorical.from_codes(iris.target, iris.target_names)
#
# y = pd.get_dummies(y)
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
#
# dt = DecisionTreeClassifier()
# dt.fit(X_train, y_train)
#
# dot_data = StringIO()
# export_graphviz(dt, out_file=dot_data, feature_names=iris.feature_names)
# (graph, ) = graph_from_dot_data(dot_data.getvalue())
# Image(graph.create_png())
