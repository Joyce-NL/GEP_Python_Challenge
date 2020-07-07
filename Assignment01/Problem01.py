#Project Euler problem 1
#https://projecteuler.net/problem=1

number = 3
sum = 0
while number < 1000:
    if (number % 3 == 0) or (number % 5 == 0):
        sum += number

    number += 1

print("sum = "+ str(sum))
