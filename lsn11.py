# Task 1 Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
# and add them as attributes. Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print("Hello, my name is {} {} and I'm {} years old".format(self.firstname, self.lastname, self.age))


carl = Person('Carl', 'Johnson', '26')
carl.talk()


# Talk 2 Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self, ):
        return self.dog_age * self.age_factor


# Task 3 Create a simple prototype of a TV controller in Python

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.active_channel = self.channels[0]

    def first_channel(self):
        self.active_channel = self.channels[0]

    def last_channel(self):
        self.active_channel = self.channels[-1]

    def turn_channel(self, number):
        try:
            self.active_channel = self.channels[number - 1]
        except IndexError:
            print('No channel found')

    def next_channel(self):
        if self.channels.index(self.active_channel) == len(self.channels) - 1:
            self.active_channel = self.channels[0]
        else:
            self.active_channel = self.channels[self.channels.index(self.active_channel) + 1]

    def previous_channel(self):
        if self.channels.index(self.active_channel) == 0:
            self.active_channel = self.channels[-1]
        else:
            self.active_channel = self.active_channel[self.channels.index(self.active_channel) - 1]

    def current_channel(self):
        return self.active_channel

    def is_exist(self, n):
        for number, name in enumerate(self.channels):
            if n == number + 1 or n == name:
                return 'Yes'
        return 'No'

controller = TVController(CHANNELS)





print(controller.is_exist('asd'))

