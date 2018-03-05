'''
In the previous exercise, you used read_csv() to read in DataFrame chunks from
a large dataset. In this exercise, you will read in a file using a bigger
DataFrame chunk size and then process the data from the first chunk.

To process the data, you will create another DataFrame composed of only the
rows from a specific country. You will then zip together two of the columns
from the new DataFrame, 'Total Population' and 'Urban population (% of total)'.
Finally, you will create a list of tuples from the zip object, where each
tuple is composed of a value from each of the two columns mentioned.
'''
import pandas as pd
import matplotlib.pyplot as plt
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('c:/Users/Sajan PC/Desktop/python-basic/wbi.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop =next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode']=='CEB']

print("-----------------------------------------------------------------")
print("the new dataframe with country code CEB only")
print(df_pop_ceb)
print("--------------------------------------------------------------")

#Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'],df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)



# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
print(df_pop_ceb.head())

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

