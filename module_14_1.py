import sqlite3

connection = sqlite3.connect('not_telegram.db')

''' Создание объекта курсора'''
cursor = connection.cursor()

"""Создание таблицы"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('''CREATE INDEX IF NOT EXISTS ind_email on Users(email)''')
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)",
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

cursor.execute(''' UPDATE Users SET balance =500 WHERE id%2=1''')

cursor.execute('''DELETE FROM Users WHERE id%3=1''')

""" Выполнение SQL запроса"""
cursor.execute('''SELECT username,email, age, balance FROM Users WHERE age !=60''')

'''Получение всех записей'''
records = cursor.fetchall()

'''Вывод записей'''
for record in records:
    print(f'Имя: {record[0]} | Почта: {record[1]} | Возраст: {record[2]} | Баланс: {record[3]}')

connection.commit()
'''Закрытие соединения с базой данных'''
connection.close()
