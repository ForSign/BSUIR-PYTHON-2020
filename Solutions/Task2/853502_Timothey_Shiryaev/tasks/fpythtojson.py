from singlt import singleton

@singleton
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
p = Person('Tom', 17, 80)
d = Person('Delted', 17, 80)
print ("\nSingleton works?= " + str(p==d), end="\n\n")

def classtojsn(obj):
    z = {}

    for i in dir(obj):
        if not i.startswith('_') :
            z[i]=getattr(obj, i)

    return z

classtojsn(p)


def to_json(obj):
    if obj is None:
        return "null"
    if isinstance(obj, bool):
        return str(obj).lower()
    if isinstance(obj, (int, float)):
        return str(obj)
    if isinstance(obj, str):
        return f'"{obj}"'
    if isinstance(obj, (tuple, list)):
        return str(list(obj))

    return classtojsn(obj)

print('List:', to_json(["apple", "bananas"]))
print('Tuple:', to_json(("apple", "bananas")))
print('String:', to_json("hello"))
print('Int:', to_json(42))
print('Float:', to_json(31.76))
print('True:', to_json(True))
print('False:', to_json(False))
print('Class:', to_json(p))
