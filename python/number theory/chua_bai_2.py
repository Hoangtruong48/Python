def tangdan(a, n):
    if n == -1:
        return True
    if a[n - 1] <= a[n - 2]:
        return False
    else:
        return tangdan(a, n - 1)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if tangdan(a, n):
        print('YES')
    else:
        print('NO')
