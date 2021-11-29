# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
# and the number of occurrences as values.

sentence = input('Input your sentence: ').lower().split()
u_words = {}
for s in sentence:
    u_words[s] = sentence.count(s)
print(f'Task 1: {u_words}')

# Task 2 Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = {}

for s in stock:
    total_price[s] = stock[s] * prices[s]
print(f'Task 2: {total_price}')

# Task 3 Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
MIN_INT = 1
MAX_INT = 11

comp = [(i, i*i) for i in range(MIN_INT, MAX_INT)]
print(f'Task 3: {comp}')