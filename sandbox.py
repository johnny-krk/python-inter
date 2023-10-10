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


