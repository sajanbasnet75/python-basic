
n=input("enter a no :")
no=int(n)
for i in range(no+1):
    if i>1:
        if no%i==0:
            if i!=no:
                print("its not a prime")
                break

            elif i==no:
                print("its a prime")
                break
                
