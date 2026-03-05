# Calls per hour 
# Random events in fixed time
# Avg 5 calls per hour
# 1000 hours simulate

import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

data=np.random.poisson(lam=5, size=1000)
sns.histplot(data, bins=10)
plt.show()