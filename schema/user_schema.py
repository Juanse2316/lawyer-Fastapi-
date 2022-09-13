#python
from datetime import  date
from typing import Optional, Union

#pydantic
from pydantic import BaseModel, Field, PaymentCardNumber, EmailStr


class UserBase(BaseModel):
    id: Optional[int] 
    email: EmailStr = Field(...)
class UserLogin(BaseModel):
    password: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )

class User(UserBase):
    
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
    

    
    payment_id: Optional[int]  = Field(default=None)
    suscription_id: Optional[int] = Field(default=None)
    user_type_id: int = Field(...)

class UserRegister(User):
    password: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )




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
