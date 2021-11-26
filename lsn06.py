import random

# Task 1
# Write a Python program to get the largest number from a list of random numbers with the length of 10
random_numbers = []
while len(random_numbers) < 10:
    random_numbers.append(random.randint(0, 1000))
print(f'List: {random_numbers}')
print(f'Max value in list: {max(random_numbers)}')

# Task 2
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.

def list_generator(length, max_int):
    new_list = []
    while len(new_list) < length:
        new_list.append(random.randint(0, max_int))
    return new_list

list_a = list_generator(10, 10)
list_b = list_generator(10, 10)
list_c = list(set(list_a) & set(list_b))
print(f'Common integers: {list_c}')

# Task 3
# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.

nums = [n for n in range(1, 101)]
sorted_nums = []
iteration = 0
while iteration != 100:
    if nums[iteration] % 7 == 0 and nums[iteration] % 5 != 0:
        sorted_nums.append(nums[iteration])
    iteration += 1
print(f'Sorted list: {sorted_nums}')

