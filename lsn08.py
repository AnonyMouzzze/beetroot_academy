# Task 1 Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.

def favorite_movie(movie_name):
    if type(movie_name) == str:
        print(f'My favorite movie is named {movie_name}')
    else:
        print('Invalid name')

favorite_movie('Zack Snyders Justice League')

# Task 2 Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(**kwargs):
    countries = kwargs
    print(countries.values())

make_country(Ukraine='Kyiv', Russia='Moscow', France='Paris', Spain='Barcelona')

# Task 3
# Create a function called make_operation, which takes in a simple arithmetic operator
# as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter.

def make_operation(*args):
    operations = ('+', '-', '*')
    arguments = args
    get_operation = False
    operator = ''
    digits_list = []

    for arg in arguments:
        arg = str(arg)
        if arg in operations and get_operation == False:
            operator = arg
            get_operation = True
        elif arg.isdigit():
            digits_list.append(arg)
        elif '-' in arg and arg[1:].isdigit():
            digits_list.append(arg)

    result = eval(operator.join(digits_list))
    print(f'Task 3: {result}')

make_operation('-', 5, 5, -10, -20)