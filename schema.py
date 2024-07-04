from pydantic import BaseModel,EmailStr, Field



class User(BaseModel):
    name:str
    email:EmailStr
    age:int
    city:str =''
    online:bool =False
    password:str 


class ShowUser(BaseModel):
    name:str
    email:EmailStr
    age:int
    city:str
    online:bool
 
    
