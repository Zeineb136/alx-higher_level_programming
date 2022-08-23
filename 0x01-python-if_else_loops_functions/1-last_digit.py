#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
<<<<<<< HEAD
    last_digit = number % 10
else 
    last_digit = number % -10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit != 0 and last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
=======
    l_digit = number % 10
else: 
    l_digit = - number % 10
if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
elif l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is 0")
elif l_digit != 0 and l_digit < 6:
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
>>>>>>> 0c29fa59fbd2a70ef8a3a37c571f5acf1a9a30b6
