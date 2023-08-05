from fastapi import FastAPI
from .user.api import router as UserAPI

app = FastAPI()

app.include_router(UserAPI.router)
