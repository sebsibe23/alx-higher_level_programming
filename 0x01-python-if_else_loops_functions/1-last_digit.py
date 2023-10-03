#!/usr/bin/python3
import random
strnumber_ = random.randint(-10000, 10000)
last_digit = strnumber_ % 10
print("Last digit of", strnumber_, "is", last_digit, end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
