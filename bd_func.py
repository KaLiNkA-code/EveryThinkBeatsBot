import xlsxwriter
import psycopg2
import os

admin = [1]


conn = psycopg2.connect(os.environ.get("DATABASE_URL", "postgresql://test:test@localhost:5432/test"))

# conn = psycopg2.connect(dbname='postgres', user='postgres',
#                         password='2108Wert', host='localhost')


cursor = conn.cursor()

"""Создание таблиц"""
cursor.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, user_id_tg VARCHAR ( 50 ) UNIQUE NOT NULL, "
               "name VARCHAR ( 50 ), phone VARCHAR ( 50 ), where_know VARCHAR ( 100 ), work VARCHAR ( 1000 ) );")

cursor.execute('CREATE TABLE IF NOT EXISTS orders (id serial PRIMARY KEY, user_id_tg VARCHAR ( 50 ) UNIQUE NOT NULL, '
               'bit VARCHAR ( 50 ), recording VARCHAR ( 50 ), mixing VARCHAR ( 50 ), platforms VARCHAR ( 50 ), '
               'about VARCHAR ( 2000 ), numbers VARCHAR ( 15 ), price VARCHAR ( 50 ));')


def register_user(tg_id, name, phone, where_know):
    cursor.execute("INSERT INTO USERS(user_id_tg, name, phone, where_know, work) VALUES('{0}', '{1}', '{2}', "
                   "'{3}', '{4}');".format(tg_id, name, phone, where_know, '0'))


def register_order(user_id_tg, bit, recording, mixing, platforms, about, price):
    cursor.execute("INSERT INTO orders(user_id_tg, bit, recording, mixing, platforms, about, price)"
                   " VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');".format
                   (user_id_tg, bit, recording, mixing, platforms, about, price))


def register_offers(user_id_tg, who, about, phone):
    cursor.execute("INSERT INTO offers(user_id_tg, who, about, phone)"
                   " VALUES('{0}', '{1}', '{2}', {3});".format(user_id_tg, who, about, str(phone)))


def job(tg_id, text):
    cursor.execute("UPDATE users SET work='{0}' WHERE user_id_tg='{1}'".format(text, tg_id))


def check_user_exists(tg_id):
    """Проверка существования юзера"""
    cursor.execute("SELECT * FROM users WHERE user_id_tg = " + tg_id + ";")
    try:
        res = cursor.fetchall()[0]
    except:
        return False
    else:
        return True


def get_ids_of_users():
    """Получение списка всех юзеров"""
    cursor.execute("SELECT user_id_tg FROM users;")
    return [i[0] for i in cursor.fetchall()]


def get_users():
    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()


def get_offers():
    cursor.execute("SELECT * FROM users WHERE work != '0';")
    return cursor.fetchall()


def get_orders():
    #  cursor.execute("SELECT * FROM users WHERE work != '0';")

    cursor.execute("SELECT * FROM orders;")
    return cursor.fetchall()


"""//////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


def export_users(d_users):
    workbook = xlsxwriter.Workbook('output.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    column = 0

    worksheet.write(row, column, "user_id")
    worksheet.write(row, column + 1, "Номер телефон")
    worksheet.write(row, column + 2, "Почта")
    worksheet.write(row, column + 3, "Откуда узнал/Отзыв")
    worksheet.write(row, column + 4, "Откуда узнал/Отзыв")

    row += 1

    for i in d_users.keys():
        content = d_users[i]
        for item in [i] + content:
            worksheet.write(row, column, item)
            column += 1
        column = 0
        row += 1

    workbook.close()
