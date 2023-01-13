

class MonoState(object):

    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(MonoState, cls,).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._state
        return obj


m1 = MonoState()
print(f"M1 ID: {id(m1)}")
print(m1.__dict__)

m2 = MonoState()
print(f"M2 ID: {id(m2)}")
print(m1.__dict__)

m1.nome = 'felicity'
print(f"M1 Estado -> `__dic__`: {m1.__dict__}")
#
print(f"M2 Estado -> `__dic__`: {m2.__dict__}")
