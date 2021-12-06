import json

# Task 1 Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents.
# Run your two scripts from the system command line.

def file_creator():
    with open('myfile.txt', 'w') as file:
        file.write('Hello file world!')

def file_reader():
    with open('myfile.txt', 'r') as file:
        print(file.read())

file_creator()
file_reader()

# Task 2 Extend Phonebook application

def create_new_phonebook(book_name):
    with open(f'{book_name}.json', 'w') as pb:
        empty = []
        json.dump(empty, pb, indent=4, ensure_ascii=False)
    print('New book was created')


def writer(data):
    with open(f'{book_name}.json', 'w') as pd:
        json.dump(data, pd, ensure_ascii=False, indent=4)


def reader():
    with open(f'{book_name}.json', 'r') as pb:
        return json.load(pb)


def add_new_entries():
    first_name = input('Enter a first name: ').strip().capitalize()
    last_name = input('Enter a last name: ').strip().capitalize()
    full_name = f'{first_name} {last_name}'
    phone_number = input('Enter a phone number: ')
    city = input('Enter a city: ')

    user_data = reader()
    user_data.append({
        'full name': full_name,
        'first name' : first_name,
        'last name' : last_name,
        'phone number' : phone_number,
        'city' : city
        })

    writer(user_data)


def search_by(character):
    user_data = reader()

    for data in user_data:
        for d in data.values():
            if d == character.capitalize():
                print(data)

def delete_contact(number):
    user_data = reader()

    for data in user_data:
            if data['phone number'] == number:
                user_data.pop(user_data.index(data))

    return user_data


def update(number, new_number):
    user_data = reader()

    for data in user_data:
        if data['phone number'] == number:
            data['phone number'] = new_number
            print('Number was updated')
    writer(user_data)


def see_all():
    user_data = reader()

    for data in user_data:
        print(data)


def book_exists(book_name):
    try:
        with open(f'{book_name}.json', 'r'):
            pass
    except FileNotFoundError:
        print('Phone book not found')
        return False
    return True


def helper():
    print("-" * 50)
    print('add - to add new contact in your active phonebook')
    print('del - to delete contact from active phonebook')
    print('search - to search a contact')
    print('update - update a record by phone number')
    print('see_all - to see all contacts')
    print('exit - to exit a program')
    print("-" * 50)


def start():
    book_name = input('Enter a phonebook name u want to work with: ').strip().lower()
    if book_exists(book_name) == False:
        create_new_phonebook(book_name)
    return book_name


book_name = start()

while True:
    command = input('What do you want to do?(help to see commands): ').strip().lower()
    if command == 'help':
        helper()
    elif command == 'add':
        add_new_entries()
        print('New contact was succesfully added')
    elif command == 'del':
        number = input('Enter a number to delete from phonebook: ').strip().lower()
        writer(delete_contact(number))
        print('Contact was successfully deleted')
    elif command == 'search':
        character = input('Enter a character: ')
        search_by(character)
    elif command == 'update':
        number = input('Enter a phone number to search: ')
        new_number = input('Enter new phone number: ')
        update(number, new_number)
    elif command == 'see_all':
        see_all()
    elif command == 'exit':
        break