"""Problem 5 - Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

if __name__ == '__main__':
    max = 20
    smallest_divisible_number = 1
    step = 1

    for actual_number in range(1, max + 1):
        while smallest_divisible_number % actual_number != 0:
            smallest_divisible_number = smallest_divisible_number + step

        step = smallest_divisible_number

    print(f'{smallest_divisible_number} is the smallest number that can be'
          f' divided by each of the numbers from 1 to {max}.')
