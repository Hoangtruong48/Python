from math import *
n, m = 0, 0
arr = []
path = [[- 2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
u, v = 0, 0
path1 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dem = 0


def loang(i, j):
    arr[i][j] = 0
    global dem
    dem += 1
    for x, y in path1:
        i1 = i + x
        j1 = j + y
        if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m and arr[i1][j1] == 1:
            loang(i1, j1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    ans = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                dem = 0
                loang(i, j)
                ans = max(ans, dem)
    print(ans)
