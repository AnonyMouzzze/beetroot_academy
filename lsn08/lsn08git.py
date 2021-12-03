# Task 1 Напишите функцию которая будет переводить возраст с Земного на Марсианский.
# В году на Земле 365 дней а на марсе 687

def mars_age(earth_age):
    earth_days = earth_age * 365
    mars_age = earth_days // 687
    return mars_age

try:
    user_age = int(input('Enter ur age: '))
    user_mars_age = mars_age(user_age)
    print(f'Your mars age is {user_mars_age}')
except ValueError:
    print('Use only digits!')

# Task 2 Напишите функцию greet принимающую имя name (type:str) м слово word (type:str).
# Если слово не передано то считать его " -" и возвращающую строку вида "[Имя] ты сегодня [слово]!"
def greet(name, word='-'):
    return f'{str(name)} ты сегодня {str(word)}!'

greet('Egor')


# Task 3 Напишите функцию joinA которая принимает неограниченное количество значений любого типа
# и возвращает строку где эти значения склеены через символ A

def joinA(*args):
    return 'A'.join([str(s) for s in args])

print(joinA('GL', 'HF', 13, True))
