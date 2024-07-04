from fastapi import APIRouter
from user import *

router=APIRouter(prefix="/v1")
router.include_router(user_router)