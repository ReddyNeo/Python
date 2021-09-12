""" Exporting Text From file system
file = open("C:/Users/Veeru/Desktop/pytho.txt",'a')
print(file.write("\n Welcome nithya for the python course "))
file.close() """
"""
file = open("C:/Users/Veeru/Desktop/pytho1.txt",'x')
print(file.write(" Hi team Welcome nithya for the python course "))
file.close() """
#Lambda function
"""
def a (x):
    return(lambda y:x+y)
j=a(5)
print(j(4))
"""
#Lambda with in filter
"""mylist=[2,4,6,6,7,12,30,34]
newlist = list(filter(lambda a:(a/3==2),mylist))
print(newlist)
import abc
print(dir(abc))"""
'''
import math
print(math.factorial(4))'''
'''
from statistics import *
print(mean([1,2,1,2,1,45,5,4,6,5,2,5]))
print(median([1,2,1,2,1,45,5,4,6,5,2,5]))
print(mode([1,2,1,2,1,45,5,4,6,5,2,5]))
print(variance([1,2,1,2,1,45,5,4,6,5,2,5])) '''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
ax = sns.boxplot(tips["total_bill"])


