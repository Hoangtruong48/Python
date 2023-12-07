from sys import stdin
from math import *
from collections import Counter
from functools import cmp_to_key


def squareMagic(a):
    if len(a) == len(a[0]):
        return True
    return False


def duongCheoChinh(a):
    res = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == j:
                res.append(a[i][j])
    return res


def duongCheoPhu(a):
    res = []
    temp = len(a) - 1
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i + j == temp:
                res.append(a[i][j])
    return res


def tongTamGiacTren(a):
    res = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if j > i:
                res += a[i][j]
    return res


def tongTamGiacDuoi(a):
    res = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if j < i:
                res += a[i][j]
    return res


def maTranChuyenVi(a):
    n = len(a)
    m = len(a[0])
    res = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[j][i]
    return b


def congMaTran(a, b):
    n = len(a)
    m = len(a[0])
    res = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = a[i][j] + b[i][j]
    return res


def nhanHaiMaTran(a, b):
    row = len(a)
    col = len(b[0])
    res = [[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            for k in range(len(a[0])):
                res[i][j] += a[i][k] * b[k][j]
    return res


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0 for i in range(n)] for j in range(m)]
    b = [x for small_list in a for x in small_list]
    res = [[0 for i in range(m)] for j in range(n)]
    print(res)
    print(b)
    d = [[1, 2, 3], [1, 2, 3], [8, 5, 2]]
    e = [[1, 2], [1, 2], [1, 2]]
    print(nhanHaiMaTran(d, e))


