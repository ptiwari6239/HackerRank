#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for grade in grades :
        nm = grade 
        for i in range(6):
            nm = nm + 1
            if nm % 5 == 0 :
                break 
            else: continue
        if grade >=38 and nm - grade < 3 :
            print(nm) 
        else : print(grade)           

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

