from os import system
from time import sleep

import psycopg2

system('cls')
DB = 'ppostgres'
USER = 'postgres'
HOST = 'localhost'
PORT = 5432
PASSWORD = '****'

ask_login = input("Siz account yaratganmisiz. H yoki h -> ")
if ask_login.lower() == 'h': exit()


register_name = input("Username kiriting -> ")
register_email = input("Email kiriting (Qo'shimcha xavfsizlik uchun!) -> ")
register_password = input("Parol yarating: ")

connection = psycopg2.connect(database=DB, user=USER, password=PASSWORD, host=HOST, port=PORT)
cur = connection.cursor()


cur.execute("CREATE TABLE register (Username VARCHAR(20), Email VARCHAR(30), Password VARCHAR(18));")

check_db = cur.execute(f"SELECT EXISTS (SELECT * FROM register WHERE username = '{register_name}');")

x = cur.fetchall()[0][0]
if x:
    print("Bu login Bazada mavjud!"); exit()

cur.execute(f"INSERT INTO register VALUES ('{register_name}', '{register_email}', '{register_password}');")
sleep(0.5)
print("Ma'lumotlar kiritildi!\n  Dasturdan foydalanishingiz mumkin!")
connection.commit()
sleep(0.4)


print("'To Do App'ga malumot kiritayapsiz!")
sleep(0.2)
todo_title = input("Sarlavha(title) kiriting -> ")
sleep(0.3)
todo_text = input("""Endi titlega matn qo'shsangiz bo'ladi. (Bu Maqola yoki biron kerakli matn bo'lishi mumkin) -> """)
cur.execute("CREATE TABLE IF NOT EXISTS ToDo_App (Title VARCHAR(40), text_title TEXT, create_date TIME);")
cur.execute(f"INSERT INTO ToDo_App VALUES ('{todo_title}', '{todo_text}', now());")

connection.commit()

print("""
1 - register bazani ko'rish.
2 - To Do bazani ko'rish
3 - Login parolni o'zgartirish.

0 - dasturdan chiqish
""")
system('cls')
sleep(0.2)



ask_view = int(input("0 dan 3 gacha raqam kiriting: "))
if ask_view == 1:
    cur.execute("SELECT * FROM register;")
    print(cur.fetchall())
elif ask_view == 2:
    cur.execute("SELECT * FROM ToDo_App;")
    print(cur.fetchall())
elif ask_view == 3:
    print('Keyingi versiyada bu funksiya ishga tushadi!')
else:
    exit()

