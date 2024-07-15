#This is my first python file that im using to establish a connection to a database.
#psycopg2 is main python package used to connect to DB. Used pip install pscyopg2 to install the package.
#loading package
import psycopg2



#establishing connection ot pstgres sql database
con = psycopg2.connect(
database = "First_Postgres_DB",
host =  "127.0.0.1",
user = "postgres",
password = "PostegresSQLserverpassword4132",
port = "5432"
)

#Establishing cursor object
cursor = con.cursor()

#Setting up talbe creation SQL
table_creation = """
Drop Table If Exists Second_Table;

CREATE TABLE Second_Table (
Database_Name VARCHAR(30),
Database_Type VARCHAR(30),
Number_of_Tabels INTEGER
);
"""

#Executing table creation
cursor.execute(table_creation)

con.commit()

#Closing the database connection
con.close()