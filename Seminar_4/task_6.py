# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка

def check_index(i_1, i_2, num_list):
    i_max = max(i_1, i_2) if max(i_1, i_2) < len(num_list) else len(num_list)
    i_min = min(i_1, i_2) if min(i_1, i_2) >= 0 else 0
    result = sum(num_list[i_min:i_max])
    return result


num_list = [23, 12, 2, 3, 4, 5, 45, 123, 456, 353]
index_1 = 2
index_2 = 7

print(check_index(index_1, index_2, num_list))
