from math import sqrt
class Vector:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        print('First vector:' + str(v1) + '\n' + 'Second vector:' + str(v2))

    def sumVec(self):
        print('Addition:')
        return(list(map((lambda x: x[0] + x[1]), zip(self.v1, self.v2))))

    def mulVec(self):
        print('Multiplication:')
        return(sum(a * b for a, b in zip(self.v1, self.v2)))

    def subVec(self):
        print('Substraction:')
        return(list(map((lambda x: x[0] - x[1]), zip(self.v1, self.v2))))

    def mulConst(self, ans):
        print('Multiplication on const: (*8)')
        return([ans * a for a in self.v1]), ([ans * a for a in self.v2])
    def comparison(self):
        counter = 0
        for a, b in zip(self.v1, self.v2):
            if a == b:
                counter += 1
            else:
                counter = 0
                print("Vectors are not equal")
                break
            if counter == len(self.v1):
                print('Vectors are equal')
    def length(self):
        print('Length of vectors:')
        print(sqrt(sum(a ** 2 for a in self.v1)))
        print(sqrt(sum(a ** 2 for a in self.v2)))
    def getInd(self, num):
        try:

            if self.v1[num] in self.v1 and self.v2[num] in self.v2:
                return self.v1[num],  self.v2[num]
        except:
            print('Wrong index')


v1 = [-3, 4]
v2 = [11, 22]

obj = Vector(v1, v2)

sv = obj.subVec()
print(sv)
mc = obj.mulConst(8)
print(mc)
mv = obj.mulVec()
print(mv)
sumv = obj.sumVec()
print(sumv)
com = obj.comparison()

l = obj.length()
ind1, ind2 = obj.getInd(1)
print('Indexes:\n',ind1,'\n',ind2)

