import random 
rolls=int(input("Number of rolls: "))
results=[]

for _ in range(rolls):
    results.append(random.randint(1,6 ))

print("\n--- Dice Statistics ---")
for i in range(1, 7):
    freq=results.count(i)
    prob=freq/rolls
    print(f'{i}:{freq} time | Probability:{prob:2f}')