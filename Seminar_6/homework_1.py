# Задача 1.
# В модуль с проверкой даты добавьте возможность запуска в терминале
# с передачей даты на проверку.

from sys import argv


def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def check_date(date):
    day, month, year = map(int, date.split('.'))
    if day < 1 or day > 31 or \
        month < 1 or month > 12 or \
            year < 1 or year > 9999:
        return False
    if month == 2 and day > 28 and not leap_year(year):
        return False
    if month == 2 and day > 29 and leap_year(year):
        return False
    if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        return False
    return True


print(check_date(str(*argv[1:])))
