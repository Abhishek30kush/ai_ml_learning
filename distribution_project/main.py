import seaborn as sns
import matplotlib.pyplot as plt
from distribution import * 
print("""
1. Uniform (Dice) 
2. Normal (Marks)
3. Binomial (Ad Click)
4. Poisson(Calls)
5. Exponential (Retentions)
6. Multinomial (Election)
7. Pareto(Wealth)
8. Zipf (views)    
""")

choice=int(input("Select distribution:"))

data=None
title=""

if choice==1:
    data=uniform_dist()
    title="Dice Uniform Distribution"
elif choice==2:
    data=normal_dist()
    title="Student Marks Distribution"
elif choice==3:
    data=binomial_dist()
    title="Marketing click distribution"
elif choice==4:
    data=poisson_dist()
    title="Call Center Load"
elif choice==5: 
    data=exponential_dist()
    title="User Retention"
elif choice==6:
    data=multinomial_dist()
    print("Votes:", data)
    exit()
elif choice==7:
    data=pareto_dist()
    title="Wealth Distribution"
elif choice==8:
    data=zipf_dist()
    title="Video Views"
print("Mean:", data.mean())
print("Std Dev: ", data.std())
sns.histplot(data, bins=30)
plt.title(title)
plt.show()