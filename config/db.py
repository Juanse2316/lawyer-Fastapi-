from google.cloud.sql.connector import Connector
import google.auth
from google.auth.transport.requests import Request
import sqlalchemy
from sqlalchemy import MetaData

# IAM database user parameter (IAM user's email before the "@" sign, mysql truncates usernames)
# ex. IAM user with email "demo-user@test.com" would have database user name "demo-user"
IAM_USER = 'ladinomendietajuanse'[0].split("@")[0]

# get application default credentials of IAM user (current logged in user)
credentials, project = google.auth.default()

# refresh credentials if expired
if not credentials.valid:
      request = Request()
      credentials.refresh(request)

# initialize connector
connector = Connector()

# getconn now using IAM user and OAuth2 token as password
def getconn():
    conn = connector.connect(
      'fastapi-lawyer-project1:us-central1:fastapi-lawyer1',
      "pymysql",
      user=IAM_USER,
      password=credentials.token,
      db="", # log in to instance but don't connect to specific database
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
meta_data = MetaData()
