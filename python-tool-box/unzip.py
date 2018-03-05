'''
no any unzip() function but we can use * and a zip
'''
mutants=['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride']
aliases=['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers=['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']


# Create a zip object from mutants and powers: z1
z1 = zip(mutants,powers)
# Print the tuples in z1 by unpacking with *
print(*z1)

#lets store seperately

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants,powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1)
print(result2)
