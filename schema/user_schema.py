from datetime import datetime, date
from typing import Optional, Union

from pydantic import BaseModel, Field, PaymentCardNumber

class User(BaseModel):
    id: Optional[int] 
    name: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )
    last_name: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )
    password: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )
    payment_id: Optional[int] 
    suscription_id: Optional[int] 
    user_type_id: int = Field(...)


class Process(BaseModel):
    id: Optional[int] 
    tittle: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )
    description: str = Field(
        ...,
        min_length= 50,
        ) 
    start_date: Union[date, None] = Field(...)
    finish_date: Union[date, None]= Field(...)
    status: bool = Field(...)
    user_id: int = Field(...)


class Payment(BaseModel):
    pass

# payment = Table(
#     'suscription', meta_data, 
#     Column('id', Integer, primary_key =True),
#     Column('name', VARCHAR(255), nullable=False),
#     Column('payment_number', String, nullable=False),
#     Column('expiration data', Date , nullable=False),

class Suscriptiom(BaseModel):
    pass
# suscription = Table(
#     'suscription', meta_data, 
#     Column('id', Integer, primary_key =True),
#     Column('suscription_Type', VARCHAR(255), nullable=False),



class UserType(BaseModel):
    pass
# usertype = Table(
#     'usertype', meta_data,
#     Column('id', Integer, primary_key =True),
#     Column('user_Type', VARCHAR(255), nullable=False),
# )