# Задание №2
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случая

a = input('Введите что нибудь ')
if a.isdigit():
    print(int(a))
elif a.replace(".", "", 1).replace("-", "", 1).isdigit():
    print(float(a))
else:
    if a != a.lower():
        a = a.lower()
    else:
        a = a.upper()
    print(a)
