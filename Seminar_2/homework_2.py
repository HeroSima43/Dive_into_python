# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))


def binary(num):
    digits = '0123456789ABCDEF'
    res = ''
    while num > 0:
        res = digits[num % 16] + res
        num = num // 16
    return res


print(binary(num))
print(hex(num))
