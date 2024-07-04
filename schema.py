from pydantic import BaseModel,EmailStr, Field
from typing import Optional


class User(BaseModel):
    name:str
    email:EmailStr
    age:int
    city:str =''
    online:Optional[bool]=False
    password:str 


class ShowUser(BaseModel):
    name:str
    email:EmailStr
    age:int
    city:str
    online:Optional[bool]=None
 
    
