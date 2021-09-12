import matplotlib.pyplot as plt
#from matplotlib import pyplot plt
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",color='b', width= .5)
plt.bar([0.25,1.05,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",color= 'g', width= .5)
plt.legend()
plt.xlabel("Days")
plt.ylabel("Distance (KM's)")
plt.title("Information")
plt.show()

#PieChart
days=[1,2,3,4,5]
Sleeping=[7,8,6,11,7]
Eating=[2,3,4,3,2]
Working=[7,8,7,2,2]
Playing=[8,5,7,8,13]
Slices=[7,2,2,13]
Activities=["Sleeping","Eating","Working","Playing"]
cols = ['g','c','gray','y']
plt.pie( Slices, labels = Activities,colors=cols,startangle= 90,shadow=True,explode=(0,0.1,0,0),autopct='%1.1f%%')
plt.title("PIE PLOT")
plt.show()