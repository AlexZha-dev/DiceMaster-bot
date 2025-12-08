import asyncio
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

ALLOWED_UPDATES = ['message, edited_message']

load_dotenv()
token = os.getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Это была команда старт")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())