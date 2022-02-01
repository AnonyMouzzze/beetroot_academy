def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError
    if n == 1:
        return a
    return a + mult(a, n-1)

