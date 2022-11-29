#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# access the string representation of number
# and then get the last character and convert
# it back to an integer
last_digit = int(str(number)[-1])

if number > 0:
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    elif 6 > last_digit > 0:
        print(f"Last digit of {number} is {last_digit}"
              f" and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {-last_digit}"
          f" and is less than 6 and not 0")
