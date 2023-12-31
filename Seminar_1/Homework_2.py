# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу 
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input('Введите число: '))

while num < 0 or num > 100000:
    print('Ошибка ввода:')
    num = int(input('Повторите ввод: '))


count_divider = 0       # Счетчик делителей
divider = 0             # Делитель

while count_divider <= 2:
    divider += 1
    if num % divider == 0:
        count_divider += 1
    elif num <= divider:
        break

if count_divider <= 2:
    print(f'Число {num} является простым')
else:
    print(f'Число {num} является составным')
