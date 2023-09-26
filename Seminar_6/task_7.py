# Задание №7
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


# year = 1900
# print(leap_year(year))


def check_date(date):
    day, month, year = map(int, date.split('.'))
    if (day < 1 or day > 31 or
        month < 1 or month > 12 or
        year < 1 or year > 9999):
        return False
    if month == 2 and day > 28 and not leap_year(year):
        return False
    if month == 2 and day > 29 and leap_year(year):
        return False
    if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        return False
    return True


date = '15.13.2021'
print(check_date(date))
