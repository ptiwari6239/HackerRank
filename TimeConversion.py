#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time  = s.split(":")

    hr = time[0]

    mn = time[1]
    sec = time[-1]

    if sec[-2] == "A":
        if hr == "12":
            return (f"00:{mn}:{sec[0:2]}")
        else:    
            return (f"{hr}:{mn}:{sec[0:2]}")
    elif sec[-2] == "P":
        if hr == "12":
            return (f"{hr}:{mn}:{sec[0:2]}")
        else: return(f"{int(hr)+12}:{mn}:{sec[0:2]}")     
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
