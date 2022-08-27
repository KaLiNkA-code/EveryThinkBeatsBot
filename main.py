from aiogram.utils import executor
from create_bot import dp
from heandlers.client_heandlers import register_handlers_client
from FSM.CreateOrderingFSM import register_handlers_login
from FSM.GetOfferFSM import register_handlers_login_GetOfferFSM
from FSM.NotificationsFSM import register_handlers_Notification
from FSM.RegisterFSM import register_handlers_register


def on_startup():
    print('Бот вышел в online')


register_handlers_register(dp)
register_handlers_Notification(dp)
register_handlers_login_GetOfferFSM(dp)
register_handlers_login(dp)
register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup())  # Команда запуска бота
