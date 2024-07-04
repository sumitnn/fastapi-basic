from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DATETIME
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


# class Basemodel():
#     date_created=Column(DATETIME,default=datetime.now())

# class User(Base,Basemodel):
#     __tablename__="users"
#     id=Column(Integer,primary_key=True,index=True)
#     email=Column(String,unique=True)
#     first_name=Column(String,default='')
#     last_name=Column(String,default='')
#     age=Column(Integer,default=18)
    

# class Items(Base,Basemodel):
#     __tablename__="items"
#     id=Column(Integer,primary_key=True,index=True)
#     name=Column(String)
#     quantity=Column(Integer,default=0)


