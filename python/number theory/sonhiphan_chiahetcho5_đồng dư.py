from sys import stdin
from math import *
from functools import cmp_to_key
from collections import Counter


if __name__ == '__main__':
    s = input()
    res = 1
    MOD = 5
    ans = (int(s[-1]) * res) % MOD
    temp = 0
    for i in range(len(s) - 2, -1, -1):
        res *= 2
        temp = (int(s[i]) * res) % MOD
        ans = (temp + ans) % MOD
    if ans == 0:
        print('YES')
    else:
        print('NO')