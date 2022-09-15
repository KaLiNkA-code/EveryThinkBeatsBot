from create_bot import bot
from aiogram import types
from aiogram import Dispatcher
from Keyboards import Client_kb
from FSM.CreateOrderingFSM import Temp_price
import bd_func
from bd_func import admin  # 814991257
total_value = 0


async def callback_d(callback: types.CallbackQuery):
    if callback.data == 'Manager_AandQ':
        await bot.send_message(callback.from_user.id, '@KaLiNkA_77', reply_markup=Client_kb.call_manager_kb)
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    elif callback.data == 'Collaboration_AandQ':
        await bot.send_message(callback.from_user.id, 'Ok')

        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    elif callback.data == 'Payment_AandQ':
        await bot.send_message(callback.from_user.id, 'Об оплате', reply_markup=Client_kb.AandQ_Payment_kb)
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    elif callback.data == 'Order_AandQ':
        await bot.send_message(callback.from_user.id, 'О Заказе', reply_markup=Client_kb.AandQ_order_kb)
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

    elif callback.data == 'Edits_Order_AandQ':
        await bot.send_message(callback.from_user.id, 'Если вы хотите изменить детали заказа то об этом необходимо '
                                                      'сообщить менеджеру. \n\nНезначительные правки бесплатны. '
                                                      'Если правки значительно меняют изначальный заказ то за это '
                                                      'придется доплатить и(или) были сообщены уже после ознакомления с'
                                                      ' демонстационной версией то придется доплатить. Стоимость вам '
                                                      'сообщит менеджер.\n@KaLiNkA_77',
                               reply_markup=Client_kb.call_manager_kb)
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

    elif callback.data == 'time_Order_AandQ':
        await bot.send_message(callback.from_user.id, 'Время выполнения зависит от сложности вашего заказа, обычно '
                                                      'на его выполнение уходит от 1 до 5 рабочих дней. \n\n'
                                                      'Если ваш заказ слишком объемный то приблизительное время '
                                                      'выполнения вам сообщит менеджер.\n@KaLiNkA_77',
                               reply_markup=Client_kb.call_manager_kb)
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

    elif callback.data == 'guarantees_Payment_AandQ':
        await bot.send_message(callback.from_user.id, 'Мы не берем 100% предоплату. \nМы берем 50% после демо версии '
                                                      'вашего заказа, и остальные 50% уже после полного выполнения.',
                               reply_markup=Client_kb.call_manager_kb)
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

    elif callback.data == 'methods_Payment_AandQ':
        await bot.send_message(callback.from_user.id, 'Оплату мы принимаем только на карту',
                               reply_markup=Client_kb.call_manager_kb)
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

    else:
        await bot.send_message(callback.from_user.id, 'Хм, какая странная кнопка')


async def help_func(message: types.Message):
    await bot.send_message(message.from_user.id, 'Давай познакомимся с интерфейсом:'
                                                 '\nВ каталоге ты найдешь лучшие наши проекты'
                                                 '\nЧтобы сделать заказ, нужно просто нажать соответствущую кнопку'
                                                 '\nЧтобы Ответить на все остальные вопросы, нажмите Связаться с '
                                                 'менеджером. Там присутствуют самые частозадаваемые вопросы')


async def text(message: types.Message):
    global total_value
    if message.from_user.id in admin:


        try:
            a = int(message.text)
            total_value += a
        except:
            pass

        if message.text == 'osir4899dij95ijfnomwo9cje8icokwiood0e84678cj8i9eiijjidkvolxk':
            admin.remove(message.from_user.id)

        elif message.text == 'Заработок':
            await bot.send_message(message.from_user.id, '🤑')
            await bot.send_message(message.from_user.id, f'За все время мы заработали: {total_value}')

        elif message.text == 'Статистика':
            a = bd_func.get_ids_of_users()
            total_price = 0
            for i in Temp_price.values():
                total_price += int(i)
            await bot.send_message(message.from_user.id, f'Всего пользователей: {len(a)}')

        elif message.text == 'Заказы':
            a = bd_func.get_orders()  # id, user_id_tg, bit, recording, mixing , platforms, about, numbers, price
            b = bd_func.get_users()
            x = 0
            for order in a:
                for user in b:
                    if order[1] == user[1]:
                        x += 1
                        await bot.send_message(message.from_user.id,
                                               f"{order[1]}  |  {order[2]}  |  {order[3]}  |  {order[4]}  |  "
                                               f"{order[5]}  |  {order[6]}  |  {user[3]}  |  {order[8]}р.")
            if x == 0:
                await bot.send_message(message.from_user.id, "Заказов нету")

        elif message.text == 'Заявки на работу':
            a = bd_func.get_offers()
            x = 0
            for i in a:
                x += 1
                await bot.send_message(message.from_user.id, f"{i[1]}  |  {i[2]}  |  {i[3]}  |  {i[5]}")

            if x == 0:
                await bot.send_message(message.from_user.id, "Заявок на работу нет)")

        elif message.text == 'Пользователи':
            await bot.send_message(message.from_user.id, "🤩")
            a = bd_func.get_users()
            if a:

                for i in a:
                    print(type(i[1]))
                    print(type(message.from_user.id))
                    await bot.send_message(message.from_user.id, f"{i[1]}  |  {i[2]}  |  {i[3]}  |  {i[4]}")
            else:
                await bot.send_message(message.from_user.id, "Пользователей нету")

    else:
        if message.text == 'osir4899dij95ijfnomwo9cje8icokwiood0e84678cj8i9eiijjidkvolxk':
            admin.append(message.from_user.id)

        elif message.text == 'Каталог':

            await bot.send_message(message.from_user.id, 'Снипеты наших последних проектов:')
            await bot.send_audio(message.chat.id, open('data/Ever.mp3', 'rb'))

        elif message.text == 'Мои заказы':
            a = bd_func.get_orders()
            x = 0
            await bot.send_message(message.from_user.id, "🤖")
            for i in a:
                if i[1] == str(message.from_user.id):
                    if x == 0:
                        await bot.send_message(message.from_user.id, "Ваши заказы:")
                    x += 1
                    await bot.send_message(message.from_user.id, f"{i[2]}  |  {i[3]}  |  {i[4]}  |  "
                                                                 f"{i[5]}  |  {i[6]}  |  {i[7]}")
            if x == 0:
                await bot.send_message(message.from_user.id, "Заказов пока что нет. Хотите сделать заказ?")

        elif message.text == 'Связаться с менеджером':
            await bot.send_message(message.from_user.id, 'Ответы на самые часто задаваемые вопросы',
                                   reply_markup=Client_kb.AandQ_kb)
        else:
            await bot.send_message(message.from_user.id, 'Я вас не понимаю')


def register_handlers_client(dp: Dispatcher):
    """Функция регистрации хендлеров"""
    dp.register_message_handler(help_func, commands=['help'], state=None)
    dp.register_message_handler(text)
    dp.register_callback_query_handler(callback=callback_d)
