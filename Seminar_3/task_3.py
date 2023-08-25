# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = (1, 'apple', 3.14, 'banan', 42, 2.71, 'mango', True, False)

result = {}

for item in my_tuple:
    result.setdefault(type(item).__name__, []).append(item)

print(result)
