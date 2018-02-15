# in order to use the specific column and rown of the dataframe
# we use a loc and iloc where loc= location based and iloc is a position based

import pandas as pd
sample=pd.read_csv("C:/Users/Sajan PC/Desktop/python-basic/FB.csv")

#row access loc : selection entire rows
print(sample.loc[[1]])
print(sample.loc[[1,2,3]])

#row and column loc
print("\n ROW AND COLUMN LOC")
print(sample.loc[[1,2,3],['Open','Close']])
print("finish")

#loc and iloc are similar loc takes the value of the dataframe
#where as iloc takes index
print(sample.iloc[1]) #gives the value 
print(sample.iloc[:,[1,2]])

