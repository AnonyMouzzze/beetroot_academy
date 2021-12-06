# Task 1 Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.

def oops():
    raise IndexError

def catcher():
    try:
        oops()
    except IndexError:
        print('oops')

catcher()

# Task 2 Write a function that takes in two numbers from the user via input(), call the numbers a and b,
# and then returns the value of squared a divided by b, construct a try-except block which raises an exception
# if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).

def operation():
    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        return a**2 / b
    except ValueError:
        print('Use only integers')
    except ZeroDivisionError:
        print('Cannot divide by zero')

operation()