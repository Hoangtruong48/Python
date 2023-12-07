f1 = open('input4.txt', "r")
f2 = open('output4.txt', 'w')


def user(s):
    k = s.lower().split()
    users = str(k[-1])
    for i in range(len(k) - 1):
        users += k[i][0]
    return users + '@28land.edu.vn'


def passWord(s):
    k = s.split('/')
    ret = ''
    for x in k:
        ret += str(int(x))
    return ret


if __name__ == '__main__':
    res = []
    for line in f1.readlines():
        res.append(line.strip())
    for i in range(0, len(res), 2):
        tk = user(res[i])
        mk = passWord(res[i + 1])
        f2.write(tk + '\n')
        f2.write(mk + '\n')
    f1.close()
    f2.close()