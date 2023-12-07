from sys import stdin
from math import *
from collections import Counter
from functools import cmp_to_key


class Person:
    def __init__(self, name, job, salary):
        self.name = name
        self._job = job
        self.__salary = salary

    def showInfor(self):
        print('Name: {}, Job: {}, Salary: {}'.format(self.name, self._job, self.__salary))

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


if __name__ == '__main__':
    p1 = Person('Teo', 'Dev', 232323)
    p1.showInfor()
