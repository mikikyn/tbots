import logging
from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor

TOKEN = "7535074646:AAG5zf3M2tHO9CF4K9cWRE1dAY_Os7BkHnw"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

admin = [6048341497, ]

async def on_startup(_):
    for i in admin:
        await bot.set_webhook(chat_id=i, text="Бот включен!")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)