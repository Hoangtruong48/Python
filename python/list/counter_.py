from math import *
from sys import stdin
from functools import cmp_to_key
from collections import Counter
if __name__ == '__main__':
    a = {x: 0 for x in range(15)}
    b = list(a)
    c = Counter(b)
    print(c)
