from matplotlib import pyplot as plt
#draw a plot with the following values
x=[1,2,3,4]
y=[1,2,3,4]

#setting the marker properties
plt.plot(x,y,marker="*")

#mec stands for marker edge color
#mfc stands for marker face color
plt.plot(x,y,marker="o",mec="red",mfc="black")
plt.show()
