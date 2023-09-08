# Задание 3.
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие—1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты-3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
# Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

balance = 0
count_operation = 0
log = []
MIN_COMMISSION = 30
MAX_COMMISSION = 600
PERCENT_WITHDRAWAL = 0.015
PERCENT_COMMISSION = 0.03
WEALTH_BALANCE = 5000000


def action_choice():
    choice = input(f'Ваш баланс: {balance} \n'
                   'Выберите действие: \n'
                   '1. Пополнение \n'
                   '2. Снятие \n'
                   '3. Выйти \n')
    if choice == '1':
        return replenishment()
    elif choice == '2':
        return withdrawal()
    elif choice == '3':
        print('Окончание работы')
    else:
        print('Ошибка ввода')
        return action_choice()


def replenishment():
    global balance
    wealth_commission = wealth_fee(balance)
    balance -= wealth_commission
    amount = int(input('Введите сумму пополнения: '))
    if amount % 50 != 0:
        print(f'Вы ввели сумму не кратную 50 у.е., повторите ввод. Коммиссия за богатство {wealth_commission}. Ваш баланс: {balance}')
        return replenishment()
    else:
        return replenishment_fee(amount, wealth_commission)


def wealth_fee(balance):
    if balance > WEALTH_BALANCE:
        wealth_commission = balance * 0.1
    else:
        wealth_commission = int(0)
    return wealth_commission


def replenishment_fee(amount, wealth_commission):
    global balance
    global count_operation
    commission_2 = 0
    if count_operation >= 3:
        commission_2 = amount * PERCENT_COMMISSION
    balance += amount - commission_2
    return balance, print(f'Коммиссия за пополнение: {commission_2}. Коммиссия за богатство {wealth_commission}. Ваш баланс: {balance} \n'), log_operations(amount)


def withdrawal():
    global balance
    wealth_commission = wealth_fee(balance)
    balance -= wealth_commission
    amount = int(input('Введите сумму снятия: '))
    if amount % 50 != 0:
        print(f'Вы ввели сумму не кратную 50 у.е., повторите ввод. Коммиссия за богатство {wealth_commission}. Ваш баланс: {balance}')
        return withdrawal()
    elif amount > balance:
        print(f'Сумма снятия {amount} превышает Ваш баланс {balance}. Коммиссия за богатство {wealth_commission}')
        return withdrawal()
    else:
        return withdrawal_fee(amount, wealth_commission)


def withdrawal_fee(amount, wealth_commission):
    global balance
    global count_operation
    commission_2 = 0
    if count_operation >= 3:
        commission_2 = amount * PERCENT_COMMISSION
    if amount * PERCENT_WITHDRAWAL < 30:
        commission = MIN_COMMISSION
        balance -= amount + commission + commission_2
    elif amount * PERCENT_WITHDRAWAL > 600:
        commission = MAX_COMMISSION
        balance -= amount + commission + commission_2
    else:
        commission = amount * PERCENT_WITHDRAWAL
        balance -= amount + commission + commission_2
    return balance, print(f'Коммиссия за снятие: {commission + commission_2}. Коммиссия за богатство {wealth_commission}. Ваш баланс: {balance} \n'), log_operations(-amount)


def log_operations(amount):
    global log
    log.append(amount)
    return log, count_operations()


def count_operations():
    global log
    global count_operation
    count_operation = len(log)
    return count_operation, action_choice()


action_choice()

print(f'Лог операций: {log}')
