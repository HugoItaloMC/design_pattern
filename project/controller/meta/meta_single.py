from typing import Dict

# Controle de instâncias de objetos


class Singleton(type):

    __instance: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]