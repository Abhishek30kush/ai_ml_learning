import random
import matplotlib.pyplot as plt
import seaborn as sns
# Roll dice
n=10000
results=[random.randint(1,6) for _ in range(n)]

# plot using seaborn
sns.histplot(results, bins=6, discrete=True)

plt.title("Uniform distribution -Dice Rolling (seaborn)")
plt.xlabel("Dice Number")
plt.ylabel("Frequency")
plt.xticks([1, 2, 3, 4, 5, 6])
plt.show()
