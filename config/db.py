from sqlalchemy import create_engine, MetaData

# engine = create_engine("mysql+pymysql://root:toor@localhost:3306/fastapi")
engine = create_engine("mysql+pymysql://sql10527362:5BEpYlfghy@sql10.freesqldatabase.com:3306/sql10527362")

conn = engine.connect()

meta_data = MetaData()
