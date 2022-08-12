from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram import Dispatcher
from create_bot import bot
import bd_func
Temp = {}


class FSMAdmin(StatesGroup):
    text = State()


async def text(message: types.Message):
    await message.reply("Введи текст, который хочешь разослать всем")
    await FSMAdmin.text.set()


async def text2(message: types.Message, state: FSMContext):
    await state.finish()
    a = bd_func.get_users()
    for i in a:
        await bot.send_message(i[1], message.text)
    await message.reply("Отправилось!")


def register_handlers_Notification(dp: Dispatcher):
    dp.register_message_handler(text, text='Рассылка', state=None)
    dp.register_message_handler(text2, state=FSMAdmin.text)
