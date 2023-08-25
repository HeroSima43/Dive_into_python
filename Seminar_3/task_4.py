# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 1, 1, 1, 2, 2, 2, 4, 4, 5, 7, 45, 45]

for item in set(my_list):
    if my_list.count(item) == 2:
        my_list.remove(item)
        my_list.remove(item)
print(my_list)
