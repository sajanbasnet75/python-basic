#wap to create a list whose value is product of 2 of another list
#uisng a for loop
list1=[1,2,3,4,5]
list2=[]

for i in list1:
    list2.append(i*2)
print(list1)
print(list2)

print("using list comprehension")
list3=[i*2 for i in list1]
print(list3)

print("using in nested loops")
list4=[(i,j) for i in list1 for j in list3]
print(list4)
"-------------------------------------------------------------------------"
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
doc=[]
for i in doctor:
    doc.append(i[0])
print(doc)    

#by using list comp
docs=[]
docs.append([i[0] for i in doctor])
print ("using list comp"+str(docs))
#"-----------------------------------------------------------"
#printing 5x5 matrix
'''
[[output expression] for iterator variable in iterable]

Note that here, the output expression is itself a list comprehension.
'''
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)

"------------------------------------------------------------------------"

#condition in list comp
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member)>=7]

# Print the new list
print(new_fellowship)
new_fellowship = [member if len(member)>=7 else " " for member in fellowship]
print(new_fellowship)

"--------------------------------------------------------------------"
'''dictionary comp'''

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member:len(member) for member in fellowship }

# Print the new list
print(new_fellowship)


    
