from math import *
from functools import cmp_to_key
from collections import Counter
from sys import stdin
path1 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
res = []
n, m = 0, 0
u, v = 0, 0
path = []


def loang(i, j):
    res[i][j] = 2
    for x, y in path1:
        i1 = i + x
        j1 = j + y
        if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m and res[i1][j1] == 0:
            if i1 == u and j1 == v:
                return
            else:
                loang(i1, j1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        temp = list(map(int, input().split()))
        res.append(temp)
    s, t = 0, 0
    u, v = n - 1, m - 1
    loang(s, t)
    for i in range(n):
        for j in range(m):
            print(res[i][j], end=' ')
        print()




