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
    language = State()
    number = State()
    how = State()


async def cm_start(message: types.Message, state: FSMContext):
    print(message)
    """Проверка на сущ. юзера и получение имени"""
    if message.from_user.id in admin:
        await bot.send_message(message.from_user.id, f'Привет) {message.from_user.first_name}',
                               reply_markup=Admin_kb.Admin_Start_kb)
        await state.finish()
    else:
        a = bd_func.get_users()
        x = 0
        for i in a:
            if str(message.from_user.id) == i[1]:
                x = 1
        if x:
            text = "Добрый день!)" if bd_func.check_language(str(message.from_user.id)) else "Hello!"
            print(bd_func.check_language(message.from_user.id))
            await bot.send_message(message.from_user.id, f'{text} {message.from_user.first_name}! ',
                                   reply_markup=Client_kb.Client_Start_kb)
            await state.finish()

        else:
            await FSMAdmin.language.set()
            await bot.send_message(message.from_user.id, f'Hi! {message.from_user.first_name}! '
                                                         f'What language you have?',
                                   reply_markup=Client_kb.Language_kb)


async def cm_start1(callback: types.CallbackQuery):
    """Проверка на сущ. юзера и получение имени"""
    Temp[callback.from_user.id] = [callback.data]
    await FSMAdmin.number.set()
    if Temp[callback.from_user.id][0] == "RU":
        await bot.send_message(callback.from_user.id, f'Добрый день {callback.from_user.first_name}! '
                                                      f'Давайте познакомимся!)'
                                                      f'Введите ваш номер телефона. Это необходимо для связи с вами,'
                                                      f' если вы не сможете ответить в телеграм!)',
                               reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_message(callback.from_user.id, f"Good afternoon {callback.from_user.first_name}! \n"
                                                      f"Let's get acquainted!)\n"
                                                      f"Enter your phone number. This is necessary to contact you, "
                                                      f"if You can't answer on telegram!)",
                               reply_markup=types.ReplyKeyboardRemove())


async def cm_start2(message: types.Message):
    try:
        temp = message.text.replace(' ', '')
        if 11 <= len(temp) <= 12:
            temp = message.text
            temp = temp.replace(' ', '')
            temp = temp.replace('+7', '8')
            if len(temp) == 11 and temp[0] == '8':
                await FSMAdmin.how.set()
                text = "Спасибо!) Остался последний пункт) Подскажите пожалуйста, как вы узнали об этом боте? " \
                       "Это и вправду очень важно для нас!" if Temp[message.from_user.id][0] == "RU" \
                    else "Thank you!) There is one last point left) Can you please tell me how you found out about " \
                         "this bot? It really is very important for us!"

                await message.reply(text)
                Temp[message.from_user.id] += [temp]
            else:
                await FSMAdmin.number.set()
                text = "Не корректный ввод, попробуй еще раз" if Temp[message.from_user.id][0] == "RU" \
                    else "Incorrect input, try again"

                await message.reply(text)
        else:
            await FSMAdmin.number.set()
            text = "Не корректный ввод, попробуй еще раз" if bd_func.check_language(
                str(message.from_user.id)) else "Incorrect input, try again"
            await message.reply(text)
    except BaseException as Err:
        await FSMAdmin.number.set()
        text = "Не корректный ввод, попробуй еще раз" if Temp[message.from_user.id][0] == "RU" \
            else "Incorrect input, try again"
        await message.reply(text)


async def cm_start3(message: types.Message, state: FSMContext):
    bd_func.register_user(message.from_user.id, message.from_user.first_name,
                          Temp[message.from_user.id][1], message.text, Temp[message.from_user.id][0])

    print(message.from_user.id, message.from_user.first_name,
                          Temp[message.from_user.id][1], message.text, Temp[message.from_user.id][0])
    await state.finish()
    if bd_func.check_language(str(message.from_user.id)):

        await message.reply("Спасибо, вы зарегистрированы!)", reply_markup=Client_kb.Client_Start_kb)
    else:
        await message.reply("Thank you, you are registered!)", reply_markup=Client_kb.Client_Start_kb)


def register_handlers_register(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['start'], state=None)
    dp.register_callback_query_handler(cm_start1, state=FSMAdmin.language)
    dp.register_message_handler(cm_start2, state=FSMAdmin.number)
    dp.register_message_handler(cm_start3, state=FSMAdmin.how)
