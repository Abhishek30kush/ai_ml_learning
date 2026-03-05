import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
# wealt distribution
data=np.random.pareto(a=2, size=1000)
sns.histplot(data, bins=50)
plt.show() 

# long tail -> rich people