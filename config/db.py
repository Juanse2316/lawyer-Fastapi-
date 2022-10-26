from google.cloud.sql.connector import Connector
import sqlalchemy
from sqlalchemy import MetaData

import pymysql

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "flask-project-357819:us-central1:firstdb",
        "pymysql",
        user="request",
        password="19072212",
        db="my_bd"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

meta_data = MetaData()
