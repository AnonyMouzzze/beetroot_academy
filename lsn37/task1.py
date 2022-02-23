import asyncio


async def fibonacci(number_in_array: int) -> int:
    fibs = [1, 1]
    if number_in_array <= 0:
        raise ValueError
    elif number_in_array in (1, 2):
        return 1

    for _ in range(3, number_in_array + 1):
        next_number = fibs[-1] + fibs[-2]
        fibs.append(next_number)
    return fibs[-1]


async def factorial(number: int) -> int:
    result = 1
    if number < 0:
        raise ValueError
    elif number == 0:
        return result

    for num in range(1, number + 1):
        result *= num
    return result


async def squares(number: int) -> int:
    return number**2


async def cubic(number: int) -> int:
    return number**3


async def gather_tasks() -> list[list[int]]:
    result = []
    for num in range(1, 11):
        gather_result = await asyncio.gather(
            fibonacci(num), factorial(num), squares(num), cubic(num)
        )

        if not result:
            result = [[] for _ in range(len(gather_result))]

        for i in range(len(result)):
            result[i].append(gather_result[i])

    return result


print(asyncio.run(gather_tasks()))
