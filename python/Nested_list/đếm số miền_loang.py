from math import *
from functools import cmp_to_key
from sys import stdin
from collections import Counter
path1 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
path2 = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
arr = []
n, m = 0, 0


def check(i ,j):
    for x, y in path2:
        i1 = i + x
        j1 = j + y
        if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m:
            if arr[i1][j1] >= arr[i][j]:
                return False
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if check(i, j):
                cnt += 1
    print(cnt)

