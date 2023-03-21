from interfaces.label import Produto
from config.db_session import DataBase

import json
# Módulo de Criacão de dados (Dados Brutos, Modelos)


class Calcados(Produto):

    def poster(self):
        _query = f'INSERT INTO calcados (first_name, mind_name, last_name, price, size) VALUES("{self.first_name}", "{self.mind_name}", "{self.last_name}", {float(self.price)}, "{self.size}")'
        DataBase.session(_query)

    def updater(self):
        _query = f'UPDATE calcados SET first_name={self.first_name} mind_name={self.mind_name} last_name={self.last_name} price={self.price} size={self.size}WHERE id={self.id}'
        DataBase.session(_query)

    def remover(self):
        _query = f'DELETE FROM calcados WHERE id={self.id}'
        DataBase.session(_query)

    def getall(self):
        _query = 'SELECT * FROM calcados'
        DataBase.session(_query)

    def get_an(self, id):
        _query = f'SELECT * FROM calcados WHERE id={id}'

    def manager(self, opp: str):
        while op := opp != None:
            if op == 'POST':
                Calcados.poster(self)
            elif op == 'PUT':
                Calcados.updater(self)
            elif op == 'DELETE':
                Calcados.remover(self)
            elif op == 'GETS':
                Calcados.getall(self)
            else:
                Calcados()
    def __iter__(self):
        yield from{
            "id": self.id,
            "Make": (self.first_name + self.mind_name + self.last_name),
            "price": self.price,
            "size": self.size
        }.items()

    def label(self):
        Calcados.__str__ = json.dumps(dict(self), ensure_ascii=False)
        return self.__str__()