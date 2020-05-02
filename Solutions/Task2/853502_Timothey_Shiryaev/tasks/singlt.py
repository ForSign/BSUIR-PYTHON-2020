def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

if __name__ == "__main__":
	
	p = Person('FirstPerson', 17, 80)
	d = Person('Second', 18, 90)

	print(( p ))
	print(( d ))
	print("Equal?: "+ str(p==d) )