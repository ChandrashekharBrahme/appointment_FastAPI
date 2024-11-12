# app/main.py
from fastapi import FastAPI
from .database import Base, engine
from .endpoints import user, admin

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/user")
app.include_router(admin.router, prefix="/admin")
