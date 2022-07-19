from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram import Dispatcher
from create_bot import bot
import bd_func
Temp = {}


class FSMAdmin(StatesGroup):
    number = State()
    how = State()


def check_mail(mail):
    if mail[-8:] == "@mail.ru":
        return True
    elif mail[-10:] == "@gmail.com":
        return True
    elif mail[-9:] == "@inbox.ru":
        return True
    elif mail[-9:] == "yandex.ru":
        return True
    elif mail[-6:] == "@ya.ru":
        return True
    else:
        if mail[-3:] == ".ru":
            return True
        elif mail[-4:] == ".com":
            return True
        else:
            return False


async def cm_start(message: types.Message):
    """Проверка на сущ. юзера и получение имени"""

    await FSMAdmin.number.set()
    await bot.send_message(message.from_user.id, f'Добрый день {message.from_user.first_name}! '
                                                 f'Давайте познакомимся! Для совершения заказа это не обходимо)'
                                                 f'Введите ваш номер телефона. Это необходимо для связи с вами, если'
                                                 f'вы не сможете ответить в телеграм!)')


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
    bd_func.register_user(message.from_user.id, Temp[message.from_user.id][0], message.text)
    await state.finish()
    await message.reply("Спасибо!) Все сохранено")


def register_handlers_login(dp: Dispatcher):

    dp.register_message_handler(cm_start1, state=FSMAdmin.number)
    dp.register_message_handler(cm_start3, state=FSMAdmin.how)

