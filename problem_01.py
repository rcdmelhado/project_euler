"""Problem 1 - Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_sum_of_multiples(_max):
    _multiples = 0
    for i in range(_max):
        if i % 3 == 0:
            _multiples += i

        if i % 5 == 0:
            _multiples += i

    return _multiples


if __name__ == '__main__':
    sum_of_multiples = get_sum_of_multiples(1000)
    print(sum_of_multiples)
