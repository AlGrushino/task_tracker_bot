from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.models import check_id

tasks_router = Router()


@tasks_router.message(Command("Add"))
async def cmd_add_task(message: Message) -> None:
    user_id = message.from_user.id

    if check_id(user_id):
        await message.answer(f"Задача добавлена id:{user_id}")
    else:
        await message.answer("Your ID not in db(")
