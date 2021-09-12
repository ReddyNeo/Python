import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
#a = sns.load_dataset("flights")
#sns.relplot(x="passengers", y="month",hue="year", data=a) #Working in python console
#sns.catplot(x="passengers", y="month",hue="year", data=a) #Working in python console
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
b = sns.load_dataset("tips") #Working in python console
sns.relplot(x='time', y='tip', data=b, kind="line")
sns.catplot(x="day", y="total_bill", kind='violin',data=b) #after Adding kind = violin its got changed
sns.catplot(x="day", y="total_bill", kind='boxen',data=b) #after Adding kind = boxen its got changed
'''
# ========================================

'''
a=sns.load_dataset("iris")
b=sns.FacetGrid(a,col="species")
b.map(plt.hist, "sepal_length")
'''
# =============================================
#sns.set(style="dark")
'''a = sns.load_dataset("flights")
b = sns.PairGrid(a)
b.map(plt.scatter)'''
c = sns.color_palette()
sns.palplot(c)
