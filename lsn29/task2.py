import random
#Merge sort without slice operator

def merge_sort(array: list[int]) -> list[int]:
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    left_half = merge_sort([array[i] for i in range(mid)])
    right_half = merge_sort([array[i] for i in range(mid, len(array))])
    sorted_list = []

    while left_half and right_half:
        if left_half[0] < right_half[0]:
            sorted_list.append(left_half.pop(0))
        elif left_half[0] > right_half[0]:
            sorted_list.append(right_half.pop(0))
        else:
            sorted_list.append(right_half.pop(0))    
            sorted_list.append(left_half.pop(0))
    
    sorted_list += left_half + right_half
    return sorted_list

arr = [random.randint(0, 100) for _ in range(10)]

print(arr)
print(merge_sort(arr))