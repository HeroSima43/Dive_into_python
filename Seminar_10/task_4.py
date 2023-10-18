# Задание №4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○  шестизначный идентификационный номер
# ○  уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from task_3 import Person
from random import randint as rnd


class Employee(Person):
    def __init__(self, name, surname, father_name, age, sex, identification):
        super().__init__(name, surname, father_name, age, sex)
        self.identification = identification
        self.access = self.get_access()

    def get_access(self):
        summa = 0
        for i in str(self.identification):
            summa += int(i)
        return summa % 7


e1 = Employee('Иван', 'Ivanov', 'Ivanovich', 30, 'M', rnd(100000, 999999))
e2 = Employee('Maria', 'Sergeevna', 'Sergeeva', 20, 'F', rnd(100000, 999999))
print(e1.access)
print(e2.access)
print(e1.identification)
print(e2.identification)
