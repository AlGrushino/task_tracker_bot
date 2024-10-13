import sqlalchemy as sa
from config import Config
import json
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = sa.create_engine(Config.SQLALCHEMY_DATABASE_URI)


# from aiogram.types.message import Message


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))


def check_id(
    user_id: int,
) -> bool:  # или лучше здесь сделать Message.from_user.id
    """
    Проверяет, есть ли id в базе данных, возвращает bool.

    Ключевые аргументы:
    user_id -- id пользователя
    """
    with open("users.json", "r") as file:
        data = json.load(file)
        return user_id == data["id"]
