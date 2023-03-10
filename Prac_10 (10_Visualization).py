# -*- coding: utf-8 -*-
"""Prac_10 (10 Visualization).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PcvteumEzX8goZyxLrs2FXx8umKXB6Gd
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import seaborn as sns

df=pd.read_csv("prac_1.csv")

df.head(5)

sns.countplot(data=df,x='Sex')

sns.countplot(data=df,x='Sex',hue='Age')

ax=df.plot(figsize=(18,12), title='Passenger Info')

df['Survived'].plot(kind='bar')

df['Age'].plot(kind='hist')

df.plot.bar()

df.plot.hist()

df.plot.scatter(x='Sex',y='Age')

df.plot.hexbin(x='PassengerId',y='Survived', gridsize=5)

