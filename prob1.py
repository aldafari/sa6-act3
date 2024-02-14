from functools import reduce 

digit = "1993"
number = []



for x in digit:
    number.append(int(x))
print(number)

sum_of_numbers = reduce(lambda x, y: x + y, number)
print(sum_of_numbers)


