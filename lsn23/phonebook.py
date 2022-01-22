import json

# Task 2 Extend Phonebook application

def create_new_phonebook(book_name: str) -> None:
    with open(f'{book_name}.json', 'w') as pb:
        empty = []
        json.dump(empty, pb, indent=4, ensure_ascii=False)
    print('New book was created')


def writer(data: list) -> None:
    with open(f'{book_name}.json', 'w') as pd:
        json.dump(data, pd, ensure_ascii=False, indent=4)


def reader() -> list:
    with open(f'{book_name}.json', 'r') as pb:
        return json.load(pb)


def add_new_entries() -> None:
    first_name = input('Enter a first name: ').strip().capitalize()
    last_name = input('Enter a last name: ').strip().capitalize()
    full_name = f'{first_name} {last_name}'
    phone_number = input('Enter a phone number: ')
    city = input('Enter a city: ')

    user_data = reader()
    user_data.append({
        'full name': full_name,
        'first name': first_name,
        'last name': last_name,
        'phone number': phone_number,
        'city': city
    })

    writer(user_data)


def search_by(character: str) -> dict:
    user_data = reader()

    for data in user_data:
        for d in data.values():
            if d == character.capitalize():
                return data


def delete_contact(number: str) -> list:
    user_data = reader()

    for data in user_data:
        if data['phone number'] == number:
            user_data.pop(user_data.index(data))

    return user_data


def update(number: str, new_number: str) -> None:
    user_data = reader()

    for data in user_data:
        if data['phone number'] == number:
            data['phone number'] = new_number
            print('Number was updated')
    writer(user_data)


def see_all() -> list:
    user_data = reader()

    for data in user_data:
        return data


def book_exists(book_name: str) -> bool:
    try:
        with open(f'{book_name}.json', 'r'):
            pass
    except FileNotFoundError:
        print('Phone book not found')
        return False
    return True


def helper() -> None:
    print("-" * 50)
    print('add - to add new contact in your active phonebook')
    print('del - to delete contact from active phonebook')
    print('search - to search a contact')
    print('update - update a record by phone number')
    print('see_all - to see all contacts')
    print('exit - to exit a program')
    print("-" * 50)


def start() -> str:
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
        print(search_by(character))
    elif command == 'update':
        number = input('Enter a phone number to search: ')
        new_number = input('Enter new phone number: ')
        update(number, new_number)
    elif command == 'see_all':
        print(see_all())
    elif command == 'exit':
        break