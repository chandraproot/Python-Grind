
# funtion to find the sum of all the terms of a array
import numpy as np


def sum_arr(ar):
    sum = 0
    for i in ar:
        sum = i + sum
    return sum


ar = np.array([1, 2, 3, 4, 5, 50, 84], dtype=np.int32)
re = sum_arr(ar)
print(re)
# time complexity O(n)
# space complexity O(1)
