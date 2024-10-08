from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

tasks_router = Router()


@tasks_router.message(Command("Add"))
async def cmd_add_task(message: Message):
    await message.answer(
        "Задача добавлена"
    )
