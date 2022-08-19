from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:toor@127.0.0.1:3306/Fastapi ")

conn = engine.connect()

meta_data = MetaData()