sum_of_the_squares = 0
_sum = 0

for i in range(1, 101):
    sum_of_the_squares += i ** 2
    _sum += i

print(_sum ** 2 - sum_of_the_squares)
