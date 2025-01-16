'''
El fichero “titanic.csv” contiene información sobre los pasajeros del Titanic. Crear
un dataframe con Pandas y a partir del mismo, generar los siguientes diagramas:

1. Diagrama de Sectores con los fallecidos y supervivientes
2. Histograma con las edades
3. Diagrama de Barras con el número de personas en cada clase
4. Diagrama de Barras con el número de personas fallecidas y
supervivientes en cada clase.
5. Diagrama de Barras con el número de personas fallecidas y
supervivientes acumuladas en cada clase.
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('titanic.csv')

# 1. Diagrama de Sectores con los fallecidos y supervivientes
survived = df['Survived'].value_counts()
plt.pie(survived, labels=['Died', 'Survived'], autopct='%1.1f%%')
plt.title('Survival Rate')
plt.show()

# 2. Histograma con las edades
plt.hist(df['Age'], bins=30, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

# 3. Diagrama de Barras con el número de personas en cada clase
plt.bar(df['Pclass'].value_counts().index, df['Pclass'].value_counts().values)
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.title('Number of Passengers in Each Class')
plt.show()

# 4 y 5 Diagrama de Barras con el número de personas fallecidas y supervivientes en cada clase.
df_class = df.groupby(['Pclass', 'Survived']).size().unstack()
df_class.plot(kind='bar',color=["orange","green"], stacked=True)
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.title('Number of Passengers Survived and Died in Each Class')
plt.show()
