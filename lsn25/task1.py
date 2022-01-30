def to_power(x: int, exp: int) -> int:
    if exp <= 0:
        raise ValueError
    if exp == 1:
        return x
    return x * to_power(x, exp-1)

assert to_power(3.5, 2) == 12.25
assert to_power(2, 3) == 8

    