from math import *
from functools import cmp_to_key
from sys import stdin
from collections import Counter

fibo = [0] * 93


def init():
    fibo[1] = 1
    for i in range(2, 93):
        fibo[i] = fibo[i - 1] + fibo[i - 2]


if __name__ == '__main__':
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    val = 1
    h1, c1, h2, c2 = 0, 0, n - 1, n - 1
    init()
    while val < n * n:
        for i in range(c1, c2 + 1):
            a[h1][i] = fibo[val]
            val += 1
        h1 += 1
        for i in range(h1, h2 + 1):
            a[i][c2] = fibo[val]
            val += 1
        c2 -= 1
        for i in range(c2, c1 - 1, - 1):
            a[h2][i] = fibo[val]
            val += 1
        h2 -= 1
        for i in range(h2, h1 - 1, -1):
            a[i][c1] = fibo[val]
            val += 1
        c1 += 1
    for arr in a:
        for x in arr:
            print(x, end=' ')
        print()
