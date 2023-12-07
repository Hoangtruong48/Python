from functools import cmp_to_key


class Person:
    def __init__(self, code, name, dOB, address):
        self.code = code
        self.name = name
        self.dOB = dOB
        self.address = address

    def conVertName(self):
        return ' '.join(self.name.split()).title()

    def getAddress(self):
        return self.address

    def getCode(self):
        return self.code

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
        return f'{self.code} {name_} {dob} {self.address}'


class Student(Person):
    def __init__(self, code, name, dOB, address, grade, gpa):
        super().__init__(code, name, dOB, address)
        self.grade = grade
        self.gpa = gpa

    def getGPA(self):
        return self.gpa

    def getGrade(self):
        return self.grade

    def __str__(self):
        return Person.__str__(self) + ' ' + f'{self.grade} {self.gpa:.2f}'


class Teacher(Person):
    def __init__(self, code, name, dOB, address, faculty, salary, grade__):
        super().__init__(code, name, dOB, address)
        self.faculty = faculty
        self.salary = salary
        self.grade__ = grade__

    def getSalary(self):
        return self.salary

    def getGrade__(self):
        return self.grade__

    def __str__(self):
        return Person.__str__(self) + ' ' + f'{self.faculty} {self.salary:.0f} {self.grade__}'


if __name__ == '__main__':
    n = int(input())
    studentList = []
    teacherList = []
    for i in range(n):
        code = input()
        name = input()
        dOB = input()
        address = input()
        attributes1 = input()
        attributes2 = float(input())
        if code[:2] == 'GV':
            k = input()
            teacherList.append(Teacher(code, name, dOB, address, attributes1, attributes2, k))
        else:
            studentList.append(Student(code, name, dOB, address, attributes1, attributes2))
    queries = input()
    print('DANH SACH GIAO VIEN PHU TRACH LOP {} :'.format(queries))
    for x in teacherList:
        if x.getGrade__() == queries:
            print(x)
    print('DANH SACH SINH VIEN LOP {} :'.format(queries))
    for x in studentList:
        if x.getGrade() == queries:
            print(x)
