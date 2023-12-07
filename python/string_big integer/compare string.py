from math import *
from functools import cmp_to_key
from collections import Counter
from sys import stdin


def cmp(s1, s2):
    if len(s1) != len(s2):
        if len(s1) < len(s2):
            return -1
        else:
            return 1
    else:
        return len(s1) - len(s2)


if __name__ == '__main__':
    s = input()
    res = list(s.split())
    res.sort()
    for x in res:
        print(x, end=' ')
    print()
    res.sort(key=cmp_to_key(cmp))
    for x in res:
        print(x, end=' ')



