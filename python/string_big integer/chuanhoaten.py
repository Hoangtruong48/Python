from math import *
from functools import cmp_to_key
from collections import Counter
from sys import stdin


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    temp1 = s1.split()
    res1 = ' '.join(temp1)
    res1 = res1.title()
    print(res1)
    temp2 = list(map(int, s2.split('/')))
    dd = ''
    mm = ''
    yyyy = str(temp2[2])
    if temp2[0] < 10:
        temp3 = '0'
        temp3 += str(temp2[0])
        dd = temp3
    else:
        dd = str(temp2[0])
    if temp2[1] < 10:
        temp4 = '0'
        temp4 += str(temp2[1])
        mm = temp4
    else:
        mm = str(temp2[1])
    res2 = dd + '/' + mm + '/' + yyyy
    print(res2)



