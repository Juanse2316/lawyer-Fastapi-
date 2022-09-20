#Python
from typing import List
#Fast api
from fastapi import APIRouter
from fastapi import status
from fastapi import Body
from werkzeug.security import generate_password_hash, check_password_hash
#Local
from schema.user_schema import User, UserRegister, Payment
from schema.process_schema import Process
from config.db import engine
from model.models import user_base, payment

user = APIRouter()


#Path operation



##User

###Create a user 
@user.post(
    path='/api/signup',
    response_model=User,
    status_code= status.HTTP_201_CREATED,
    summary="register a user",
    tags=["Users"]
)
def signup(data_user: UserRegister, data_payment: Payment ):
    """
    This path operation register a user in a data base

    Parameters:
        - Request body parameter
            - user: UserRegister
    Return a json with the basic infromation:
        - email: EmailStr
        - name: str
        - last name: str
    """
    with engine.connect() as conn:
        new_user = data_user.dict()
        new_user["password"] = generate_password_hash(data_user.password, "pbkdf2:sha256:30", 40)
        conn.execute(user_base.insert().values(new_user))
        
        
        new_payment = data_payment.dict()
        new_payment["expiration_date"] = str(new_payment["expiration_date"])
        conn.execute(payment.insert().values(new_payment))
    
        return data_user

###Login a user 
@user.post(
    path='/api/login',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary="login a user",
    tags=["Users"]
)
def login():
    """
    """
    pass

###Show all users 
@user.get(
    path='/api/users',
    response_model=List[User],
    status_code= status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    """
    This path operation shows all users in the app

    Parameters:
        
    Return a json with the basic infromation:
        - email: EmailStr
        - name: str
        - last name: str
    """
    with engine.connect() as conn:
        result = conn.execute(user_base.select()).fetchall()

        return result

###Show a user
@user.get(
    path='/api/users/{user_id}',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user(user_id: str):
    """
    """
    with engine.connect() as conn:
        result = conn.execute(user_base.select().where(user_base.c.id== user_id)).first()

        return result

###Delete a user
@user.delete(
    path='/api/user/{user_id}/delete',
    status_code= status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
def delete_a_user(user_id: str):
    """
    """
    with engine.connect() as conn:
        conn.execute(user_base.delete().where(user_base.c.id== user_id))
        conn.execute(payment.delete().where(user_base.c.id== user_id))
        return {"mensage": "user delete"}

###Update a user
@user.put(
    path='/api/users/{user_id}/update',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
)
def update_a_update(data_update:UserRegister, user_id: str):
    """
    """
    with engine.connect() as conn:
        encryp_password = generate_password_hash(data_update.password, "pbkdf2:sha256:30", 40)
        result = conn.execute(user_base.update().values(name=data_update.name,last_name=data_update.last_name, password= encryp_password).where(user_base.c.id== user_id))
        result= conn.execute(user_base.select().where(user_base.c.id== user_id)).first()
        return result

##Process

@user.get(path='/',
    # response_model=List[Process],
    status_code= status.HTTP_200_OK,
    summary="show all process",
    tags=["process"]
)
def root():
    return {"message": "Hi I'm a God"}


@user.post(path='/api/new-process',
    response_model=List[Process],
    status_code= status.HTTP_201_CREATED,
    summary="create a process",
    tags=["process"]
)
def create_new_user ():
    """
    """
    pass

@user.get(path='/api/process/{process_id}',
    response_model=List[Process],
    status_code= status.HTTP_200_OK,
    summary="show a process",
    tags=["process"]
)
def create_new_user ():
    """
    """
    pass


@user.delete(path='/api/{process_id}/delete',
    response_model=List[Process],
    status_code= status.HTTP_201_CREATED,
    summary="Delete aprocess",
    tags=["process"]
)
def create_new_user ():
    """
    """
    pass


@user.put(path='/api/{process_id}/update',
    response_model=List[Process],
    status_code= status.HTTP_201_CREATED,
    summary="Delete aprocess",
    tags=["process"]
)
def create_new_user ():
    """
    """
    pass