from matplotlib import pyplot as plt
#draw a plot with the following values
x=[1,2,3,4]
y=[1,2,3,4]
plt.plot(x,y)

#setting the line properties
plt.plot(x,y,ls="dotted",lw=4,c="black")
#another way
#plt.plot(x,y,ls=":")

plt.show()