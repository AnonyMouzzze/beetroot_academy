# Task 1 Enumerate
class Enum:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.iteration = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration == len(self.iterable) - 1:
            raise StopIteration
        self.iteration += 1
        return self.iteration, self.iterable[self.iteration],


for i in Enum([1, 2, 3, 4]):
    print(i)


# Task 2 Range
def in_range(start, end, step=1):
    while start < end:
        yield start
        start += step


for i in in_range(1, 5):
    print(i)


# Task 3 Fibs
class Fibs:
    def __init__(self, n):
        self.start()
        self.n = n

    def start(self):
        self.count = 1
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:
            self.start()
            raise StopIteration
        res = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return res

    def __getitem__(self, item):
        return item


obj = Fibs(10)
for s in obj:
    print(s)
print(obj[5])
