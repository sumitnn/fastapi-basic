from fastapi import FastAPI,HTTPException,Path
from typing import Annotated,List
from data import data
from schema import *
app=FastAPI()


# path 
@app.get("/{email}")
async def get_data_with_Email(email:str):
    for val in data:
        if email == val["email"]:
            return val

    raise HTTPException(status_code=404,detail="wrong email is entered") 

@app.get("/search/",response_model=ShowUser)
async def data_search(email:str="guest@hotmail.com"):
  
    for val in data:
        if email == val["email"]:
            return val

    raise HTTPException(status_code=404,detail="wrong email is entered")
    
@app.post("/create/",response_model=List[ShowUser])
async def create_Data(user:User):
    print(user.model_dump())
    print(type(user.model_dump()))
    data.append(user.model_dump())
    
    return data
      
@app.post("/show/")
async def show_Data(user:User):
    return user.email


