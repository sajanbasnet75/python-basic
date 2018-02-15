import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails=[]

for i in range(10000):
    tails=[0]
    for x in range(10):
        coin=np.random.randint(0,2)
        tails.append(tails[x]+coin)
    final_tails.append(tails[-1])
   
print(final_tails)
print(len(final_tails))
plt.hist(final_tails,bins=10)
plt.show()
   
'''
From this curve ,we can see that in around 2500 games of the
10000 games played we end up with 5 times the tails
'''
