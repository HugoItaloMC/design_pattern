from concrets.schemas_concret import EstoqueVestuario, EstoqueCalcados

class Estoque:

    def cadastro(self):
        for line in [EstoqueVestuario(), EstoqueCalcados()]:
            self.line = line
            self.cadastrar = self.line.cadastrar_produto()
            self.escolher = self.line.escolher_produto()
