import math


def binarySreach(a, k, l , r, n):
    mid = (l + r) // 2
    if l == -1 or r == n:
        return False
    if a[mid] == k:
        return True
    elif a[mid] > k:
        binarySreach(a, k, mid + 1, r, n)
    else:
        binarySreach(a, k, l, mid - 1, n)


if __name__ == '__main__':
    n = 10000
    for i in range(1, n):
        print(i, end=' ')



