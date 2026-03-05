# # youtube views 
# top video=max views
# baake sb= kam 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
data= np.random.zipf(a=2,size=1000)
sns.histplot(data, bins=50)
plt.show()