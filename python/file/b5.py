f1 = open('input5.txt', 'r')
f2 = open('output5.txt', 'w')


class Student:
    def __init__(self, name, email, phone, point):
        self.name = name
        self.email = email
        self.phone = phone
        self.point = point

    def getName(self):
        s1 = self.name
        ret = s1.title().split()
        return ' '.join(ret)

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    def getPoint(self):
        s1 = list(map(float, self.point.split()))
        total_point = 0.0
        for x in s1:
            total_point += x
        return total_point

    def __str__(self):
        return f'{self.name} {self.email} {self.phone} {self.getPoint()}'


if __name__ == '__main__':
    listStudent = []
    res = []
    for line in f1.readlines():
        listStudent.append(line.strip())
    for i in range(0, len(listStudent), 4):
        name = listStudent[i]
        email = listStudent[i + 1]
        phone = listStudent[i + 2]
        point = listStudent[i + 3]
        s = Student(name, email, phone, point)
        if s.getPoint() >= 27.5:
            res.append(s)
    res.sort(key=lambda x: x.getPoint(), reverse=True)
    for x in res:
        f2.write(x.getName() + '\n')
        f2.write(x.getEmail() + '\n')
        f2.write(x.getPhone() + '\n')
        f2.write(str(x.getPoint()) + '\n')
f1.close()
f2.close()



