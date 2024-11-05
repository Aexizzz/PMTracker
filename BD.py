import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('Projects.db')
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(len(cursor.fetchall()))