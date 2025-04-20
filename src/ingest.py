from sklearn.datasets import load_iris
import pandas as pd

# Cargo el dataset
data = load_iris()

# Convierto en dataframe
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Guardo en formato Excel
name = 'mlops-iris-pipeline\data/iris_dataset.xlsx'
df.to_excel(name, index=False) 
