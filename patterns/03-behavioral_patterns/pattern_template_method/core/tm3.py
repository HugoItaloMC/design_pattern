from abc import ABCMeta, abstractmethod


class Viagem(metaclass=ABCMeta):

    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass

    @abstractmethod
    def retorno(self):
        pass
    
    def itinerario(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retorno()


class ViagemVeneza(Viagem):

    def ida(self):
        print('Viagem de avião...')
    
    def dia1(self):
        print('Visita à Basílica de São Marcos na Praça São Marcos')
    
    def dia2(self):
        print('Visita ao Palácio Doge')
    
    def dia3(self):
        print('Aproveitar a comida próximo à Ponte Rialto')
    
    def retorno(self):
        print('Viagem de avião...')


class ViagemMalvinas(Viagem):

    def ida(self):
        print('Viagem de ônibus...')
    
    def dia1(self):
        print('Apreciar a vida varinha de Banana Reef')
    
    def dia2(self):
        print('Praticar esportes aquáticos')
    
    def dia3(self):
        print('Relaxar na praia e aproveitar o sol')
    
    def retorno(self):
        print('Viagem de avião...')



class GeekTravel:

    def preparar_viagem(self):
        opcao = input('Qual local de viagem deseja fazer? [Veneza, Malvinas]: ')

        if opcao == 'Veneza':
            self.viagem = ViagemVeneza()
            self.viagem.itinerario()
        elif opcao == 'Malvinas':
            self.viagem = ViagemMalvinas()
            self.viagem.itinerario()
        else:
            print('Opção inválida')


agencia = GeekTravel()
agencia.preparar_viagem()

