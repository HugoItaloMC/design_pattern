from abc import ABCMeta, abstractmethod

# Principais funcões para objetos


class ProdutoFactory(metaclass=ABCMeta):
    # Factory

    @abstractmethod
    def services(self):
        (...)


    @abstractmethod
    def get_all(self):
        (...)
