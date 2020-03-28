class Singleton(type):
    def __init__(self, *args,**kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args,**kwargs):
        if self.__instance is None:
            self.__instance = super.__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Zeus(metaclass=Singleton):
    def _init__(self):
        print('Создается новый обьект', self)

'''
if __name__ == '__main__':
    man = Zeus()
    woman = Zeus()
    print(man is woman)
'''