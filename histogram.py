import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#implementation of histogram
marks=np.random.randint(10,51,35)
marks_interval=np.array([10,20,30,40,50])
plt.hist(marks,marks_interval,histtype="bar",edgecolor="red")
plt.show()