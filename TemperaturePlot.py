import pandas as pd
from matplotlib import pyplot as plt
df=pd.DataFrame({"Days":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"week-1":[27,29,32,33,33,31],"week-2":[29,30,31,33,34,31],"week-3":[29,28,25,27,31,30]})
print(df)

#plot
plt.plot(df["Days"],df["week-1"],lw=6,c="red",marker="o")
plt.plot(df["Days"],df["week-2"],lw=6,c="green",marker="X")
plt.plot(df["Days"],df["week-3"],lw=6,c="black",marker="*")
plt.xlabel("WEEK DAYS",fontdict={"family":"Arial","color":"blue","size":15})
plt.ylabel("TEMP",fontdict={"family":"Arial","color":"blue","size":20})
plt.title("TEMP IN 3 WEEK DAYS",fontdict={"family":"Arial","color":"blue","size":20})
plt.legend(labels=["week1","week2","week3"])
plt.grid(axis="both",ls="dotted")


plt.show()