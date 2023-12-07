class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def __add__(self, other):
        temp = self.thuc + other.thuc
        temp1 = self.ao + other.ao
        return SoPhuc(temp, temp1)

    def __eq__(self, other):
        if self.thuc == other.thuc and self.ao == other.ao:
            return True
        return False

    def __str__(self):
        return f'{self.thuc} + {self.ao}j'


if __name__ == '__main__':
    s1 = SoPhuc(1, 2)
    s2 = SoPhuc(1, 2)
    print(s1.__eq__(s2))
