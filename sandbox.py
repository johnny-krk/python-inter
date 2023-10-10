from typing import List
import math

numbers: list[int] = [1, 12, 14, 13, 15]
result = [item for item in numbers if item % 2 == 0]
print(result)


def square(x):
    return x ** 2


print("power:")
numbers = map(square, numbers)
squared_numbers = list(numbers)
print(squared_numbers)
print("sqrt:")

new_numbers = map(lambda x: math.sqrt(x), squared_numbers)
print(list(new_numbers))


# filter

def is_even(item: int) -> bool:
    return item % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
filtered_results = filter(is_even, numbers)
print(*filtered_results)

result = filter(lambda x: x % 2 == 0, numbers)
print(*result)
