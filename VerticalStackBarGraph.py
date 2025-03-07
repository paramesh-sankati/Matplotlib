import matplotlib.pyplot as plt
year=["2021","2022","2023","2024"]
placements=[150,175,125,100]
cse=[80,95,65,50]
it=[30,35,12,6]

#plot
plt.bar(year,cse,color="red",label="CSE")
plt.bar(year,it,bottom="cse",color="blue",label="IT")
plt.legend()
plt.show()