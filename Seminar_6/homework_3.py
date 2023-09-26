# Задача 3.
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

import random
from homework_2 import queen_placement


def generate_positions():
    x = list(range(1, 9))
    y = list(range(1, 9))
    for _ in range(4):
        random.shuffle(x)
        random.shuffle(y)
        while not queen_placement(x, y):
            random.shuffle(x)
            random.shuffle(y)
        print(x, y)


generate_positions()
