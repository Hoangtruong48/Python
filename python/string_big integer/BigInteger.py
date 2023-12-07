from sys import stdin
from math import *
from functools import cmp_to_key
from collections import Counter


def cmp(a, b):
    ab = a + b
    ba = b + a
    if ab > ba:
        return -1
    else: return 1


if __name__ == '__main__':
    s = input()
    temp = ''
    res = []
    for x in s:
        if x.isalpha():
            temp += ' '
        else:
            temp += x
    res = list(map(int, temp.split()))
    res1 = list(map(str, res))
    res1.sort(key=cmp_to_key(cmp))
    print(''.join(res1))


