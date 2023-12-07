from math import *
from functools import cmp_to_key
from collections import Counter
from sys import stdin


if __name__ == '__main__':
    t = int(input())
    mp = dict()
    while t:
        s = input()
        s = s.split()
        passWord = s[len(s) - 1].split('/')
        res1 = []
        if passWord[0][0] == '0':
            temp = passWord[0][1]
            res1.append(temp)
        else:
            res1.append(passWord[0])
        if passWord[1][0] == '0':
            temp = passWord[1][1]
            res1.append(temp)
        else:
            res1.append(passWord[1])
        res1.append(passWord[2])
        passWord1 = ''.join(res1)
        user = s[len(s) - 2].lower()
        for i in range(0, len(s) - 2):
            user += s[i][0].lower()
        if user not in mp:
            mp[user] = 1
            user += '@xyz.edu.vn'
        else:
            mp[user] += 1
            k = str(mp[user]) + '@xyz.edu.vn'
            user += k
        print(user)
        print(passWord1)
        t -= 1







