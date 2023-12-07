import math
from math import *


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def sumOfDigit(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res


def isReverse(n):
    a = str(n)
    l = 1
    r = len(a) - 2
    c = False
    while l <= r:
        if a[l] != a[r]:
            return False
        l += 1
        r -= 1
    return True


def check(n):
    temp1 = n % 10
    temp2 = -1
    while n:
        temp2 = n % 10
        n //= 10
    if temp1 == 2 * temp2 or temp1 * 2 == temp2:
        return True
    return False


dd = []


def sieve():
    for i in range(10001):
        dd.append(1)
    dd[0] = dd[1] = 0
    for i in range(2, int(sqrt(10000) + 1)):
        if dd[i] == 1:
            for j in range(i ** 2, 10000, i):
                dd[j] = 0


def solve():
    a = int(input())
    for i in range(2, a // 2 + 1):
        if isPrime(i) and isPrime(a - i):
            print(i, a - i)


if __name__ == '__main__':
    n = int(input())
    fibo = []
    for i in range(0, 93):
        fibo.append(i)
    fibo[1] = fibo[2] = 1
    for i in range(3, 93):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    while n:
        m = int(input())
        if m in fibo:   print("YES")
        else:   print('NO')
        n -= 1
