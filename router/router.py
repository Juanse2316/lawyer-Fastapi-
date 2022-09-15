#Python
from typing import List
#Fast api
from fastapi import APIRouter
from fastapi import status
from werkzeug.security import generate_password_hash, check_password_hash
#Local
from schema.user_schema import User, UserBase, UserLogin, UserRegister
from schema.process_schema import Process
from config.db import engine
from model.models import user_base

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
def signup(data_user: UserRegister):
    """
    This path operation register a user in a data base

    Parameters:
        - Request body parameter
            - user: UserRegister
    Return a success message
    """
    with engine.connect() as conn:
        new_user = data_user.dict()
        new_user["password"] = generate_password_hash(data_user.password, "pbkdf2:sha256:30", 40)
        conn.execute(user_base.insert().values(new_user))
    
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
    """
    with engine.connect() as conn:
        result = conn.execute(user_base.select()).fetchall()

        return result

###Show a user
@user.get(
    path='/api/user/{user_id}',
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
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
def delete_a_user():
    """
    """
    pass

###Update a user
@user.put(
    path='/api/user/{user_id}/update',
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
    response_model=List[Process],
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