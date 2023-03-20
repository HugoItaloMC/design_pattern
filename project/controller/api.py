from abc import ABC

from models.model import Calcados
from interfaces.pagine import APIMeta, Page


class Index(Page):

    def renderizer(self, template: str):
        return self.render(template)

    def service(self):
        # Renderizar Home Page
        produto = Calcados.getall()
        self.render('index.html', produto=produto)


class API(APIMeta):

    def _post(self):
        Index.renderizer('novo.html')

        nome = self.get_argument('...', None)
        marca = self.get_argument('...', None)
        modelo = self.get_argument('...', None)
        preco = self.get_argument('...', None)
        tamanho = self.get_argument('...', None)

        self.produto = Calcados(first_name=nome,
                                mind_name=marca,
                                last_name=modelo,
                                price=float(preco),
                                size=tamanho)
        self.produto.manager('POST')
        self.redirect('index.html')

    def _put(self):
        ...

    def _get_an(self):
        ...

    def _get(self):
        ...