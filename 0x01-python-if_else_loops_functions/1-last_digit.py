#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number % 10 == 0:
    print("Last digit of " + str(number) + ' is ' + str(n) + ' and is 0')
elif (number % 10 > 5):
    print("Last digit of " + str(number) + ' is ' + str(n) + ' and is greater than 5')
else:
    print("Last digit of " + str(number) + ' is ' + str(n) + ' and is less than 6 and not 0')
