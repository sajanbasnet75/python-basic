import pandas as pd
sample=pd.read_csv("c:/users/sajan pc/desktop/python-basic/fb.csv")
print(sample)
for lab,row in sample.iterrows():
  print(lab,row["Open"])
  
    
#lets say i want to add a column "Difference"
#which contains difference between High and Low

for lab,row in sample.iterrows():
  sample.loc[lab,"Difference"]=(row["High"]-row["Low"])

print(sample)

'''
If you want to add a column to a DataFrame by calling a function
on another column, the iterrows() method in combination with a for loop
is not the preferred way to go.
Instead, you'll want to use apply().
'''
#example :cars["COUNTRY"]=cars["country"].apply(str.upper)

sample["New_Column"]=sample['High']-sample['Low']
print(sample)
