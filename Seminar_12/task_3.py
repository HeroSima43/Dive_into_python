# Задание №3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

class My_Gen:

    def __init__(self, *args):
        if len(args) == 1:
            self.stop = args[0]
            self.stop = 1
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) >= 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            res = 1
            for i in range(2, self.start+1):
                res *= i
            self.start += self.step
            return res
        raise StopIteration


s = My_Gen(1, 10, 2)
for item in s:
    print(item)
