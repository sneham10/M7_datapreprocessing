from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

df1 = pd.read_csv('cleaned1.csv')

x = df1['Units Sold']
y = df1['Total Profit']
plt.subplot(1,2,1)
plt.plot(x,color='r')
plt.title("Unit Sold")


plt.subplot(1,2,2)
plt.plot(y,color='b')
#title for plot
plt.title("total profit")
#over all title
plt.suptitle("comparison of unit sold and profit")
plt.show()


a=df1['year']
b=df1['Sales Channel']
plt.bar(a,b,color=['r','b'])
plt.suptitle("Sales Channel calculation over 2010-2017")
plt.show()

b=df1['Order Priority']
plt.suptitle("order priority")
plt.hist(b)
plt.legend()
plt.show()

