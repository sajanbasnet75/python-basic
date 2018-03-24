'''
You have just imported a file from the web, saved
it locally and loaded it into a DataFrame. If you just wanted
to load a file from the web into a DataFrame without first saving
it locally, you can do that easily using pandas.
In particular, you can use the function pd.read_csv()
with the URL as the first argument and the separator sep as the
second argument.
'''


# Import packages
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlretrieve
# Assign url of file: url
url='https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df=pd.read_csv('https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv',sep=';')

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()
