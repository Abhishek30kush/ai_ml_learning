import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

data=np.random.multinomial(10000, [0.4, 0.35, 0.25]) #3 parties, 1000 voters
print("party A, B, C votes:", data)