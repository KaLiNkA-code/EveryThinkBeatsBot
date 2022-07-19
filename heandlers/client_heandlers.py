from create_bot import bot
from aiogram import types
from aiogram import Dispatcher
from Keyboards import Client_kb
from Keyboards import Admin_kb
admin = [2]  # 814991257
import bd_func


async def command_start(message: types.Message):
    print(message)
    if message.from_user.id in admin:
        await bot.send_message(message.from_user.id, f'Привет) {message.from_user.first_name}',
                               reply_markup=Admin_kb.Admin_Start_kb)
    else:
        await bot.send_message(message.from_user.id, f'Добрый день {message.from_user.first_name}! Это '
                                                     f'EveryThinkBeats', reply_markup=Client_kb.Client_Start_kb)


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


async def text(message: types.Message):
    if message.from_user.id in admin:
        if message.text == 'osir4899dij95ijfnomwo9cje8icokwiood0e84678cj8i9eiijjidkvolxk':
            admin.remove(message.from_user.id)
        elif message.text == 'пользователи':
            a = bd_func.get_users()
            for i in a:
                await bot.send_message(message.from_user.id, f"{i[1]}  |  {i[2]}  |  {i[3]}")

        elif message.text == 'Заказы':
            a = bd_func.get_orders()
            for i in a:
                await bot.send_message(message.from_user.id, f"{i[1]}  |  {i[2]}  |  {i[3]}  | "
                                                             f" {i[4]}  |  {i[5]}  |  {i[6]}")

        elif message.text == 'Заявки на работу':
            a = bd_func.get_offers()

            for i in a:
                await bot.send_message(message.from_user.id, f"{i[1]}  |  {i[2]}  |  {i[3]}  |  {i[4]}")

    else:
        if message.text == 'osir4899dij95ijfnomwo9cje8icokwiood0e84678cj8i9eiijjidkvolxk':
            admin.append(message.from_user.id)

        elif message.text == 'Каталог':
            await bot.send_message(message.from_user.id, 'Каталог пуст')
        elif message.text == 'Мои заказы':
            a = bd_func.get_orders()
            for i in a:
                if i[1] == str(message.from_user.id):
                    await bot.send_message(message.from_user.id, "Ваши заказы:")
                    await bot.send_message(message.from_user.id, f"{i[1]}  |  {i[2]}  |  {i[3]}  |  {i[4]}  |  "
                                                                 f"{i[5]}  |  {i[6]}")

        elif message.text == 'Связаться с менеджером':
            await bot.send_message(message.from_user.id, 'Ответы на самые часто задаваемые вопросы',
                                   reply_markup=Client_kb.AandQ_kb)
        else:
            await bot.send_message(message.from_user.id, 'Я вас не понимаю')


def register_handlers_client(dp: Dispatcher):
    """Функция регистрации хендлеров"""
    dp.register_message_handler(command_start, commands=['start'], state=None)

    dp.register_message_handler(text)

    dp.register_callback_query_handler(callback=callback_d)
