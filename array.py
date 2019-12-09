# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    tmp = numpy.array(arr, float)
    return tmp[::-1]

arr = [2,5,7,8,10]
result = arrays(arr)
print(result)
