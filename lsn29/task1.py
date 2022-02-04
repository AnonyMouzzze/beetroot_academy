import random

# bubble sort in both directions

def bubble_sort(array: list[int]) -> list[int]:
    swiched = True
    while swiched:
        swiched = False
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                swiched = True
        for index in range(-1, -len(array), -1):
            if array[index] < array[index-1]:
                array[index], array[index-1] = array[index-1], array[index]
                swiched = True
    return array


arr = [random.randint(0, 100000) for _ in range(10000)]
print(arr)
print(bubble_sort(arr))