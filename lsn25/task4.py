def reverse(input_str: str) -> str:
    string = ''
    if not input_str:
        return string
    string = input_str[-1] + reverse(input_str[:-1])
    return string

print(reverse('hello'))