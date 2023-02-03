from abc import ABCMeta, abstractmethod
from config.db_session import  DataBase


# Interfaces de Modelos (Meta Models)

class Produto(metaclass=ABCMeta):


    def __init__(self, first_name: str, mind_name: str, last_name: str, price: float, size: str):

        self.first_name = first_name
        self.mind_name = mind_name
        self.last_name = last_name
        self.price = price
        self.size = size
        # If not exists table from `calcados` create on database
        query = 'CREATE TABLE IF NOT EXISTS produto (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, mind_name TEXT, last_name TEXT, price REAL, size TEXT'
        DataBase.session(query)
    @abstractmethod
    def manager(self):
         # Master Abstract Method
        (...)

    @abstractmethod
    def label(self):
        # Maker Abstract Method
        (...)
