#a progrm that simulates a random walk taken when a dice is thrown
#if dice=1,2 step=step-1
#if dice=3,4,5 step=step+1
#if dice=6 roll dice again and step=outcome of rolled dice
#plot it in a graph
#simulate multiple walks
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
all_walks=[]
np.random.seed(123)
for i in range(100):
    random_walk=[0]
    for x in range(100):
        step=random_walk[-1]
        dice=np.random.randint(1,7)
        if dice<=2:
            step=max(0,step-1) #to not decrease less then 0
        elif dice<=5:
            step=step+1
        else:
            step=step+np.random.randint(1,7)
        if np.random.rand()<=0.001 :
            step = 0    
        random_walk.append(step)
    #print("this is "+str(i)+"th walk") 
    #print(random_walk)
    all_walks.append(random_walk)
print(len(all_walks))
np_array=np.array(all_walks)

np_array_transpose=np.transpose(np_array)
print(np_array)
print("transposed")
print(np_array_transpose)
print("transposed ends")
print(np_array_transpose[-1])
plt.plot(np_array_transpose)


plt.xlabel("index")
plt.ylabel("steps")
plt.title("Random Walk Graph")
plt.show()        
plt.hist(np_array_transpose[-1])
plt.show()

'''
The histogram was created from a Numpy array np_array_transpose[-1],
that contains 500 integers.
Each integer represents the end point of a random walk.
To calculate the chance that this end point is greater than or equal to 60,
you can count the number of integers in ends that are greater than or equal to 60 and divide that number by 500,
the total number of simulations.
'''
print(str(np.mean(np_array_transpose[-1]>=60)*100)+"% of chance")


