#iterate over dictionary

europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
          
# Iterate over europe
for x, y in europe.items():
    print("the capital of "+str(x)+" is "+str(y))
