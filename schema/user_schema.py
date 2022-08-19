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
    start_date: Union[datetime, None] = Field(...)
    finish_date: Union[date, None]= Field(...)
    status: bool = Field(...)
    user_id: int = Field(...)


class Payment(BaseModel):
    id: Optional[int] 
    name: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )
    payment_number: PaymentCardNumber = Field(...)
    sexpiration_date: Union[date, None] = Field(...)
    

class Suscriptiom(BaseModel):
    id: Optional[int] 
    suscription_Type: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )


class UserType(BaseModel):
    id: Optional[int] 
    user_Type: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )
