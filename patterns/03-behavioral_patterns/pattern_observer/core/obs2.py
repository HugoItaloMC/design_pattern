from abc import ABCMeta, abstractmethod


# Assunto/Tópico
class AgenciaNoticias:

    def __init__(self):
        self.__inscritos = []
        self.__ultima_noticia = None
    
    def inscrever(self, inscrito):
        self.__inscritos.append(inscrito)
    
    def desinscrever(self, inscrito=None):
        if not inscrito: 
           return self.__inscritos.pop()
        else:
            return self.__inscritos.remove(inscrito)
    
    def notificar_todos(self):
        for insc in self.__inscritos:
            insc.notificar()
    
    def adicionar_noticia(self, noticia):
        self.__ultima_noticia = noticia
    
    def mostrar_noticia(self):
        return f'Urgente: {self.__ultima_noticia}'
    
    def inscritos(self):
        return [type(valor).__name__ for valor in self.__inscritos]


# Interface Observer
class TipoInscricao(metaclass=ABCMeta):

    @abstractmethod
    def notificar(self):
        pass


# Observador A
class InscritosSMS(TipoInscricao):

    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)
    
    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')

# Observador B
class InscritosEmail(TipoInscricao):

    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)
    
    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')


# Observador N
class InscritosOutroMeio(TipoInscricao):

    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)
    
    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')



# Cliente
if __name__ == '__main__':
    agencia_noticias = AgenciaNoticias()

    InscritosSMS(agencia_noticias)
    InscritosEmail(agencia_noticias)
    InscritosOutroMeio(agencia_noticias)
    
    print(f'Inscritos: {agencia_noticias.inscritos()}')
    
    agencia_noticias.adicionar_noticia('Novo curso na Geek University')
    agencia_noticias.notificar_todos()

    print(f'Descadastrado: {type(agencia_noticias.desinscrever()).__name__}')
    print(f'Inscritos: {agencia_noticias.inscritos()}')

    agencia_noticias.adicionar_noticia('Design Patterns em Python!')
    agencia_noticias.notificar_todos()


