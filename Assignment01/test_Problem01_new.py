import unittest
from Problem01_new import find_and_sum_multiples


class TestProblem01(unittest.TestCase):
    def test_function(self):
        self.assertEqual(find_and_sum_multiples(1000, 3, 5), 233168, "The result of the function does not match the expected result.")
        self.assertEqual(find_and_sum_multiples(10, 3), 18, "The result of the function does not match the expected result.")
        self.assertEqual(find_and_sum_multiples(10, 3, 5), 23, "The result of the function does not match the expected result.")


    def test_input_type(self):
        with self.assertRaises(TypeError):
            find_and_sum_multiples(5j, 3, 5)
            find_and_sum_multiples(1000, 2j, 8)
            find_and_sum_multiples(100, 2, 7j)
            find_and_sum_multiples("yes", 4, 7)
            find_and_sum_multiples(25, "no", 4)
            find_and_sum_multiples(250, 25, "None")


    def test_input_value(self):
        with self.assertRaises(ValueError):
            find_and_sum_multiples(-1, 2, 5)
            find_and_sum_multiples(-1, -3, -2)
            find_and_sum_multiples(10, 0, 8)
            find_and_sum_multiples(10, 11, 12)
            find_and_sum_multiples(1000, 3, 2)


if __name__ == '__main__':
    unittest.main()
