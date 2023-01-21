from abc import ABCMeta, abstractmethod

class Calcados(metaclass=ABCMeta):

    @abstractmethod
    def label(self, Tenis):
        pass


class Vestuario(metaclass=ABCMeta):

    @abstractmethod
    def label(self, Camisa):
        pass