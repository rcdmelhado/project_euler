"""Problem 07 - 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import time

prime_list = [2, 3]
actual_number = 3

start = time.time()
while len(prime_list) < 10001:
    is_prime = True
    actual_number += 2
    half_actual_number = actual_number / 2
    for prime in prime_list:
        if prime > half_actual_number:
            break

        if actual_number % prime == 0:
            is_prime = False
            break

    if is_prime:
        prime_list.append(actual_number)

print(f'run time: {time.time() - start} seconds')
print(f'{prime_list[-1]} is the 10,000st prime number')
