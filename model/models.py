from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, VARCHAR, TIMESTAMP, BOOLEAN, String, TEXT, Date
from config.db import engine, meta_data

suscription = Table(
    'suscription', meta_data, 
    Column('id', Integer, primary_key =True),
    Column('suscription_Type', VARCHAR(255), nullable=False),
)

payment = Table(
    'suscription', meta_data, 
    Column('id', Integer, primary_key =True),
    Column('name', VARCHAR(255), nullable=False),
    Column('payment_number', String, nullable=False),
    Column('expiration data', Date , nullable=False),
)


usertype = Table(
    'usertype', meta_data,
    Column('id', Integer, primary_key =True),
    Column('user_Type', VARCHAR(255), nullable=False),
)

user_base = Table(
    'user_base', meta_data,
    Column('id', Integer, primary_key =True),
    Column('name', VARCHAR(255), nullable=False),
    Column('last_name', VARCHAR(255), nullable=False),
    Column('password', String(255), nullable=False),
    Column('email', VARCHAR(255), nullable=False ),
    Column('payment_id', Integer, ForeignKey('payment.id')), 
    Column('suscription_id', Integer, ForeignKey('suscription.id')),
    Column('user_type_id', Integer, ForeignKey('usertype.id')),
)

process = Table(
    'user_base', meta_data,
    Column('id', Integer, primary_key =True),
    Column('tittle', VARCHAR(255), nullable=False),
    Column('description', TEXT, nullable=False),
    Column('start date', TIMESTAMP),
    Column('finish date', Date),
    Column('status', BOOLEAN),
    Column('user_base_id', Integer, ForeignKey('user_base.id'))   
)

meta_data.create_all(engine)
