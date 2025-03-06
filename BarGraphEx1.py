import matplotlib.pyplot as plt
x=[2,7,1,6,3,4,2]      #No.Of students
y=[4.5,5.5,6.5,6.0,3.5,2.5,6.2]    #heights of students
#colors to bars
col=["red","blue","red","blue","red","blue","red"]

plt.bar(x,y,width=0.4,color=col)
plt.show()