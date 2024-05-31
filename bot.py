import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardButton, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ.get("BOT_TOKEN")

WEB_APP_URL = os.environ.get("WEB_APP_URL")

dp = Dispatcher()

inline_webapp = InlineKeyboardBuilder()

inline_webapp_buttons = InlineKeyboardButton(
    text='Manage', web_app=WebAppInfo(url=WEB_APP_URL))
inline_webapp.add(inline_webapp_buttons)


@dp.message(Command(commands=['start']))
async def register_handler(message) -> None:

    await message.answer("Click the button below to manage your federated learning project:", reply_markup=inline_webapp.as_markup())


async def main() -> None:
    bot = Bot(token=TOKEN)

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
