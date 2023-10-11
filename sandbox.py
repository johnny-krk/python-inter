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



#data = [128, 121, 134, 136, 136, 118, 123, 109, 120, 116, 125, 128, 121, 129, 130, 131, 127, 119,
#114, 134, 110, 136, 134, 125, 128, 123, 128, 133, 132, 136, 134, 129, 132]

data =[18, 18, 18, 18, 19, 20, 20, 20, 21, 22, 22, 23, 24, 26, 27, 32, 33, 49, 52, 56]
data = sorted(data)

print(data)
print(len(data))
n = len(data) + 1
dolny = n * 0.25
print(dolny)
print(data[int(dolny)], '\n')
srodkowy = n * 0.50
print(srodkowy)
print(data[int(srodkowy)], '\n')
gorny = n * 0.75
print(gorny, int(gorny))
print(data[int(gorny)], '\n')
print(27+ 5* 0.75)


import statistics

values = [23, 26, 29, 30, 32, 34, 37, 45, 57, 80, 102, 147, 210, 355, 782, 1209]
values_median = statistics.median(values)
print(values_median)

values_median_l = statistics.median_low(values)
print(values_median_l)


import numpy

print("0.25: ", numpy.quantile(values, 0.25))
print("0.5: ", numpy.quantile(values, 0.5))
print("0.75: ", numpy.quantile(values, 0.75))
values_median_h = statistics.median_high(values)
print(values_median_h)
