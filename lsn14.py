# Task 1 Write a Python program to detect the number of local variables declared in a function.

def local_variables():
    x = 1
    y = 2
    z = 3


def find_locals(func):
    return func.__code__.co_nlocals


print(find_locals(local_variables))

# Task 2 Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add

func = test(4)
print(func(5))


# Task 3
def choose_func(nums: list, func1, func2):
    if [num for num in nums if num < 0]:
        return func2(nums)
    return func1(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
print(choose_func(nums2, square_nums, remove_negatives))