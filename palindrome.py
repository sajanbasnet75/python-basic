#palindrome no checker
n=int(input("enter a no :"))
print(n)
#process 1
numb=str(n)
rev_number=numb[::-1] #[begain:end:step]
print(rev_number)

# process 2 
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev)
    
