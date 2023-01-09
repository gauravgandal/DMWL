# -*- coding: utf-8 -*-
"""Prac - 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q3mWELy37SnkBEtJid1hjeR5xX7d4ktR
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

df = pd.read_csv('prac_1.csv')

"""# New Section"""

df

#Finding Null values
df.isnull()

#Sum of Null values
df.isnull().sum()

df.shape

df.info

#Visualization of Unprocessed data
#1. Histogram

df.hist()

#2. Barplot
sea.barplot(df['Sex'], df['Age'])
plt.title('BarPlot')

#3. Pie Chart
labels=['Age','Sex','PassengerId']
sizes=[50,50,50]
plt.pie(sizes,labels=labels,explode=(0.1,0.1,0.1))

#4. Count Plot
sea.countplot(x='Age', data=df)
plt.title('Count for Age')

#5.  Box Plot
sea.boxplot(data=df, orient='h')
plt.title("Box Plot")

#6. JointPlot
sea.jointplot(x='Age', y='Sex', kind = 'scatter', data=df)

#Preprocessing.
df.isnull().sum()

#Filling Missing Valus of Age Column
df['Age']=df['Age'].fillna(df['Age'].mode()[0])
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Cabin']=df['Cabin'].fillna(df['Cabin'].mode()[0])

df.isnull().sum()

df

#Visualization for Processed Data
#1. Histogram
df.hist()

#2. BarPlot
sea.barplot(df['Sex'],df['Age'])

#3. PieChart
labels=('Age','Sex','PassengerId')
sizes=(50,50,50)
plt.pie(sizes, labels=labels,explode=(0.1,0.1,0.1))

#Countplot
sea.countplot(x='Age',data= df)

#JointPlot
sea.jointplot(x='Age',y='Sex',kind='scatter',data=df)

