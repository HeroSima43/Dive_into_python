# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import decimal
import math
decimal.getcontext().prec = 50

diametr = decimal.Decimal(input('Введите диаметр окружности: '))

STOP_DIAMETR = 1000

if diametr <= STOP_DIAMETR:
    square = decimal.Decimal(math.pi) * (diametr / 2)**2
    print(square)
    line = decimal.Decimal(math.pi) * diametr
    print(line)
else:
    print('Вы ввели число вне диапазона')
