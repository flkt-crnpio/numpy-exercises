# Task
# You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.
#
# Input Format
# A single line of input containing 9 space separated integers.
#
# Output Format
# Print the 3X3 NumPy array.

import numpy

my_array = numpy.array(input().split(), int)
my_array.shape = (3,3)
print(my_array)
