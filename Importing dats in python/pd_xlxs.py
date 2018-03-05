
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file ="c:/Users/Sajan PC/Desktop/python-basic/Importing dats in python/fff.xls"

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
