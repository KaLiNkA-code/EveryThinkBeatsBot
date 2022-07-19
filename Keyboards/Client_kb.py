from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


Client_Start_kb = ReplyKeyboardMarkup(row_width=1)
Client_Start_b1 = KeyboardButton(text='Каталог')
Client_Start_b2 = KeyboardButton(text='Сделать заказ')
Client_Start_b3 = KeyboardButton(text='Мои заказы')
Client_Start_b4 = KeyboardButton(text='Связаться с менеджером')
Client_Start_kb.add(Client_Start_b1, Client_Start_b2, Client_Start_b3, Client_Start_b4)


Yes_No_kb = InlineKeyboardMarkup()
Yes = InlineKeyboardButton(callback_data='Yes', text='Да')
No = InlineKeyboardButton(callback_data='No', text='Нет')
Yes_No_kb.add(Yes, No)

call_manager_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Менеджер',
                                                                  url='https://web.telegram.org/z/#814991257'))

AandQ_kb = InlineKeyboardMarkup(row_width=1)
AandQ_b1 = InlineKeyboardButton(callback_data='Order_AandQ', text='О заказе')
AandQ_b2 = InlineKeyboardButton(callback_data='Payment_AandQ', text='Об оплате')
AandQ_b3 = InlineKeyboardButton(callback_data='Collaboration_AandQ', text='Сотрудничество')
AandQ_b4 = InlineKeyboardButton(callback_data='Manager_AandQ', text='Вызвать менеджера')
AandQ_kb.add(AandQ_b1, AandQ_b2, AandQ_b3, AandQ_b4)

AandQ_order_kb = InlineKeyboardMarkup(row_width=1)
AandQ_order_b1 = InlineKeyboardButton(callback_data='Edits_Order_AandQ', text='Правки')
AandQ_order_b2 = InlineKeyboardButton(callback_data='time_Order_AandQ', text='Время выполнения')
AandQ_order_kb.add(AandQ_order_b1, AandQ_order_b2)

AandQ_Payment_kb = InlineKeyboardMarkup(row_width=1)
AandQ_Payment_b1 = InlineKeyboardButton(callback_data='guarantees_Payment_AandQ', text='Правки')
AandQ_Payment_b2 = InlineKeyboardButton(callback_data='methods_Payment_AandQ', text='способ оплаты')
AandQ_Payment_kb.add(AandQ_Payment_b1, AandQ_Payment_b2)

FSM_reg_kb1 = InlineKeyboardMarkup(row_width=3)
FSM_reg_b1 = InlineKeyboardButton(callback_data='1', text='1')
FSM_reg_b2 = InlineKeyboardButton(callback_data='2', text='2')
FSM_reg_b3 = InlineKeyboardButton(callback_data='3', text='3')
FSM_reg_b4 = InlineKeyboardButton(callback_data='4', text='4')
FSM_reg_b5 = InlineKeyboardButton(callback_data='5', text='5')
FSM_reg_b6 = InlineKeyboardButton(callback_data='6', text='6')
FSM_reg_kb1.add(FSM_reg_b1, FSM_reg_b2, FSM_reg_b3, FSM_reg_b4, FSM_reg_b5, FSM_reg_b6)
