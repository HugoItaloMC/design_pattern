from concrets.schemas_concret import EstoqueVestuario, EstoqueCalcados
from abs.meta_single import Singleton
class Estoque(metaclass=Singleton):

    def cadastro(self):
        for line in [EstoqueVestuario(), EstoqueCalcados()]:
            self.line = line
            self.cadastrar = self.line.cadastrar_produto()
