from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram import Dispatcher
from create_bot import bot
from Keyboards import Client_kb
import bd_func
Temp = {}


class FSMAdmin(StatesGroup):
    who = State()
    experience = State()
    number = State()
    how = State()


async def cm_start(callback: types.CallbackQuery):
    """Проверка на сущ. юзера и получение имени"""

    if callback.from_user.id not in bd_func.get_ids_of_users():
        pass
    else:
        pass
    await FSMAdmin.who.set()

    await bot.send_message(callback.from_user.id, f'Добрый день {callback.from_user.first_name}! '
                                                  f'Давайте познакомимся! На данный момент мы набираем людей '
                                                  f'на следующие направления:\n'
                                                  f'1 - Разработчик игр (C# & Unity)\n'
                                                  f'2 - Разработчик чат ботов\n'
                                                  f'3 - Разработчик сайтов\n'
                                                  f'4 - Саунд дизайнер для игр\n'
                                                  f'5 - Графика для игр\n'
                                                  f'6 - Битмейкер',
                           reply_markup=Client_kb.FSM_reg_kb1)
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


async def cm_start1(callback: types.CallbackQuery):
    global Temp
    print(callback.data)
    if callback.data == '1':
        await callback.message.answer('Отлично! О нас: Мы амбициозная и быстроразвивающаяся команда, разрабатываютщая '
                                      'серию игр, которая инновационная и не повторимая!')
        await callback.message.answer("Мог бы написать, какой у тебя опыт в программировании на этом стеке и"
                                      " желательно расскажи о играх, которые уже создавал!)")
        await callback.answer(':)')
        Temp[callback.from_user.id] = ['Разработчик игр (C# & Unity)']

    elif callback.data == '2':
        await callback.message.answer('Отлично! О нас: Мы разрабатываем чат ботов на заказ, а так же для своих '
                                      'продуктов! Если хочешь постоянно саморазвиваться, присоединяйся к нам!)')
        await callback.message.answer("Мог бы написать, какой у тебя опыт в программировании на Python and PostgreSQL "
                                      "и покажи кейсы, которые уже создавал!)")
        Temp[callback.from_user.id] = ['Разработчик чат ботов']
    elif callback.data == '3':
        await callback.message.answer('Отлично! О нас: Мы делаем инновационные продукты и для них нужны сайты, а так '
                                      'же у нас могут заказать сайт')
        await callback.message.answer("Мог бы написать, какой у тебя опыт в программировании на Django and PostgreSQL "
                                      "и покажи кейсы, которые уже создавал!)")
        Temp[callback.from_user.id] = ['Разработчик сайтов']
    elif callback.data == '4':
        await callback.message.answer('Отлично! О нас: Мы амбициозная и быстроразвивающаяся команда, разрабатываютщая '
                                      'серию игр, которая инновационная и не повторимая!')
        await callback.message.answer("Мог бы написать, какой у тебя есть опыт в создании звуков или даже озвучки "
                                      "персонажей?)")
        Temp[callback.from_user.id] = ['Саунд дизайнер для игр']
    elif callback.data == '5':
        await callback.message.answer('Отлично! О нас: Мы амбициозная и быстроразвивающаяся команда, разрабатываютщая '
                                      'серию игр, которая инновационная и не повторимая!')
        await callback.message.answer("Мог бы написать, какой у тебя есть опыт в создании ассетов или даже "
                                      "анимации персонажей?)")
        Temp[callback.from_user.id] = ['Графика для игр']
    elif callback.data == '6':
        await callback.message.answer('Отлично! О нас: Мы амбициозная и быстроразвивающаяся команда, разрабатываютщая и'
                                      ' делающая на заказ биты, свидения и треки! Есть перспектива сделать музыку для'
                                      ' таких продуктов, как игры или приложения KaLiNkA Group')
        await callback.message.answer("Мог бы написать, какой у тебя есть опыт в создании треков, желательно даже "
                                      "скинуть ссылки на твои лучшие работы!)")

        Temp[callback.from_user.id] = 'Битмейкер'

    await FSMAdmin.experience.set()


async def cm_start2(message: types.Message, state: FSMContext):
    await state.finish()
    a = str(Temp[message.from_user.id])
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace("'", "")
    Temp[message.from_user.id] = a + "  |  " + message.text
    bd_func.job(message.from_user.id, Temp[message.from_user.id])
    await message.reply("Хорошо, скоро менеджер с тобой свяжется!")


async def cm_start3(message: types.Message, state: FSMContext):

    try:
        temp = message.text.replace(' ', '')
        if 11 <= len(temp) <= 12:
            temp = message.text
            temp = temp.replace(' ', '')
            temp = temp.replace('+7', '8')
            if len(temp) == 11 and temp[0] == '8':
                await state.finish()
                await message.reply("Спасибо! Заказ принят, скоро с вами свяжется наш менеджер!)")
                bd_func.register_offers(message.from_user.id, Temp[message.from_user.id][0],
                                        Temp[message.from_user.id][1], temp)

            else:
                await FSMAdmin.number.set()
                await message.reply('Не корректный ввод, попробуй еще раз')
        else:
            await FSMAdmin.number.set()
            await message.reply('Не корректный ввод, попробуй еще раз')
    except ValueError:
        await FSMAdmin.number.set()
        await message.reply('Не корректный ввод, попробуй еще раз')


def register_handlers_login_GetOfferFSM(dp: Dispatcher):
    dp.register_callback_query_handler(cm_start, text='Collaboration_AandQ', state=None)
    dp.register_callback_query_handler(cm_start1, state=FSMAdmin.who)
    dp.register_message_handler(cm_start2, state=FSMAdmin.experience)
    dp.register_message_handler(cm_start3, state=FSMAdmin.number)
