from model import Calcados
from interfaces.pagine import APIMeta, Page


class Index(Page):

    def __init__(self):
        self.produto = Calcados

    def home_2handler(self):
        self.produto.manager('GETS')
        self.render('index.html', produtos=self.produto)

    def new_2handler(self):
        self.render('new.html')

    def update_2handler(self):
        self.render('update.html')

    def service(self, opp: int):
        while (op := opp != None):
            if op == 1:
                return self.home_2handler()
            elif op == 2:
                return self.new_2handler()
            elif op == 3:
                return self.update_2handler()
            else:
                 ...



class API(APIMeta, Index):

    def _post(self):

        nome = self.get_argument('...', None)
        marca = self.get_argument('...', None)
        modelo = self.get_argument('...', None)
        preco = self.get_argument('...', None)
        tamanho = self.get_argument('...', None)

        self.produto.first_name = nome
        self.produto.mind_name = marca
        self.produto.last_name = modelo
        self.produto.price = preco
        self.produto.size = tamanho
        self.produto.manager('POST')
        self.redirect('index.html')

    def _put(self, id):

        nome = self.get_argument('...', None)
        marca = self.get_argument('...', None)
        modelo = self.get_argument('...', None)
        preco = self.get_argument('...', None)
        tamanho = self.get_argument('...', None)

        self.produto.first_name = nome
        self.produto.mind_name = marca
        self.produto.last_name = modelo
        self.produto.price = preco
        self.produto.size = tamanho

        produto.manager('PUT')
        self.redirect('index.html')

    def _remove(self, id):
        self.produto.get_an(id)
        self.produto.manager('DELETE')
        self.redirect('index.html')
