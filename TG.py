import asyncio
import logging
import random
from tabnanny import check
from datetime import date
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from pyexpat.errors import messages
from aiogram.filters import StateFilter
import sqlite3
import counters
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import KB
import func


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="8013896759:AAHPykvXHc2i7rFIwzh55FU22nxFx1xuXpM")
# Диспетчер
check_project = 0
dp = Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Создать новый проект")],
        [types.KeyboardButton(text="Выбрать проект для работы")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Привет я бот Project Manager.")
    await message.answer("что вы хотите сделать?", reply_markup=keyboard)

@dp.message(F.text=="Создать новый проект")
async def project_new(message: types.Message):
    connection = sqlite3.connect('Projects.db')
    cursor = connection.cursor()
    counters.counter_project += 1
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS Project{counters.counter_project} (
    id INTEGER PRIMARY KEY,
    role TEXT NOT NULL,
    task TEXT NOT NULL,
    date INTEGER
    )
    ''')
    connection.commit()
    connection.close()
    await message.answer(f"Был успешно создан проект номер {counters.counter_project}")

@dp.message(F.text=="Выбрать проект для работы")
async def project_choice(message: types.Message):
    await message.answer("Выберите номер проекта",  reply_markup=KB.KB_PROJECTS())

    await message.answer("Что вы хотите сделать?", reply_markup=KB.KB_ACTION_PROJECT())



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

