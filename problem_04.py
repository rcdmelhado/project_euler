"""Problem 4 - Largest palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def get_range(number_of_digits: int) -> tuple:
    _max = ''
    _min = ''

    for i in range(number_of_digits):
        _max += '9'
        _min += '0'

    return int(_max), int('1' + _min[number_of_digits - 1])


def is_palindrome(number: int) -> bool:
    half_chars = int(len(str(number)) / 2)
    begin = str(number)[half_chars:]
    end = str(number)[:half_chars]
    reversed_end = ''.join(reversed(end))

    return begin == reversed_end


def get_largest_palindrome_product(_digits: int) -> tuple:
    max_number, min_number = get_range(_digits)
    _largest_palindrome = 0
    _a = 0
    _b = 0

    for i in range(max_number, min_number, -1):
        for j in range(max_number, min_number, -1):
            product = i * j
            if is_palindrome(product) and product > _largest_palindrome:
                _a = i
                _b = j
                _largest_palindrome = product

    return _a, _b, _largest_palindrome


if __name__ == '__main__':
    digits = 3

    a, b, largest_palindrome = get_largest_palindrome_product(digits)
    print(f'{largest_palindrome} is the largest palindrome\nproduct of {a} and {b}')
