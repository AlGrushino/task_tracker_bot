import asyncio
from create_bot import bot, dp
from bot.handlers.start import start_router
from bot.handlers.tasks import tasks_router

# from work_time.time_func import send_time_msg


async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    dp.include_router(start_router)
    dp.include_router(tasks_router)
    await bot.delete_webhook(drop_pending_updates=True)  # что это
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
