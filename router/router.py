from typing import List

from fastapi import APIRouter
from fastapi import status

from schema.user_schema import User, UserBase, UserLogin, UserRegister
user = APIRouter()


#Path operation
@user.get("/")
def root():
    return {"message": "Hi I'm a God"}


##User
@user.post(
    path='/api/signup',
    response_model=User,
    status_code= status.HTTP_201_CREATED,
    summary="register a user",
    tags=["Users"]
)
def signup():
    """
    This path operation register a user in a data base

    Parameters:
        - Request body parameter
            - user: UserRegister
    Return a success message
    """
    pass
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
    pass

@user.get(
    path='/api/user/{user_id}',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user():
    """
    """
    pass

@user.delete(
    path='/api/user/{user_id}/delete',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def delete_a_user():
    """
    """
    pass

@user.put(
    path='/api/user/{user_id}/update',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def delete_a_user():
    """
    """
    pass

##Process
 