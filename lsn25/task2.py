def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if index == len(looking_str) // 2:
        return True
    if looking_str[index] != looking_str[-1-index]:
        return False
    return is_palindrome(looking_str, index+1)


print(is_palindrome('racecar'))