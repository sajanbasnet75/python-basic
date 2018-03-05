'''
Its same as list comp except the use of brackets insted of [] it uses ()
'''
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths =(len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)
"-------------------------------------------------"
print("using function and yield insted of return")


# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)