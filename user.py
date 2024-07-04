from fastapi import APIRouter,HTTPException,UploadFile
from schema import *
from typing import List
from data import data

user_router=APIRouter(prefix='',tags=["UserData"])

# path 
@user_router.get("/{email}")
async def get_data_with_Email(email:str):
    for val in data:
        if email == val["email"]:
            return val

    raise HTTPException(status_code=404,detail="wrong email is entered") 

@user_router.get("/search/",response_model=ShowUser)
async def data_search(email:str="guest@hotmail.com"):
  
    for val in data:
        if email == val["email"]:
            return val

    raise HTTPException(status_code=404,detail="wrong email is entered")
    
@user_router.post("/create/",response_model=List[ShowUser])
async def create_Data(user:User):
    print(user.model_dump())
    print(type(user.model_dump()))
    data.append(user.model_dump())
    
    return data
      
@user_router.post("/show/")
async def show_Data(user:User):
    return user.email


@user_router.post("/fileupload/")
def file_upload(file:UploadFile):
    return file