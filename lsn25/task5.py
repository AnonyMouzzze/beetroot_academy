def sum_of_digits(digit_string: str) -> int:
    if type(digit_string) != str:
        raise TypeError
    if not digit_string.isalnum():
        raise ValueError
    if len(digit_string) == 1:
        return digit_string
    return int(digit_string[0]) + int(sum_of_digits(digit_string[1:]))

print(sum_of_digits('26'))