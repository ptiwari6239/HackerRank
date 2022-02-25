#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#
def BigSorting(unsorted):
    def converted(array):
        for i in range(0, len(array)):
            array[i] = int(array[i])
        return array

    def swap(arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]
        return arr
    converted(unsorted)
    n = len(unsorted)
    lst_idx = n - 1
    arrr_range = n
    for i in range(n):
        Max = max(unsorted[0:arrr_range])
        Max_idx = unsorted.index(Max)
        swap(unsorted, lst_idx, Max_idx)
        lst_idx = lst_idx - 1
        arrr_range = arrr_range - 1
    for ele in range(n):
        print(unsorted[ele], end='\n')





if __name__ == '__main__':
    

    num = int(input().strip())

    unsorted = []

    for _ in range(num):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = BigSorting(unsorted)

