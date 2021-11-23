# Task 1 'String manipulation'
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
strings = ['hello world', 'my', 'x']

for string in strings:
    if len(string) >= 2:
        result = string[:2] + string[-2:]
        print(f'Maded string: {result}')
    else:
        result = ''
        print(f'Lenth of string {string} is less than 2.Result: {result} ')

# Task 2 'The valid phone number program.'
# Make a program that checks if a string is in the right format for a phone number. 0938080908
kyivstar = ['039', '067', '068', '096', '097', '098']
vodafone = ['050', '066', '095', '099']
lifecell = ['063', '093']

number = str(input('Enter a phone number: '))

if number.isalnum() and len(number) == 10:
    if number[:3] in kyivstar:
        print('Your operator is kyivstar')
    elif number[:3] in vodafone:
        print('Your operator is vodafone')
    elif number[:3] in lifecell:
        print('Your operator is lifecell')
    else:
        print('Invalid phone number format')
else:
    print('Invalid phone number format or lenth')

# Task 3 'The name check.
stored_name = 'andrii'
asked_name = input('Enter your name: ')

if asked_name.isalpha():
    asked_name = asked_name.lower()
    if stored_name == asked_name:
        print(stored_name == asked_name)
    else:
        print(stored_name == asked_name)
else:
    print('Enter only alphabet symbols')










