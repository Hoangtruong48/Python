from functools import cmp_to_key


class Person:
    def __init__(self, name, dOB, address):
        self.name = name
        self.dOB = dOB
        self.address = address

    def conVertName(self):
        return ' '.join(self.name.split()).title()

    def getName(self):
        return self.name

    def conVertDOB(self):
        temp = self.dOB.split('/')
        d, m, y = temp[0], temp[1], temp[2]
        dd, mm, yyyy = '', '', ''
        if int(d) < 10:
            dd = '0' + str(int(d))
        else:
            dd = str(int(d))
        if int(m) < 10:
            mm = '0' + str(int(m))
        else:
            mm = str(int(m))
        if int(y) < 10:
            yyyy = '000' + y
        elif int(y) < 100:
            yyyy = '00' + y
        elif int(y) < 1000:
            yyyy = '0' + y
        else:
            yyyy = y
        return [dd, mm, yyyy]

    def __str__(self):
        name_ = Person.conVertName(self)
        dob = '/'.join(Person.conVertDOB(self))
        return f'{name_} {dob} {self.address} '


class Student(Person):
    def __init__(self, code, name, dOB, address, lop, gpa):
        self.code = code
        super().__init__(name, dOB, address)
        self.lop = lop
        self.gpa = gpa

    def getCode(self):
        return self.code

    def __str__(self):
        #print(self.code)
        return f'{self.code} ' + Person.__str__(self) + f'{self.lop} {self.gpa:.2f}'


def cmp(s):
    a = s.split()
    res = a[-1] + ' '
    res += ' '.join(a[:-1])
    return res


if __name__ == '__main__':
    n = int(input())
    res = []
    for i in range(1, n + 1):
        code = ''
        if i < 10:
            code = '000' + str(i)
        elif i < 100:
            code = '00' + str(i)
        elif i < 1000:
            code = '0' + str(i)
        else:
            code = str(i)
        name = input()
        dOB = input()
        address = input()
        lop = input()
        gpa = float(input())
        student = Student(code, name, dOB, address, lop, gpa)
        res.append(student)
    res.sort(key=lambda x: (cmp(x.getName())))
    for i in range(int(len(res))):
        print(res[i])

