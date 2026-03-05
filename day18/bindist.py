# ad clicks

import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

data= np.random.binomial(n=10, p=0.5, size=1000) #10 trials, 50% success chance, 1000 experiments 

sns.histplot(data, bins=10)
plt.show()