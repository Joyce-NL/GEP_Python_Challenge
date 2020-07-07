from itertools import permutations
from functools import reduce
from math import sqrt, floor


def find_largest_pandigital_prime(min_digits, max_digits):
    if type(min_digits) is not int or type(max_digits) is not int:
        raise TypeError("Both parameters should be integers.")
    if min_digits < 1 or min_digits > 9 or max_digits < 1 or max_digits > 9:
        raise ValueError("The parameters should both be integers between 1 and 9.")
    if max_digits < min_digits:
        raise ValueError("The first parameter should be smaller than or equal to the second parameter.")

    largest_pandigital_prime = 0

    for nr_of_digits in reversed(range(min_digits, max_digits + 1)):
        if nr_of_digits not in [1, 2, 3, 5, 6, 8, 9]:
            set_of_required_digits = [str(i) for i in reversed(range(1, nr_of_digits + 1))]
            pandigital_numbers = permutations(set_of_required_digits)
            for number in pandigital_numbers:
                pandigital_number = int(reduce(lambda a, b: a+b, number))
                if is_prime_number(pandigital_number):
                    if pandigital_number > largest_pandigital_prime:
                        largest_pandigital_prime = pandigital_number

        if largest_pandigital_prime > 0:
            print(largest_pandigital_prime)
            return largest_pandigital_prime

    print("No prime pandigital found in the specified range.")
    return "NA"


def is_prime_number(number):
    max_factor = floor(sqrt(number)) + 1
    if number == 1:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        for i in range(2, max_factor):
            if number % i == 0:
                return False
    return True
