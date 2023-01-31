from schemas.schemas_concret import EstoqueCalcados
from controller.meta.meta_single import Singleton

# Fábrica de eventos para objetos

class GerenciamentoEstoque(metaclass=Singleton):

    def signup(self):
        for line in [EstoqueCalcados()]:
            self.line = line
            self.cadastrar = self.line.services('POST')

    def gete(self):
        for line in [EstoqueCalcados()]:
            self.line = line
            self.buscar = self.line.services('GET')

    def updater(self):
        for line in [EstoqueCalcados()]:
            self.line = line
            self.atualizar = self.line.services('PUT')

    def exclude(self):
        for line in [EstoqueCalcados()]:
            self.line = line
            self.remover = self.line.services('DELETE')