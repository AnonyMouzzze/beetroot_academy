import string
from functools import wraps

# Task 1 Email validation
class Email:
    def __init__(self, email):
        self.email = self.validate(email)

    def validate(self, email):
        if '@' in email:
            splited_email = email.split('@')
            if self.prefix_validation(splited_email[0]) and self.domain_validation(splited_email[1]):
                return email
        return 'Invalid Email'

    def prefix_validation(self, prefix):
        acceptable_symbols = ['.', '-', '_']
        if len(prefix) < 2:
            return False
        for symbol in prefix:
            if symbol not in acceptable_symbols and symbol not in string.ascii_letters:
                return False
            elif symbol in acceptable_symbols and prefix[prefix.index(symbol) + 1] == symbol:
                return False
        if prefix[0] in acceptable_symbols or prefix[-1] in acceptable_symbols:
            return False
        return True

    def domain_validation(self, domain):
        acceptable_symbols = ['-', '.']
        if len(domain) < 4:
            return False
        elif '.' not in domain:
            return False
        elif domain.count('.') > 1 or domain.count('-') > 1:
            return False
        elif len(domain.split('.')[1]) < 2:
            return False
        for symbol in domain:
            if symbol not in string.ascii_letters and symbol not in acceptable_symbols:
                return False
        return True


e = Email('abc.def@mail-archive.com')
print(e.email)


# Task 2 Boss - Workers
class Boss:
    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name
        self.__workers = []

    @property
    def worker(self):
        return self.__workers

    @worker.setter
    def worker(self, worker: 'Worker'):
        for w in self.__workers:
            if w == worker:
                break
        else:
            self.__workers.append(worker)


class Worker:
    def __init__(self, id_: int, name: str, boss: Boss):
        self.id = id_
        self.name = name
        self.boss = boss

    def __eq__(self, other):
        if isinstance(other, Worker):
            if self.id == other.id:
                return True
        return False


boss = Boss(13, 'Andrii')
boss.worker = Worker(0, 'Alex', boss)
boss.worker = Worker(1, 'Benjamin', boss)
print(boss.worker)


# Task 3
class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return int(func(*args, **kwargs))
            except ValueError:
                return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
                return str(func(*args, **kwargs))
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return bool(func(*args, **kwargs))
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return float(func(*args, **kwargs))
            except ValueError:
                return func(*args, **kwargs)
        return wrapper

