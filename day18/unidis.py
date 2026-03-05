import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

data=np.random.uniform(1, 7, 10000)

sns.histplot(data, bins=6)
plt.show()