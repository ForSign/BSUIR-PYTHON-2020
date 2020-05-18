from math import sqrt
class Vector:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def sum_vec(self):
        return list(map((lambda x: x[0] + x[1]), zip(self.v1, self.v2)))

    def mul_vec(self):
        return sum(a * b for a, b in zip(self.v1, self.v2))

    def sub_vec(self):
        return list(map((lambda x: x[0] - x[1]), zip(self.v1, self.v2)))

    def mul_const(self, ans):
        return ([ans * a for a in self.v1]), ([ans * a for a in self.v2])

    def comparison(self):
        counter = 0
        for a, b in zip(self.v1, self.v2):
            if a == b:
                counter += 1
            else:
                counter = 0
                return False
            if counter == len(self.v1):
                return True

    def length(self):
        return (sqrt(sum(a ** 2 for a in self.v1))), (sqrt(sum(a ** 2 for a in self.v2)))

    def get_index(self, num):
        if self.v1[num] in self.v1 and self.v2[num] in self.v2:
            return self.v1[num],  self.v2[num]
        else: raise IndexError("IndexError")