from fastapi import APIRouter


user = APIRouter()

@user.get("/")
def root():
    return {"message": "Hi I'm a God"}

@user.get('/login')
def creat_user(data_uder):
    pass

 