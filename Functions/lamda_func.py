raise_power=lambda x,y:print(x**y)
raise_power(2,3)

'''
MAP:
One of the common things we do with list and other
sequences is applying an operation to each item and collect the result.

The map(aFunction, aSequence) function applies a passed-in function to
each item in an iterable object
and returns a list containing all the function call results.
'''

nums=[1,2,3,4,5]
def squ(x):
    return x**2
print(list(map(squ,nums)))


'''
---------------------------------------------------------------------------------------------
Because map expects a function to be passed in, it also happens to be
one of the places where lambda routinely appears:
'''

print("using lambda : \n"+str(list(map(lambda x:x**2,nums))))

'''
--------------------------------------------------------------------------------------------
Filter and lambda function
The function filter() offers a way to filter out elements from a list that
don't satisfy certain criteria.
wap to Create, from an input list of strings, a new list that contains
only strings that have more than 6 characters.
'''
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda x:len(x)>6,fellowship)

# Convert result to a list: result_list
result_list=list(result)

# Convert result into a list and print it
print(result_list)

'''
-------------------------------------------------------------------------
Reduce and lambda function
The reduce() function is useful for performing some computation on a list and,
unlike map() and filter(), returns a single value as a result.
To use reduce(), you must import it from the functools module.
'''
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda x,y:x+y, stark)

# Print the result
print(result)

