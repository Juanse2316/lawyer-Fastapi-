from google.cloud.sql.connector import Connector
import sqlalchemy
from sqlalchemy import MetaData
import pymysql
from google.cloud.sql.connector import Connector, IPTypes

# Note: all parameters below are optional
connector = Connector(
    ip_type=IPTypes.PUBLIC,
    enable_iam_auth=False,
    timeout=30,
    credentials=None
)
# initialize Connector object


# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "fastapi-lawyer-project1:us-central1:fastapi-lawyer1",
        "pymysql",
        user="root",
        password="toor",
        db="fastapi"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://root:toor@/fastapi?unix_socket=/cloudsql/fastapi-lawyer1",
    creator=getconn,
)

meta_data = MetaData()
#  mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>