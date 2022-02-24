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

def bigSorting(unsorted):
    for i in range(0,len(unsorted)):
        unsorted[i] = int(unsorted[i])
    return unsorted
    def swap(arr,a,b):
        a[i] ,b[i] = b[i],a[i]
        return arr 
    leng = len(unsorted)
    last_idx = n - 1
    arr_range = n 
    for j in range(leng):
        Max = max(unsorted[0:arr_range])
        Max_idx = unsorted.index(Max)
        swap(unsorted,Max,last_idx)
        last_idx = last_idx - 1 
        arr_range = arr_range - 1
    for ele in range(leng):
        print(unsorted[ele],end = '\n')       
         
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
