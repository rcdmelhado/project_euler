"""Problem 09 - Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def product_pythagorean_triplet(numbers_sum):
    for a in range(3, numbers_sum):

        for b in range(a + 1, numbers_sum):
            c = (a ** 2 + b ** 2) ** 0.5

            if a + b + c > numbers_sum:
                continue

            if a + b + c == numbers_sum:
                return int(a * b * c)


print(product_pythagorean_triplet(1000))
