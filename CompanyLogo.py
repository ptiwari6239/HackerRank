import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
from collections import Counter
seq = sorted(s)
x = Counter(seq)
key = []
value = []
for i in x:
    key.append(i)
    value.append(x[i])
final = dict(zip(key, value))
counter = 0
while counter <= 2:
    Keymax = max(final, key=lambda x: final[x])
    print(Keymax, final[Keymax])
    final.pop(Keymax)
    counter += 1
