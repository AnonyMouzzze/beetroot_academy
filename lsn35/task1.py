import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    @classmethod
    def run(cls):
        for _ in range(cls.rounds):
            cls.counter += 1


c = Counter()
c1 = Counter()

c.start()
c1.start()

c.join()
c1.join()

print(c.counter)
print(c1.counter)
