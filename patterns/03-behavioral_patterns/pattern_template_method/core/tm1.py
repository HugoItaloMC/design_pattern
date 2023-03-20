from abc import ABCMeta, abstractmethod


class Compilador(metaclass=ABCMeta):

    @abstractmethod
    def coletar_fonte(self):
        pass

    @abstractmethod
    def compilar_objeto(self):
        pass

    @abstractmethod
    def executar(self):
        pass

    def compilar_e_executar(self):
        self.coletar_fonte()
        self.compilar_objeto()
        self.executar()


class CompiladorIOS(Compilador):

    def coletar_fonte(self):
        print('Coletando código fonte Swift')
    
    def compilar_objeto(self):
        print('Compilando código Swift para bytecode LLVM')
    
    def executar(self):
        print('Programa executando no ambiente de execução')


class CompiladorAndroid(Compilador):

    def coletar_fonte(self):
        print('Coletando código fonte Kotlin')
    
    def compilar_objeto(self):
        print('Compilando código Kotlin para bytecode JVM')
    
    def executar(self):
        print('Programa executando no ambiente de execução')



ios = CompiladorIOS()
ios.compilar_e_executar()

android = CompiladorAndroid()
android.compilar_e_executar()
