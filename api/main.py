from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
import sqlalchemy as sa

# from config import Config

# from .database.models import User, engine

app = FastAPI()
# engine = sa.create_engine(Config.SQLALCHEMY_DATABASE_URI)
# engine = engine
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/")
async def root():
    return {"message": "Hello world"}


class UserCreate(BaseModel):
    user_id: int
    user_name: str


class UserID(BaseModel):
    user_id: int


@app.post("/create_user/")
async def create_user(user_data: UserCreate):
    user_id = user_data.user_id
    user_name = user_data.user_name
    return {
        "msg": "we got data succesfully",
        "user_id": user_id,
        "username": user_name,
    }


@app.get("/get_user_info")
async def get_user_info():
    return {
        "msg": "delivering data",
        "user_id": 10,
        "user_name": "Some_Name"
    }
