from fastapi import FastAPI,HTTPException,APIRouter
from typing import Annotated,List
from  routers import router

app=FastAPI()

app.include_router(router)

