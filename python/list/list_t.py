from math import *
from sys import stdin
MOD = 10 ** 9 + 7

cnt = [1] * 1000001


def sumOfDigit(n):
    Sum = 0
    while n:
        Sum += n % 10
        n //= 10
    return Sum


if __name__ == '__main__':
    a = [[112, 223], [-212, 124], [-399, 22], [40, 40], [40, 41], [45455, 22]]
    a.sort(key=lambda x: (abs(x[0]), abs(x[1])), reverse=True)
    print(a)






