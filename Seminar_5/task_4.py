# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

my_list = []
for i in range(0, 100, 2):
    if i % 10 + i // 10 != 8:
        my_list.append(i)

print(my_list)

my_gena = (i for i in range(0, 100, 2) if i % 10 + i // 10 != 8)
print(*my_gena)
