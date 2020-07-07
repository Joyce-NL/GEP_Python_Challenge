def find_and_sum_multiples(maximum, number1, number2=None):

    if type(maximum) is not int or type(number1) is not int:
        raise TypeError("All parameters should be integers.")

    if number1 < 1:
        raise ValueError("The second parameter should be an integer with value 1 or higher.")

    if maximum < number1:
        raise ValueError("The first parameter should an integer that is equal to or higher than the second parameter.")

    if number2 is not None:
        if type(number2) is not int:
            raise TypeError("All parameters should be integers.")

        if number2 <= number1:
            raise ValueError("The third parameter should be an integer that is bigger than the second parameter.")

        if number2 > maximum:
            raise ValueError("The third parameter should be an integer that is smaller or equal to the first parameter")


    if number2 is None:
        sum_multiples = sum([number for number in range(number1, maximum) if number % number1 == 0])

    else:
        sum_multiples = sum([number for number in range(number1, maximum) if number % number1 == 0 or number % number2 == 0])

    print(sum_multiples)
    return sum_multiples

find_and_sum_multiples(1000,3,5)


