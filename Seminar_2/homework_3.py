# Напишите программу, которая принимает две строки вида “a/b”
#  - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

str_1 = input("Введите первую дробь: ")
str_2 = input("Введите вторую дробь: ")


def fraction_sum(str_1, str_2):
    a_1, b_1 = map(int, str_1.split('/'))
    a_2, b_2 = map(int, str_2.split('/'))
    sum_a = a_1 * b_2 + a_2 * b_1
    sum_b = b_1 * b_2
    return str(sum_a) + '/' + str(sum_b)


def fraction_prod(str_1, str_2):
    a_1, b_1 = map(int, str_1.split('/'))
    a_2, b_2 = map(int, str_2.split('/'))
    prod_a = a_1 * a_2
    prod_b = b_1 * b_2
    return str(prod_a) + '/' + str(prod_b)


f_1 = fractions.Fraction(str_1)
f_2 = fractions.Fraction(str_2)
print(f"Сумма дробей {str_1} и {str_2} равняется {fraction_sum(str_1, str_2)}")
print(f'Проверка: {f_1 + f_2}')

print(f"Произведение дробей {str_1} и {str_2} равняется {fraction_prod(str_1, str_2)}")
print(f'Проверка: {f_1 * f_2}')
