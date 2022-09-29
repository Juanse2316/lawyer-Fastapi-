from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, VARCHAR, TIMESTAMP, BOOLEAN, String, TEXT, Date
from config.db import engine, meta_data

suscription = Table(
    'suscription', meta_data, 
    Column('id', Integer, primary_key =True),
    Column('suscription_Type', VARCHAR(255), nullable=False),
)


usertype = Table(
    'usertype', meta_data,
    Column('id', Integer, primary_key =True),
    Column('user_Type', VARCHAR(255), nullable=False),
)

payment = Table(
    'payment', meta_data, 
    Column('id', Integer, primary_key =True),
    Column('name', VARCHAR(255), nullable=False),
    Column('payment_number', VARCHAR(255), nullable=False, unique=True),
    Column('expiration_date', Date , nullable=False),
    Column('user_id', Integer, ForeignKey('user_base.id'), nullable = False)
)

user_base = Table(
    'user_base', meta_data,
    Column('id', Integer, primary_key =True),
    Column('name', VARCHAR(255), nullable=False),
    Column('last_name', VARCHAR(255), nullable=False),
    Column('password', String(255), nullable=False),
    Column('email', VARCHAR(255), nullable=False, unique=True ), 
    Column('suscription_id', Integer, ForeignKey('suscription.id'), nullable = False),
    Column('user_type_id', Integer, ForeignKey('usertype.id'), nullable = False),
)

process = Table(
    'process', meta_data,
    Column('id', Integer, primary_key =True),
    Column('tittle', VARCHAR(255), nullable=False),
    Column('description', TEXT, nullable=False),
    Column('start_date', TIMESTAMP),
    Column('update_at', TIMESTAMP),
    Column('finish_date', Date),
    Column('status', BOOLEAN),
    Column('user_id', Integer, ForeignKey('user_base.id'), nullable = False)   
)

meta_data.create_all(engine)

