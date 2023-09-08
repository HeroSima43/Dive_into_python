# Задача 4. Создайте словарь со списком вещей для похода
# в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

items = {'Одежда': 3, 'Вода': 3, 'Еда': 3, 'Аптечка': 1,
         'Спальный мешок': 4, 'Сапоги': 1, 'Топор': 2}
max_weight = 12
backpack = []

for item, weight in items.items():
    if weight <= max_weight:
        backpack.append(item)
        max_weight -= weight
print(backpack)