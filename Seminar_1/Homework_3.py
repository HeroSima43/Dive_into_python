# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint
num = randint(0, 1000)
print(num)
n = 10  # Число попыток

while n > 0:
    a = int(input('Ваше число: '))
    n -= 1
    if num == a:
        print('Вы угадали число!')
        break
    elif n == 0:
        print(f'Вы проиграли, загаданное число было {num}')
    elif num > a:
        print(f'Загаданное число больше {a}. Осталось попыток: {n}')
    elif num < a:
        print(f'Загаданное число меньше {a}. Осталось попыток: {n}')