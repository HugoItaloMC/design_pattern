

class LazySingleton(object):

    _instance = None

    def __init__(self):
        if not LazySingleton._instance:
            print("Object Not instanced")
        else:
            print(self.get_instance(),
                  '\nIs Instanced Object')

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = LazySingleton()
        return cls._instance


s1 = LazySingleton()  # Sem instância
print(f"{LazySingleton.get_instance()}")  # Gerando Inst6ancia
s2 = LazySingleton()  # Com instância
