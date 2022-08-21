from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
""" async: Если в исполнении какой либо функции получился участок времени, когда ничего не используется,
он позволяет в эти промежутки исполнять что то другое"""
storage = MemoryStorage()
token = '5460098484:AAH2GnJwqjzE6dAQAUNtmo2OCNPOwvdMo_U'

bot = Bot(token)
dp = Dispatcher(bot, storage=storage)  # Инициализируем диспачер
