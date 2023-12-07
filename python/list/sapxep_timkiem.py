from math import *
from sys import stdin
from functools import cmp_to_key

def sumOfDigit(n):
    Sum = 0
    while n:
        Sum += n % 10
        n //= 10
    return Sum


def binarySreach_first(a, l, r, x):
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            res = mid
            r = mid - 1
        elif a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return res


def binarySreach_last(a, l, r, x):
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            res = mid
            l = mid + 1
        elif a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return res


def binarySreach_first_lonhonhoacbang(a, l, r, x):
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res


#Tìm vị trí đầu tiên lớn hơn x trong mảng
def binarySreach_first_lonhon(a, l, r, x):
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res


if __name__ == '__main__':
    a = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 10]
    print(binarySreach_first(a, 0, len(a) - 1, 2))
    print(binarySreach_last(a, 0, len(a) - 1, 2))
    print(binarySreach_first_lonhonhoacbang(a, 0, len(a) - 1, 2))
    print(binarySreach_first_lonhon(a, 0, len(a) - 1, 2))
