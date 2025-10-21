import pandas as pd

# Load the dataset
df = pd.read_csv(r"files/data.csv", encoding='utf-8-sig', delimiter=',')

##Imprinme las primeras cinco filas
print(df.head())
