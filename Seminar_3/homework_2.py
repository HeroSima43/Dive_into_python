# Задание 2.
# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 1, 1, 1, 2, 2, 2, 4, 4, 5, 7]
my_list = list(set([x for x in my_list if my_list.count(x) > 1]))
print(my_list)