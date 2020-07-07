# GEP_Python_Challenge
GEP Coding Python Challenge

This is a repository for the GEP Python Coding Challenge Assignments.  
Each function is developed to handle small changes in the problem definition.

1.  Assignment 1 is a Python program to solve Project Euler problem 1.  
    https://projecteuler.net/problem=1
    
    The function in this script takes 2 mandatory and 1 optional parameters. 
    All parameters should be positive integers.
    The first parameter is the number up until which you want to count multiples.
    The second parameter is the number for which you want to sum the multiples.
    The third (optional) parameter is the second number for which you want to sum the multiples.  

    **Syntax: 
    `find_and_sum_multiples(maximum, number1, number2)`**

    To solve Project Euler problem 1 enter the following parameters:  
    `find_and_sum_multiples(1000, 3, 5)`  
    Leaving out the 3rd parameter would result in the sum of all multiples of 3 under 1000.
    
2.  Assignment 2 is a Python program to solve Project Euler problem 2.  
    https://projecteuler.net/problem=2  
    
    This function is made to run on different ranges within the Fibonacci sequence.
    The function takes 2 parameters. These parameters should be positive integers or floats.  
    The first parameter determines where the range of the Fibonacci sequence should start.
    If the first parameter is a Fibonacci number, the range will start with that number.
    If the first parameter is not a Fibonacci number, the range will start with the first 
    Fibonacci number that comes after this parameter.  
    The second parameter is the maximum value for the range. The last Fibonacci number 
    used in the function should be below this value.  
    The result is a sum of all even Fibonacci numbers in the specified range.
    
    **Syntax:`sumevenfibonaccinumbers(startnumber, endvalue)`**
    
    To solve Project Euler problem 2 would require the following parameters:  
    `sumevenfibonaccinumbers(1, 4000000)`
    
    To count all even Fibonacci numbers between 2 and 10:  
    `sumevenfibonaccinumbers(2, 10)`
    
3.  Assignment 3 is a Python program to solve Project Euler 41.  
    https://projecteuler.net/problem=41
    
    This function is made to run on numbers where the number of digits is in a specified range.
    The function takes 2 arguments that specify the range of the number of digits.
    The digits are assumed to be part of the base-10 numbering system. 
    The possible number of digits in the base-10 system are 1, 2, 3, 4, 5, 6, 7, 8, 9.
    
    **Syntax: `find_largest_pandigital_prime(min_digits, max_digits)`**
    
    The pandigital with 1 digit is automatically excluded, because it only consists of the number 1 and 
    that's not a prime number.  
    Pandigitals of 2, 3, 5, 6, 8 and 9 digits are also excluded, because their digits add up to a 
    number that is divisible by 3. If the digits of a number add up to a multiple of 3, 
    the number is divisible by 3 and can therefore not be a prime number. If you have never 
    heard of this rule, you can find a nice explanation here:  
    https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-divisibility-tests/v/the-why-of-the-3-divisibility-rule  
    It is still possible to select a range that includes pandigitals with the excluded number of digits, 
    but they will be skipped in the function. This is done to speed up performance. There is no
    use finding pandigitals that you know can never be prime numbers.  
    The function returns the largest prime pandigital number for numbers with a number of digits 
    that is in the specified range. If the range is (7,7), then only the largest pandigital 
    prime number with 7 digits is returned.
    
    To solve Project Euler problem 41 would require the following parameters:
    `find_largest_pandigital_prime(1,9)`
    
    
    
    
   