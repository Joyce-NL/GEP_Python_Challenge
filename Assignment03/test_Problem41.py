import unittest
from Problem41 import find_largest_pandigital_prime, is_prime_number

class TestProblem41(unittest.TestCase):
    def test_main_function(self):
        self.assertEqual(find_largest_pandigital_prime(1, 9), 7652413, 'the result of the function does not match the expected result.')
        self.assertEqual(find_largest_pandigital_prime(1, 3), "NA", 'the result of the function does not match the expected result.')
        self.assertEqual(find_largest_pandigital_prime(5, 6), "NA", 'the result of the funtion does not match the expected result.')
        self.assertEqual(find_largest_pandigital_prime(8, 9), "NA", 'the result of the function does not match the expeced result.')
        self.assertEqual(find_largest_pandigital_prime(5, 7), 7652413, 'the result of the function does not match the expected result.')

    def test_input_type(self):
        with self.assertRaises(TypeError):
            find_largest_pandigital_prime(5j, 5)
            find_largest_pandigital_prime(1, 2j)
            find_largest_pandigital_prime("yes", 5)
            find_largest_pandigital_prime(1, "no")

    def test_input_value(self):
        with self.assertRaises(ValueError):
            find_largest_pandigital_prime(-1, 2)
            find_largest_pandigital_prime(1, 0)
            find_largest_pandigital_prime(8, 2)
            find_largest_pandigital_prime(1, 10)
            find_largest_pandigital_prime(0, 7)

    def test_is_prime_number_function(self):
        self.assertEqual(is_prime_number(1), False,'the result of the function does not match the expected result.')
        self.assertEqual(is_prime_number(2), True, 'the result of the function does not match the expected result.')
        self.assertEqual(is_prime_number(3), True, 'the result of the function does not match the expected result.')
        self.assertEqual(is_prime_number(4), False, 'the result of the function does not match the expected result.')
        self.assertEqual(is_prime_number(7919), True, 'the result of the function does not match the expected result.')
        self.assertEqual(is_prime_number(123456), False, 'the result of the function does not match the expected result.')
        self.assertEqual(is_prime_number(7652413), True, 'the result of the function does not match the expected result.')


if __name__ == '__main__':
    unittest.main()
