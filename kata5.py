"""
Find the Minimum, Maximum, Length and Average Values
Create a function that takes a list of numbers and returns the following statistics:
Minimum Value
Maximum Value
Sequence Length
Average Value
"""
def minMaxLengthAverage(lst):
	return [min(lst), max(lst), len(lst), sum(lst)/len(lst)]
  
  
"""
Return the Sum of the Two Smallest Numbers
Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.
"""
def sum_two_smallest_nums(lst):
	return sum(list(filter(lambda x: x>=0, sorted(lst)))[:2])
  
  
"""
Cumulative List Sum
Create a function that takes a list of numbers and returns a list where each number is the sum of itself + all previous numbers in the list.
"""
def cumulative_sum(lst):
  return [sum(lst[:i+1]) for i in range(len(lst))]
