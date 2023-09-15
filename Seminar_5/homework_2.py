# Задача 2.
# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

def generate_dict(names_list, salary_list, bonus_list):
    return {name: salary * (float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salary_list, bonus_list)}


names = ["Александр", "Владимир", "Иван"]
salary = [100000, 150000, 200000]
bonus = ["10.25%", "15.50%", "20.75%"]

salary_dict = generate_dict(names, salary, bonus)
print(salary_dict)
