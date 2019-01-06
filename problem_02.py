"""Problem 2 - Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def get_fibonacci_even_terms_sum_up_to(highest_number: int) -> int:
    even_terms_sum = 0
    last_number = 1
    actual_number = 2

    while actual_number <= highest_number:
        if actual_number % 2 == 0:
            even_terms_sum += actual_number

        aux = last_number + actual_number
        last_number = actual_number
        actual_number = aux

    return even_terms_sum


if __name__ == '__main__':
    print(get_fibonacci_even_terms_sum_up_to(4000000))
