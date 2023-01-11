class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

instance1 = Singleton()
instance2 = Singleton()

print(f"INstância 1, id: {id(instance1)}")
print(f"INstância 2, id: {id(instance2)}")
