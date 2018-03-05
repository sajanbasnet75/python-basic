
'''
Each row or record in a table represents an instance of an entity type.

Each column in a table represents an attribute or feature of an instance.

Connecting a "sqlite" database using "sqlalchemy" package

1>Creating a databse engine
from sqlalcchemy import create_engine
engine=create_engine("sqlite:///sajan.sqlite")
Here in above create_engine function the argument should be a string which
contains the type of db u are trying to connect and the name of the database

2>Now connecting with the databse

con=engine.connect()

3>Executing a simple query and storing the result in a variable
rs=con.execute("SELECT  * FROM table_name")

4>using pandas to make the result rs into dataframe
df=pd.DataFrame(rs.fetchall())
print(df.head())
con.close()

If dont want to close engine again nad asin use:
#with engine.connect() as con
'''
