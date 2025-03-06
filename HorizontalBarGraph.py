import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,30,40,50]

#colors
col=["red","blue","red","blue","red"]

#Horizontal Bar plot
plt.barh(x,y,color=col,height=0.5)
plt.show()