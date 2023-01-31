from controller.meta.meta_factory import ProdutoFactory
from database.models.models_concret import Calcados

# Módulo de Transicão de dados a Partir do Modelo (Instâncias, Reponses)


class EstoqueCalcados(ProdutoFactory):
     def __init__(self):
         self.produto = Calcados()
     def services(self, requester: str):
         while requeste := requester is not None:
             if requeste == 'POST':
                 self.produto.manager(opp=1)
             elif requeste == 'PUT':
                 self.produto.manager(opp=2)
             elif requeste == 'DELETE':
                 self.produto.manager(opp=3)
             else:
                 self.produto.manager(opp=4)


     def get_all(self):
         (...)