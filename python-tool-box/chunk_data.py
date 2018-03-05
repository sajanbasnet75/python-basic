'''
Processing large amounts of Twitter data

Sometimes, the data we have to process reaches a size that is
too much for a computer's memory to handle. This is a common problem
faced by data scientists. A solution to this is to process an entire data
source chunk
by chunk, instead of a single go all at once.

In this exercise, you will do just that. You will process a
large csv file of Twitter data in the same way that you processed
'tweets.csv' in Bringing it all together exercises of the prequel course,
but this time, working on it in chunks of 10 entries at a time.
'''
import pandas as pd

count_langu={}
for data in pd.read_csv("C:/Users/Sajan PC/Desktop/python-basic/tweets.csv",chunksize=10):
    for chunk in data['lang']:
        # Iterate over the column in DataFrame
        # If the language is in count_langu, add 1
        if chunk in count_langu.keys():
            count_langu[chunk] += 1
        else:
            count_langu[chunk] = 1

print(count_langu)
