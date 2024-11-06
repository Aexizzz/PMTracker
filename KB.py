#Клавиатуры для бота

import asyncio
import logging
import random
from gc import callbacks
from tabnanny import check
from datetime import date
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram.types import Message, CallbackQuery
from pyexpat.errors import messages
from aiogram.filters import StateFilter
import sqlite3
import counters
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def KB_PROJECTS():
    connection = sqlite3.connect('Projects.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    builder = InlineKeyboardBuilder()
    for item in range(1, len(cursor.fetchall())+1):
        builder.button(text = f"Project {item}", callback_data = "choice_action")
    return builder.as_markup(resize_keyboard=True)

def KB_ACTION_PROJECT():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Добавить задачу")
    builder.button(text='Просмотреть задачи')


