"""
Return the Factorial

Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.
Examples

3 ➞ 6

5 ➞ 120

13 ➞ 6227020800
"""

import math

def factorial(num):
	return math.factorial(num)

"""
Absolutely Sum

Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.
Examples

[2, -1, 4, 8, 10] ➞ 25

[-3, -4, -10, -2, -3] ➞ 22

[2, 4, 6, 8, 10] ➞ 30

[-1] ➞ 1
"""

def get_abs_sum(lst):
	return sum(abs(x) for x in lst)
