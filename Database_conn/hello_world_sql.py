
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///hrms.sqlite')
print(engine.table_names())
# Open engine connection: con
con=engine.connect()

# Perform query: rs
rs = con.execute("SELECT dep_name FROM department")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
#set the DataFrame's column names to the corresponding names of
#the table columns.
df.columns = rs.keys()
# Close connection

# Print head of DataFrame df
print(df.head())

print("================================================")
print("Selecting particular column and row")

rs = con.execute("SELECT first_name FROM employee")
df = pd.DataFrame(rs.fetchmany(size=5))
df.columns = rs.keys()

print(df)
con.close()


                     
