#executing query using pandas
import pandas as pd
from sqlalchemy import create_engine
engine=create_engine("sqlite:///hrms.sqlite")
print(engine.table_names())
df=pd.read_sql_query("SELECT * FROM employee WHERE emp_id>=7 ORDER BY first_name ",engine)
pd.columns=df.keys()
print(df.head())
