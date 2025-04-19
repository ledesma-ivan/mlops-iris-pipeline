from sklearn.datasets import load_iris
data = load_iris()

name = 'iris_dataset.xslx'
data.to_excel(name)
