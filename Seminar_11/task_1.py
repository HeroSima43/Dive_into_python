# Задание №1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

import time


class MyStr(str):

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance


sss = MyStr('Hello World', 'Athor')

print(sss)
print(sss.name)
print(sss.time)
print(sss.upper())
