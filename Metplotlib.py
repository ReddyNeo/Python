from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")

x= [1,8,6]
y=[6,4,3]

x2=[5,2,6]
y2=[3,5,7]
plt.plot(x,y,'g',label='Line1',linewidth=5)
plt.plot(x2,y2,'y',label='Line2',linewidth=5)
plt.title("INFO")
plt.ylabel("Yaxis")
plt.xlabel("Xaxis")
plt.grid(True,color='k')
plt.legend()
plt.show()