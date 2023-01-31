from controller.factory.cadastro_produtos import GerenciamentoEstoque
from controller.meta.meta_single import Singleton

# Módulo Faixada para principal instância


class Cadastro(metaclass=Singleton):


    def manager(self):

        while (op := input('\nEscolha Opcao: ')) != 'sair':
            if int(op) == 1:
                (...)
            elif int(op) == 2:
                print('***  Cadastro Calcados  ***')
                self.calcados = GerenciamentoEstoque()
                self.calcados.signup()
            else:
                Cadastro()
