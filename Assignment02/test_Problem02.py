import unittest
from Problem02 import sumevenfibonaccinumbers

class TestSumRangeEvenFibNumbers(unittest.TestCase):
    def test_function(self):
        self.assertEqual(sumevenfibonaccinumbers(0, 0), 0, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(0, 1), 0, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(1, 1), 0, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(0, 2), 2, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(1, 9), 10, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(2, 9.5), 10, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(4.4, 19.1), 8, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(8, 8), 8, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(4, 12), 8, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(19, 60), 34, 'the result of the function does not match the expected result.')
        self.assertEqual(sumevenfibonaccinumbers(1, 4000000), 4613732, 'the result of the function does not match the expected result.')

    def test_input_type(self):
        with self.assertRaises(TypeError):
            sumevenfibonaccinumbers(5j, 5)
            sumevenfibonaccinumbers(1, 2j)
            sumevenfibonaccinumbers("yes", 5)
            sumevenfibonaccinumbers(1, "no")

    def test_input_value(self):
        with self.assertRaises(ValueError):
            sumevenfibonaccinumbers(-1, 2)
            sumevenfibonaccinumbers(1, 0)
            sumevenfibonaccinumbers(8, 2)
            sumevenfibonaccinumbers(2.6, -4.5)

if __name__ == '__main__':
    unittest.main()
