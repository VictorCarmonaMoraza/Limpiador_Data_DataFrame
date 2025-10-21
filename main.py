import pandas as pd

# Load the dataset
df = pd.read_csv(r"files/data.csv", encoding='ISO-8859-1', delimiter=',')
df.columns = df.columns.str.strip()
##Imprinme las primeras cinco filas
print(df.head())

# columnas y filas del dataframe
print(df.shape)

## Data types
print(df.dtypes)

#Estadisticas resumidas
print(df.describe())

##Obtener los valores faltantes de cada una de las columnas
print(df.isnull().sum())

#Rellenar valores faltante
df["age"]=df["age"].fillna(40)

##Borra la fila con valores vacios
df = df.dropna()

##Comporbar cuantos duplicodos tenemos
print(df.duplicated().sum())

#Eliminar valores duplicaods
print(df.drop_duplicates())

#Renombra columnas
df =df.rename(columns={'age':'edad'})

#Transformacion de datos
df["name"]=df["name"].str.upper()

#Normalizar datos numericos
df["edad"] = (df["edad"] - df["edad"].mean()) / df["edad"].std()

print(df.head())
