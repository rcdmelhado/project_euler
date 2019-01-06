"""Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


def highest_prime_factor(number):
    remainder = number
    largest_prime_number = 0
    for i in range(2, remainder):
        if remainder % i == 0:
            remainder = int(remainder / i)
            if i > largest_prime_number:
                largest_prime_number = i

            if i > remainder:
                return largest_prime_number


if __name__ == '__main__':
    print(highest_prime_factor(600851475143))
