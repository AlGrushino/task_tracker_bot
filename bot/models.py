import json

# from aiogram.types.message import Message


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
