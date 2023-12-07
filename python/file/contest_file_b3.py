import math

f1 = open('input3.txt', "r")
f2 = open("output3.txt", "w")
a = list(map(int, f1.read().split()))


def isPrime(n):
    if n < 2:   return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:  return False
    return True


res = []
for x in a:
    if isPrime(x):
        res.append(x)
res.sort()
for x in res:
    f2.write(str(x))
    f2.write(' ')
f1.close()
f2.close()