

class MonoState(object):

    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(
            MonoState, cls,
        ).__new__(cls)
        return obj
