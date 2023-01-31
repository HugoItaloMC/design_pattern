from database.infra.meta.meta_models import Produto
from database.infra.config.db_session import DataBase

import json
# Módulo de Criacão de dados (Dados Brutos, Modelos)

__execute = DataBase()


class Calcados(Produto):

    def __init__(self):
        self.manager(opp=self)


    def poster(self):
        _query = f'INSERT INTO calcados (first_name, mind_name, last_name, price, size) VALUES("{self.first_name}", "{self.mind_name}", "{self.last_name}", {float(self.price)}, "{self.size}")'
        __execute.session(_query)

    def updater(self):
        _query = 'SQL DML'
        __execute.session(_query)

    def remover(self):
        _query = 'SQL DML'
        __execute.session(_query)

    def get_all(self):
        _query = 'SELECT * FROM calcados'
        __execute.session(_query)


    def manager(self, opp: int):
        while op := opp != None:
            if op == 1:
                Calcados.poster(self)
            elif op == 2:
                Calcados.updater(self)
            elif op == 3:
                Calcados.remover(self)
            elif op == 4:
                Calcados.get_all(self)
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
        return json.dumps(dict(self), ensure_ascii=False)