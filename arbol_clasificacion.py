import pandas as pd
import numpy as np
import datetime
import joblib
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv("dataset_products.csv", delimiter=',')

print("Mostrar las primeras 5 filas del dataset")

print(df.head(5))

print("Comprobando si hay valores vacios")

print(df.isnull().sum())

df.Name.replace(np.nan,'Sardinas', inplace = True)

df.Sale_date.replace(np.nan,'6/1/2022', inplace = True)

df["Unit_price"] = pd.to_numeric(df["Unit_price"].str.replace('$', ''))

df.Unit_price.replace(np.nan,15000, inplace = True)

df.Quantity.replace(np.nan,120, inplace = True)


print("Comprobando si hay valores vacios de nuevo")

print(df.isnull().sum())

print("Visualizamos de nuevo el dataframe")

print(df.head(10))

df['Quantity'] = df['Quantity'].astype(int)

df['Unit_price'] = df['Unit_price'].astype(int)

print("Vemos los tipos de datos")

print(df.dtypes)

df['Total'] = df['Unit_price'] * df['Quantity']

print("Creamos una nueva columna llamada Total")

print(df.head(10))


condition =[
    (df['Quantity'] <= 250),
    (df['Quantity'] > 250) & (df['Quantity'] <= 350),
    (df['Quantity'] > 350)
]

opcions = ['Less','Normal', 'More']
df['Decision'] = np.select(condition, opcions)
df['Decision'].value_counts()

print("ver la nueva columna de decisión")

print(df.head(10))

#Algoritmo de Arbol de decisión

decision = preprocessing.LabelEncoder()
df['Decision'] = decision.fit_transform(df['Decision'] )

name = preprocessing.LabelEncoder()
df['Name'] = name.fit_transform(df['Name'] )

list(decision.inverse_transform([0,1,2]))

list(name.inverse_transform([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]))

print("Vemos el cambio en la columna Name y Decision")

print(df.head(20))

X = df[['Name','Unit_price','Quantity','Total']].values
y = df['Decision'].values

X_ent, X_pru, y_ent, y_pru = train_test_split(X, y,random_state = 1)

tree = DecisionTreeClassifier(criterion='gini', max_depth=20, random_state=1)
tree.fit(X, y)

print("Exactitud del conjunto de entrenamiento: {:.2f}".format(tree.score(X_ent, y_ent)))
print("Exactitud del conjunto de prueba: {:.2f}".format(tree.score(X_pru, y_pru)))

test = np.array([25,33567,404,13561241])
predict = tree.predict(test.reshape(1 , -1))
predict

if predict[0] == 0:
    print("Less")
elif predict[0] == 1:
    print("More")
elif predict[0] == 2:
    print("Normal")

joblib.dump(tree, "model.pkl")
print("El modelo ha sido exportado")

