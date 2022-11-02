from google.cloud.sql.connector import Connector

from sqlalchemy import MetaData
import sqlalchemy
from google.cloud.sql.connector import Connector
import sqlalchemy

INSTANCE_CONNECTION_NAME = f"fastapi-lawyer-project1:us-central1:fastapi-lawyer1" # i.e demo-project:us-central1:demo-instance		
DB_USER = "batman"
DB_PASS = "robin"
DB_NAME = "fastapi"
# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,)

meta_data = MetaData()
