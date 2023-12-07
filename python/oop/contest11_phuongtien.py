from functools import cmp_to_key


class Vehicle:
    def __init__(self, code, name, firm, color, price):
        self.code = code
        self.name = name
        self.firm = firm
        self.color = color
        self.price = price

    def getFirm(self):
        return self.firm

    def getPrice(self):
        return int(self.price)

    def getCode(self):
        return self.code

    def getName(self):
        return self.name


class Motorbike(Vehicle):
    def __init__(self, code, name, firm, color, attribute1, price):
        super().__init__(code, name, firm, color, price)
        self.attribute1 = attribute1

    def __str__(self):
        return f'{self.code} {self.name} {self.firm} {self.color} {self.attribute1} {self.price}'


class Car(Vehicle):
    def __init__(self, code, name, firm, color, attribute2, price):
        super().__init__(code, name, firm, color, price)
        self.attribute2 = attribute2

    def __str__(self):
        return f'{self.code} {self.name} {self.firm} {self.color} {self.attribute2} {self.price}'


if __name__ == '__main__':
    n = int(input())
    carList = []
    motorbikeList = []
    for i in range(n):
        code = input()
        if code[0] == 'O':
            carList.append(Car(code, input(), input(), input(), input(), input()))
        else:
            motorbikeList.append(Car(code, input(), input(), input(), input(), input()))
    queries = input()
    print('DANH SACH OTO :')
    for x in carList:
        if x.getName() == queries:
            print(x)
    print('DANH SACH XE MAY :')
    for x in motorbikeList:
        if x.getName() == queries:
            print(x)

