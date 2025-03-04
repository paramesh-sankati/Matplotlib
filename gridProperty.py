from matplotlib import pyplot as plt
import numpy as np

#to set grid property we use a pre defined function grid()
x=[1,2,3,4]
y=[4,3,2,1]

#limits
plt.xlim(0,6)
plt.ylim(0,6)

#ticks
plt.xticks([1,2,3,4])
plt.yticks([1,2,3,4])
plt.plot(x,y,marker="o",mec="red",mfc="yellow",c="red",ls="solid",lw=3,ms=5)
plt.plot(x,[3,4,2,1],marker="*",mec="red",mfc="yellow",c="blue",ls="solid",lw=3,ms=5)

#plt.grid(axis="y")
#grid lines also satisfies line properties
plt.grid(axis="both",ls="solid",c="green")

#labels
plt.xlabel("X-Axis",fontdict={"family":"arial","color":"blue","size":15})
plt.ylabel("Y-Axis",fontdict={"family":"arial","color":"blue","size":15})

#title
plt.title("Line Plot",fontdict={"family":"Times New Roman","size":15})

#legend
plt.legend(labels=["India","Aus"])
plt.show()