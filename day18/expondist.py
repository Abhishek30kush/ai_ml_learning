# User Retention Time 
# User kab app chod dega? 

# most users jaldi quit
# kuch bahut der tak

import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

data=np.random.exponential(scale=2, size=1000)
sns.histplot(data, bins=30)
plt.show()