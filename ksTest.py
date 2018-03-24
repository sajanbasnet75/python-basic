import numpy as np 
print("enter the value of no. of random nos:")
n=int(input())
rand_no= np.empty((n), dtype=float)
dm=np.empty((n),dtype=float)
dp=np.empty((n),dtype=float)

for i in range(n):
    rand_no[i]=input()

rand_no.sort()    
for i in range(n):
    dp[i]=((i+1)/n)-rand_no[i]
    dm[i]=rand_no[i]-(((i+1)-1)/n)
print(dp)
print(dm)
a=max(dp)
b=max(dm)
Dobt=max(a,b)
print("enter the critical value of D:")
Dcri=float(input())
Dmax=max(Dobt,Dcri)
print(Dmax)
if Dmax==Dcri:
    print("Accept Ho")
else:
    print("Accept H1")
