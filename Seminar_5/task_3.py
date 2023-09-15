# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

my_text = 'Проводите уроки, вебинары и встречи, анализируйте поведение людей и улучшайте качество вашего контента'

my_dic = {i: ord(i) for i in my_text}

print(my_dic, end='\n\n')

my_iter = iter(my_dic.items())

for _ in range(0, 5):
    print(*next(my_iter))
