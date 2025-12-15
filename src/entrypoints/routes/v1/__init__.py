from fastapi import APIRouter

from .auth.auth import router as auth

v1 = APIRouter(prefix="/v1")
v1.include_router(auth)
