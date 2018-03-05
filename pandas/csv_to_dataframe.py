import pandas as pd
sample=pd.read_csv("C:/Users/Sajan PC/Desktop/python-basic/FB.csv")
print(sample)

#now using square bracket to select a specific column
dup_sample=pd.read_csv("C:/Users/Sajan PC/Desktop/python-basic/FB.csv")
sample1=dup_sample[["Open"]]  #sq brac under sq to make its type as a dataframe
print(sample1)

#to read specific rows
dup_sample2=pd.read_csv("C:/Users/Sajan PC/Desktop/python-basic/FB.csv",index_col=0)
sample1=dup_sample2[0:3] # 0 to 2 rows will be read
#print(sample1)


