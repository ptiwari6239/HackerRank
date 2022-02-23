

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    point_a = 0
    point_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            point_a = point_a + 1
        elif a[i] < b[i]:
            point_b = point_b + 1
    print(point_a , point_b)        


    pass
    # Write your code here

if __name__ == '__main__':
    

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

