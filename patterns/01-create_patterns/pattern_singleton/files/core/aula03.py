from typing import List, Tuple


class Curso:

    def __init__(self: object, nome: str = 'Curso Padrão', carga_horaria: int = 45) -> None:
        self.__nome = nome
        self.__carga_horaria = carga_horaria


curso1: Curso = Curso()
curso2: Curso = Curso(nome='Padrões de Projetos em Python')
curso3: Curso = Curso(nome='Orquestração de Containers com Kubernetes', carga_horaria=23)

# print(curso1.__dict__)
# print(curso2.__dict__)
# print(curso3.__dict__)


nome: str = 'Geek University'
tupla: Tuple = (1, 2, 3, 4, 5)
lista: List = [1, 2, 3, 4, 5]

# print(nome[:4], tupla[:4], lista[:4])


class Pessoa:

    def __init__(self: object, nome: str) -> None:
        self.__nome = nome
    
    def andar(self: object) -> None:
        print('Estou andando...')


class Aluno(Pessoa):

    def __init__(self: object, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.__matricula = matricula


felicity = Aluno('Felicity', '12345')

# felicity.andar()

def gerar_fibonacci(qtd: int) -> None:
    if qtd <= 0:
        print('A quantidade deve ser maior que 0')
    else:
        print(f'A sequência Fibonacci para {qtd} termo(s) é: ')
        contador: int = 0
        aux1: int = 0
        aux2: int = 1
        while contador < qtd:
            print(aux1)
            proximo = aux1 + aux2
            aux1 = aux2
            aux2 = proximo
            contador += 1

# gerar_fibonacci(10)


class Motor:

    def ligar(self: object) -> None:
        print('Motor ligado...')

class Pneu:

    def encher(self: object) -> None:
        print('Pneu cheio')


class Carro:

    def __init__(self: object, modelo: str) -> None:
        self.__modelo = modelo
        self.__motor = Motor()
        self.__pneu1 = Pneu()
        self.__pneu2 = Pneu()
        self.__pneu3 = Pneu()
        self.__pneu4 = Pneu()

fusca = Carro('Fusca')
fusca._Carro__motor.ligar()
