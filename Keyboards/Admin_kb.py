from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


Admin_Start_kb = ReplyKeyboardMarkup(row_width=1)
Admin_Start_b1 = KeyboardButton(text='Выставить бит')
Admin_Start_b2 = KeyboardButton(text='Заказы')
Admin_Start_b3 = KeyboardButton(text='Заявки на работу')
Admin_Start_b4 = KeyboardButton(text='пользователи')
Admin_Start_kb.add(Admin_Start_b1, Admin_Start_b2, Admin_Start_b3, Admin_Start_b4)

Yes_No_kb = InlineKeyboardMarkup()
Yes = InlineKeyboardButton(callback_data='Yes', text='Да')
No = InlineKeyboardButton(callback_data='No', text='Нет')
Yes_No_kb.add(Yes, No)

call_manager_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Менеджер',
                                                                  url='https://web.telegram.org/z/#814991257'))
