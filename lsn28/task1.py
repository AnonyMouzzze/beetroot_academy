arr = [3, 6, 8, 10, 12, 15, 18, 19, 21]


def binary_search(array: list[int], value: int, first_item_index: int = 0, last_item_index: int = -1) -> bool:
    if last_item_index == -1:
        last_item_index = len(array) - 1
    half_list_index = (first_item_index + last_item_index)//2
    if array[half_list_index] == value:
        return True
    elif first_item_index < last_item_index:
        if array[half_list_index] > value:
            return binary_search(array, value, first_item_index=first_item_index, last_item_index=half_list_index-1)
        elif array[half_list_index] < value:
            return binary_search(array, value, first_item_index=half_list_index+1, last_item_index=last_item_index)
    return False


assert binary_search(arr, 19) == True
assert binary_search(arr, 1) == False
