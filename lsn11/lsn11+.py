#  Task 1 Создайте класс Friend для хранения имени name и телефона phone.
#  Обратите внимание, у друга может не быть телефона.

class Friend:
    def __init__(self, *params):
        self.name = params[0]
        self.phone = params[1] if len(params) == 2 else ''


# Task 2 Реализуйте класс SymbolA с методам line который параметром принимает
# номер выводимой строки и возвращает соответствующее строковое значение.

class SymbolA:
    def __init__(self, symbol):
        self.symbol = symbol
        self.iteration = 0

    def creator(self):
        a = f' {self.symbol*3}\n{self.symbol}  {self.symbol}\n{self.symbol*4}\n{self.symbol}  {self.symbol}'
        return a

    def draw(self):
        print(self.creator())

    def line(self, number):
        lines = self.creator().split('\n')
        print(lines[number])

    def line_wp(self):
        lines = self.creator().split('\n')
        print(lines[self.iteration])
        if self.iteration <= 4:
            self.iteration += 1
        else:
            self.iteration = 0
            raise StopIteration

