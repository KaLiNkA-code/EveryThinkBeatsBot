from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram import Dispatcher
from create_bot import bot
import bd_func
from Keyboards import Client_kb, Admin_kb
from bd_func import admin


Temp = {}


class FSMAdmin(StatesGroup):
    number = State()
    how = State()


async def cm_start(message: types.Message, state: FSMContext):
    """Проверка на сущ. юзера и получение имени"""

    print(message)
    if message.from_user.id in admin:
        await bot.send_message(message.from_user.id, f'Привет) {message.from_user.first_name}',
                               reply_markup=Admin_kb.Admin_Start_kb)
        await state.finish()
    else:
        print('dddd')
        a = bd_func.get_users()
        x = 0
        for i in a:
            if str(message.from_user.id) == i[1]:
                x = 1
        if x:
            await bot.send_message(message.from_user.id, f'Добрый день {message.from_user.first_name}! ', reply_markup=Client_kb.Client_Start_kb)

        else:
            await FSMAdmin.number.set()
            await bot.send_message(message.from_user.id, f'Добрый день {message.from_user.first_name}! '
                                                         f'Давайте познакомимся!)'
                                                         f'Введите ваш номер телефона. Это необходимо для связи с вами,'
                                                         f' если вы не сможете ответить в телеграм!)', reply_markup=types.ReplyKeyboardRemove())


async def cm_start1(message: types.Message):
    try:
        temp = message.text.replace(' ', '')
        if 11 <= len(temp) <= 12:
            temp = message.text
            temp = temp.replace(' ', '')
            temp = temp.replace('+7', '8')
            if len(temp) == 11 and temp[0] == '8':
                await FSMAdmin.how.set()
                await message.reply('Спасибо!) Остался последний пункт) Подскажите пожалуйста, как вы узнали об'
                                    'этом боте? Это и вправду очень важно для нас!')
                Temp[message.from_user.id] = [temp]
            else:
                await FSMAdmin.number.set()
                await message.reply('Не корректный ввод, попробуй еще раз')
        else:
            await FSMAdmin.number.set()
            await message.reply('Не корректный ввод, попробуй еще раз')
    except ValueError:
        await FSMAdmin.number.set()
        await message.reply('Не корректный ввод, попробуй еще раз')


async def cm_start3(message: types.Message, state: FSMContext):
    bd_func.register_user(message.from_user.id, message.from_user.first_name,
                          Temp[message.from_user.id][0], message.text)
    await state.finish()
    await message.reply("Спасибо, вы зарегистрированы!)", reply_markup=Client_kb.Client_Start_kb)


def register_handlers_register(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['start'], state=None)
    dp.register_message_handler(cm_start1, state=FSMAdmin.number)
    dp.register_message_handler(cm_start3, state=FSMAdmin.how)
