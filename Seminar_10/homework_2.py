class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        res = []
        count = 0
        for i in self.list1:
            for j in self.list2:
                if i == j:
                    res.append(i)
                    count += 1
                    break
        if len(res) == 0:
            print('Совпадающих чисел нет.')
        else:
            print(f'Совпадающие числа: {res}\n Количество совпадающих чисел: {count}')


list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
