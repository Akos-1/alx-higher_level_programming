#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_number = abs(number)
digit = abs_number % 10
output_text = ""

if number < 0:
    digit = -digit
if digit > 5:
    output_text = "greater than 5"
elif digit == 0:
    output_text = "0"
else:
    output_text = "less than 6 and not 0"
print(f"Last digit of {number} is {digit} and is {output_text}")
