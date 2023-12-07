from sys import stdin
from math import *
from functools import cmp_to_key
from collections import Counter


def check(n):
    temp = n % 10
    n //= 10
    while n:
        if n % 10 > temp:
            return False
        else:
            temp = n % 10
            n //= 10
    return True


if __name__ == '__main__':
    d = dict()
    for line in stdin:
        a = list(map(int, line.split()))
        for x in a:
            if check(x):
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
    res = []
    for x, y in d.items():
        res.append([x, y])
    res.sort(key=lambda x: (-x[1], x[0]))
    for x in res:
        print(x[0], x[1])



