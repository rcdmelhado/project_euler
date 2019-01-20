import time


class Prime:
    """Prime number benchmark result

    BRUTE FORCE - total time in seconds: 23.2
    OPTIMIZED - total time in seconds: 2.1
    """

    @staticmethod
    def _brute_force_is_prime(number):
        for i in range(2, number):
            if number % i == 0:
                return False

        return True

    def brute_force(self, number):
        _prime = 0
        i = 1

        start = time.time()
        while _prime < number:
            i += 1
            if self._brute_force_is_prime(i):
                _prime += 1

        print('\nBRUTE FORCE - total time in seconds: {:.1f}'.format(time.time() - start))

        return i

    @staticmethod
    def _optimized_is_prime(number: int, known_primes: list) -> bool:
        for _prime in known_primes:
            if number % _prime == 0:
                return False

        return True

    def optimized(self, number):
        known_prime_list = [2]
        i = 1

        start = time.time()
        while len(known_prime_list) < number:
            i += 1
            if self._optimized_is_prime(i, known_prime_list):
                known_prime_list.append(i)

        print('\nOPTIMIZED - total time in seconds: {:.1f}'.format(time.time() - start))
        return known_prime_list[len(known_prime_list) - 1]


if __name__ == '__main__':
    prime_number = 10001

    print(Prime().brute_force(prime_number))
    print(Prime().optimized(prime_number))
