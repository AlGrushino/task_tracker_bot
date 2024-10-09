import json
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

# from aiogram.types.message import Message


class Base(DeclarativeBase):
    pass


class User(Base):  # mb better call it's Person
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


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
