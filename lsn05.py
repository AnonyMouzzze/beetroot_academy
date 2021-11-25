import random

# Task 1 'Используя модуль random и его функции randint напишите игру "математика 5кл"'
formula_1 = 'y = 2x + 3'
formula_2 = 'y = 3x + 15'
formula_3 = 'y = x + 7'

game_start = True
while game_start:
    x = random.randint(0, 30)
    random_formula = random.choice([formula_1, formula_2, formula_3])
    if random_formula == formula_1:
        solve = 2*x + 3
    elif random_formula == formula_2:
        solve = 3*x + 15
    else:
        solve = x + 7

    print(random_formula + '\n' + f'x = {x}' + '\n' + 'y = ?')

    answer = input('Enter your answer (must be integer): ')
    if answer.isdigit():
        if answer == str(solve):
            print('Good job!')
            break
        else:
            print('Try one more time :(')
    else:
        print('Answer must be integer!')

# Task 2 'Получите от пользователя слово длинной больше 5 символов.
# Сгенерируйте и выведите 5 комбинаций которые можно получить переставив буквы в слове.'

start = True
while start:
    user_word = input('Enter a word (more than five symbols): ')
    if len(user_word) < 5:
        print('Try again')
        continue
    sample_times = 0
    while sample_times < 5:
        sample_times += 1
        new_word = ''
        iteration = 0
        user_word_copy = user_word
        while iteration < len(user_word):
            random_letter = random.choice(user_word_copy)
            if random_letter not in new_word:
                new_word += random_letter
                iteration += 1

        print(new_word)

# Task 3 'The Guessing Game.'
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

random_number = random.randint(1, 11)
user_number = input('Enter a number beetween 1 and 10:' )
if random_number == user_number:
    print('You are right!')
else:
    print('Unlucky :(')
    print(f'Real number {random_number}')
    print(f'Your number {user_number}')

# Task 4 'Write a program that takes your name as input, and then your age as input and greets you with the following:'
# “Hello <name>, on your next birthday you’ll be <age+1> years”
user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))
print(f'Hello {user_name}, on your next birthday you’ll be {user_age + 1} years')




