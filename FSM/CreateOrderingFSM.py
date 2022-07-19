from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram import Dispatcher
from Keyboards import Client_kb
from create_bot import bot
import bd_func
Temp = {}


class FSMAdmin(StatesGroup):
    bit = State()
    recording = State()
    compilation = State()
    unload = State()
    wishes = State()


async def CreateOrdering_start(message: types.Message):
    """Проверка на сущ. юзера и получение имени"""
    await message.reply('Вам нужен бит?', reply_markup=Client_kb.Yes_No_kb)
    await FSMAdmin.bit.set()


async def CreateOrdering_bit(callback: types.CallbackQuery):
    try:
        if callback.data == 'Yes':
            Temp[callback.from_user.id] = ['бит нужен']
            await bot.send_message(callback.from_user.id, 'Хорошо, нужна ли запись голоса на профессиональной студии?',
                                   reply_markup=Client_kb.Yes_No_kb)
            await FSMAdmin.recording.set()
        else:
            Temp[callback.from_user.id] = ['бит не нужен']
            await bot.send_message(callback.from_user.id, 'Хорошо, нужна ли запись голоса на профессиональной студии?',
                                   reply_markup=Client_kb.Yes_No_kb)
            await FSMAdmin.recording.set()
    except AttributeError:
        await FSMAdmin.bit.set()
        await bot.send_message(callback.from_user.id, 'Пожалуйста, воспользуйтесь вводом с кнопок')


async def CreateOrdering_recording(callback: types.CallbackQuery):
    try:
        if callback.data == 'Yes':
            Temp[callback.from_user.id] += ['Запись нужна']
            await bot.send_message(callback.from_user.id, 'Нужно ли тебе сведение?',
                                   reply_markup=Client_kb.Yes_No_kb)
            await FSMAdmin.compilation.set()
        else:
            Temp[callback.from_user.id] += ['Запись не нужна']
            await bot.send_message(callback.from_user.id, 'Нужно ли тебе сведение?',
                                   reply_markup=Client_kb.Yes_No_kb)
            await FSMAdmin.compilation.set()

    except AttributeError:
        await FSMAdmin.recording.set()
        await bot.send_message(callback.from_user.id, 'Пожалуйста, воспользуйтесь вводом с кнопок')


async def CreateOrdering_compilation(callback: types.CallbackQuery):
    try:
        if callback.data == 'Yes':
            Temp[callback.from_user.id] += ['сведение нужно']
            await bot.send_message(callback.from_user.id, 'Нужна ли помощь в выгрузки музыки на музыкальные платформы?',
                                   reply_markup=Client_kb.Yes_No_kb)
            await FSMAdmin.unload.set()
        else:
            Temp[callback.from_user.id] += ['сведение не нужно']
            await bot.send_message(callback.from_user.id, 'Нужна ли помощь в выгрузки музыки на музыкальные платформы?',
                                   reply_markup=Client_kb.Yes_No_kb)
            await FSMAdmin.unload.set()

    except AttributeError:
        await FSMAdmin.compilation.set()
        await bot.send_message(callback.from_user.id, 'Пожалуйста, воспользуйтесь вводом с кнопок')


async def CreateOrdering_unload(callback: types.CallbackQuery):
    try:
        if callback.data == 'Yes':
            Temp[callback.from_user.id] += ['нужно выгружать на платформы']
            await bot.send_message(callback.from_user.id, 'Есть ли какие то пожелания для вашего заказа?')
            await FSMAdmin.wishes.set()
        else:
            Temp[callback.from_user.id] += ['нужно выгружать на платформы']
            await bot.send_message(callback.from_user.id, 'Есть ли какие то пожелания для вашего заказа?')
            await FSMAdmin.wishes.set()

    except AttributeError:
        await FSMAdmin.unload.set()
        await bot.send_message(callback.from_user.id, 'Пожалуйста, напишите свои пожелания!')


async def CreateOrdering_wishes(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Спасибо! ваш заказ принят!')
    bd_func.register_order(message.from_user.id, Temp[message.from_user.id][0],
                           Temp[message.from_user.id][1], Temp[message.from_user.id][2], Temp[message.from_user.id][3],
                           message.text)
    await state.finish()


def register_handlers_login(dp: Dispatcher):
    dp.register_message_handler(CreateOrdering_start, text='Сделать заказ', state=None)
    dp.register_callback_query_handler(CreateOrdering_bit, state=FSMAdmin.bit)
    dp.register_callback_query_handler(CreateOrdering_recording, state=FSMAdmin.recording)
    dp.register_callback_query_handler(CreateOrdering_compilation, state=FSMAdmin.compilation)
    dp.register_callback_query_handler(CreateOrdering_unload, state=FSMAdmin.unload)
    dp.register_message_handler(CreateOrdering_wishes, state=FSMAdmin.wishes)
