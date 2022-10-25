
from google.cloud.sql.connector import Connector
import sqlalchemy
from sqlalchemy import MetaData

import pymysql

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "fastapi-lawyer-project1:us-central1:lawyerdb",
        "pymysql",
        user="request",
        password="19072212",
        db="fastapidb"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

meta_data = MetaData()