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
    await message.reply("Введи текст, который хочешь разослать всем или напиши 'Х'")
    await FSMAdmin.text.set()


async def text2(message: types.Message, state: FSMContext):
    await state.finish()
    a = bd_func.get_users()
    if message.text in ['x', 'X', 'Х', 'х'] or \
            message.text in ['Каталог', 'Сделать заказ', 'Мои заказы', 'Связаться с менеджером']:
        bot.send_message(message.from_user.id, 'Отменил!')
        await state.finish()
    else:
        for i in a:
            await bot.send_message(i[1], message.text)
        await message.reply("Отправилось!")
        await state.finish()


def register_handlers_Notification(dp: Dispatcher):
    dp.register_message_handler(text, text='Рассылка', state=None)
    dp.register_message_handler(text2, state=FSMAdmin.text)
