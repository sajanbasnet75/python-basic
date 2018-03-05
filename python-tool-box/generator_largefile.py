'''
In the previous exercise, you processed a file line by line for a given
number of lines. What if, however, you want to do this for the entire file?

In this case, it would be useful to use generators. Generators allow users to
lazily evaluate data. This concept of lazy evaluation is useful when you have
to deal with very large datasets because it lets you generate values in an
efficient manner by yielding only chunks of data at a time instead of the
whole thing at once.

In this exercise, you will define a generator function read_large_file()
that produces a generator object which yields a single line from a file
each time next() is called on it. The csv file 'world_dev_ind.csv' is in
your current directory for your use.
Note that when you open a connection to a file,the resulting file object is already a generator!
So out in the wild, you won't have to explicitlycreate generator
objects in cases such as this.
'''
# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""
    #remove column name
    file_object.readline()
    
    # Loop indefinitely until the end of the file
    while True:
          
        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield(data)
        
# Open a connection to the file
with open('c:/Users/Sajan PC/Desktop/python-basic/wbi.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
