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


async def project_choice_two(message: types.Message):
    await message.answer("Что вы хотите сделать?", reply_markup=KB.KB_ACTION_PROJECT())