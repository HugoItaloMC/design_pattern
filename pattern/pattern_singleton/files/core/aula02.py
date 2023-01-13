from datetime import datetime

class Pessoa:

    def __init__(self: object, nome: str) -> None:
        self.__nome = nome
        self.__nascimento = datetime.now()
    
    def __str__(self: object) -> str:
        return self.__nome
    
    def __repr__(self: object) -> str:
        return self.__nome


class Carro:

    def __init__(self: object, is_sedan: bool = False) -> None:
        self.__is_sedan = is_sedan
        self.__velocidade = 0
        self.__motorista = None
    
    def __str__(self: object) -> str:
        if self.__motorista:
            return f'Carro do(a) {self.__motorista.__nome}'
        return 'Carro sem motorista'
    
    def dirigir(self: object, motorista: Pessoa) -> None:
        self.__motorista = motorista
        self.acelerar(1)
    
    def acelerar(self: object, velocidade: int) -> None:
        self.__velocidade += velocidade
    
    def parar(self: object):
        self.__velocidade = 0

