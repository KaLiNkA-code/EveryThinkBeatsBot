from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram import Dispatcher
from Keyboards import Client_kb
from create_bot import bot
import bd_func
from bd_func import admin
Temp = {}
Temp_price = {}


class FSMAdmin(StatesGroup):
    bit = State()
    recording = State()
    compilation = State()
    unload = State()
    numbers = State()


async def CreateOrdering_start(message: types.Message):
    """Проверка на сущ. юзера и получение имени"""
    if bd_func.check_language(message.from_user.id):
        await message.reply('Тебе нужен бит? (390р)', reply_markup=Client_kb.Yes_No_kb)
    else:
        await message.reply('Do you need a bit? ($15)', reply_markup=Client_kb.Yes_No_ENG_kb)
    await FSMAdmin.bit.set()


async def CreateOrdering_bit(callback: types.CallbackQuery, state: FSMContext):
    try:
        if callback.data == 'Yes':
            Temp[callback.from_user.id] = ['бит нужен']
            Temp_price[callback.from_user.id] = 390
            await bot.send_message(callback.from_user.id, 'Хорошо, нужна ли запись голоса на профессиональной'
                                                          ' студии со звукорежиссер?  (1490р /час) ',
                                   reply_markup=Client_kb.Yes_No_kb)
            await FSMAdmin.recording.set()
        elif callback.data == 'No':
            Temp_price[callback.from_user.id] = 0
            await bot.send_message(callback.from_user.id, 'Хорошо, нужна ли запись голоса на профессиональной'
                                                          ' студии со звукорежиссер?  (1490р /час) ',
                                   reply_markup=Client_kb.Yes_No_kb)
            Temp[callback.from_user.id] = ['бит не нужен']
        elif callback.data == 'Y':
            Temp[callback.from_user.id] = ['bit is needed']
            Temp_price[callback.from_user.id] = 15
            await bot.send_message(callback.from_user.id, 'Okay, is it necessary to record your voice in a '
                                                          'professional studio with a sound engineer? ($125 an hour)',
                                   reply_markup=Client_kb.Yes_No_ENG_kb)
        else:
            Temp[callback.from_user.id] = ["bit is not needed"]
            Temp_price[callback.from_user.id] = 0
            await bot.send_message(callback.from_user.id, 'Okay, is it necessary to record your voice in a '
                                                          'professional studio with a sound engineer? ($125 an hour)',
                                   reply_markup=Client_kb.Yes_No_ENG_kb)

        await FSMAdmin.recording.set()
    except:
        await state.finish()
        await bot.send_message(callback.from_user.id, 'Заказ отменен!')


async def CreateOrdering_recording(callback: types.CallbackQuery, state: FSMContext):
    try:
        if callback.data == 'Yes':
            Temp[callback.from_user.id] += ['Запись нужна']
            Temp_price[callback.from_user.id] = int(Temp_price[callback.from_user.id]) + 1490
            await bot.send_message(callback.from_user.id, 'Нужно ли тебе сведение? (490р)',
                                   reply_markup=Client_kb.Yes_No_kb)
            await FSMAdmin.compilation.set()
        elif callback.data == 'No':
            Temp[callback.from_user.id] += ['Запись не нужна']
            await bot.send_message(callback.from_user.id, 'Нужно ли тебе сведение? (490р)',
                                   reply_markup=Client_kb.Yes_No_kb)
            await FSMAdmin.compilation.set()

        elif callback.data == 'Y':
            Temp[callback.from_user.id] += ['record is needed']
            Temp_price[callback.from_user.id] = int(Temp_price[callback.from_user.id]) + 125
            await bot.send_message(callback.from_user.id, 'Do you need a mix? ($19)',
                                   reply_markup=Client_kb.Yes_No_ENG_kb)
            await FSMAdmin.compilation.set()
        else:
            Temp[callback.from_user.id] += ['a record is not needed']
            await bot.send_message(callback.from_user.id, 'Do you need a mix? ($19)',
                                   reply_markup=Client_kb.Yes_No_ENG_kb)
            await FSMAdmin.compilation.set()

    except:
        await state.finish()
        await bot.send_message(callback.from_user.id, 'Заказ отменен!')


async def CreateOrdering_compilation(callback: types.CallbackQuery, state: FSMContext):
    try:
        if callback.data == 'Yes':
            Temp_price[callback.from_user.id] = int(Temp_price[callback.from_user.id]) + 490
            Temp[callback.from_user.id] += ['сведение нужно']
            await bot.send_message(callback.from_user.id, 'Нужна ли помощь в выгрузки трека на музыкальные '
                                                          'платформы? (590р)',
                                   reply_markup=Client_kb.Yes_No_kb)
        elif callback.data == 'No':
            Temp[callback.from_user.id] += ['сведение не нужно']
            await bot.send_message(callback.from_user.id, 'Нужна ли помощь в выгрузки трека на музыкальные '
                                                          'платформы? (590р)',
                                   reply_markup=Client_kb.Yes_No_kb)

        elif callback.data == 'Y':
            Temp_price[callback.from_user.id] = int(Temp_price[callback.from_user.id]) + 19
            Temp[callback.from_user.id] += ['mixing is needed']
            await bot.send_message(callback.from_user.id, 'Do you need help uploading your track to music '
                                                          'platforms? ($15)',
                                   reply_markup=Client_kb.Yes_No_ENG_kb)
        else:
            Temp[callback.from_user.id] += ['mixing is not needed']
            await bot.send_message(callback.from_user.id, 'Do you need help uploading your track to music '
                                                          'platforms? ($15)',
                                   reply_markup=Client_kb.Yes_No_ENG_kb)

        await FSMAdmin.unload.set()
    except:
        await state.finish()
        await bot.send_message(callback.from_user.id, 'Заказ отменен!')


async def CreateOrdering_unload(callback: types.CallbackQuery, state: FSMContext):
    try:
        if callback.data == 'Yes':
            Temp_price[callback.from_user.id] = int(Temp_price[callback.from_user.id]) + 590
            Temp[callback.from_user.id] += ['нужно выгружать на платформы']
            await bot.send_message(callback.from_user.id, 'Есть ли какие то пожелания для твоего заказа?')
            await FSMAdmin.numbers.set()
        elif callback.data == 'No':
            Temp[callback.from_user.id] += ['не нужно выгружать на платформы']
            await bot.send_message(callback.from_user.id, 'Есть ли какие то пожелания для твоего заказа?')
            await FSMAdmin.numbers.set()
        if callback.data == 'Y':
            Temp_price[callback.from_user.id] = int(Temp_price[callback.from_user.id]) + 15
            Temp[callback.from_user.id] += ['need to unload on the platforms']
            await bot.send_message(callback.from_user.id, 'Are there any wishes for your order?')
            await FSMAdmin.numbers.set()
        else:
            Temp[callback.from_user.id] += ['no need to unload on platforms']
            await bot.send_message(callback.from_user.id, 'Are there any wishes for your order?')
            await FSMAdmin.numbers.set()

    except:
        await state.finish()
        await bot.send_message(callback.from_user.id, 'Заказ отменен!')


async def CreateOrdering_number(message: types.Message, state: FSMContext):
    try:
        if Temp_price[message.from_user.id] == 0:
            if bd_func.check_language(message.from_user.id):
                bot.send_message(message.from_user.id, 'Понятно! Заказ не принят. Когда вам понадобится сделать трек, '
                                                       'вы знаете, где нас искать)')
            else:
                bot.send_message(message.from_user.id, 'Got it! The order is not accepted. When you need to make a '
                                                       'track, you know where to find us)')
            bot.send_message(message.from_user.id, '🤠')
            await state.finish()

        bd_func.register_order(message.from_user.id, Temp[message.from_user.id][0],
                               Temp[message.from_user.id][1], Temp[message.from_user.id][2],
                               Temp[message.from_user.id][3], message.text, Temp_price[message.from_user.id])

        if bd_func.check_language(message.from_user.id):
            await bot.send_message(message.from_user.id, f'Супер, заказ принят! Примерная стоимость: '
                                                        f'{Temp_price[message.from_user.id]}р.')
        else:
            await bot.send_message(message.from_user.id, f'Great, order taken! Approximate cost: '
                                                         f'${Temp_price[message.from_user.id]}')

    except BaseException as f:
        await state.finish()
        await bot.send_message(message.from_user.id, 'Пожалуйста, воспользуйся вводом с кнопок')
        await bot.send_message(814991257, f)

    await state.finish()
    Temp_price[message.from_user.id] = 0
    try:
        for i in admin:
            await bot.send_message(i, 'У нас новый заказ!')
    except:
        pass


def register_handlers_login(dp: Dispatcher):
    dp.register_message_handler(CreateOrdering_start, text='Сделать заказ', state=None)
    dp.register_message_handler(CreateOrdering_start, text='Place an order', state=None)
    dp.register_callback_query_handler(CreateOrdering_bit, state=FSMAdmin.bit)
    dp.register_callback_query_handler(CreateOrdering_recording, state=FSMAdmin.recording)
    dp.register_callback_query_handler(CreateOrdering_compilation, state=FSMAdmin.compilation)
    dp.register_callback_query_handler(CreateOrdering_unload, state=FSMAdmin.unload)
    dp.register_message_handler(CreateOrdering_number, state=FSMAdmin.numbers)
