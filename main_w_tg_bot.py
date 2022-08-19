import requests
import datetime

from pip._internal import commands

from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handlers(commands=["start"])
async def start_command(message: types.message):
    await message.reply("Hello give me some information ")


if __name__ == '__main__':
    executor.start_polling(dp)
