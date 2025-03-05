import pandas as pd
from matplotlib import pyplot as plt
df=pd.DataFrame({"Days":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"week-1":[27,29,32,33,33,31],"week-2":[29,30,31,33,34,31],"week-3":[29,28,25,27,31,30]})
print(df)

#days with week1 plot
plt.subplot(3,1,1)    #3 rows 1 col 1 index
plt.plot(df["Days"],df["week-1"],lw=6,c="red",marker="o")
plt.title("First Week",fontdict={"family":"Arial","color":"blue","size":10})

#days with week2 plot
plt.subplot(3,1,2)
plt.plot(df["Days"],df["week-2"],lw=6,c="green",marker="o")
plt.title("Second Week",fontdict={"family":"Arial","color":"blue","size":10})

#Days with week-3
plt.subplot(3,1,3)
plt.plot(df["Days"],df["week-3"],lw=6,c="black",marker="o")
plt.title("Third Week",fontdict={"family":"Arial","color":"blue","size":10})

plt.show()