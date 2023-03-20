from tornado.web import RequestHandler

from models.produto_model import Produto



class Index(RequestHandler):

    def get(self):
        produtos = Produto.get_produtos()
        self.render('index.html', produtos=produtos)

class Novo(RequestHandler):

    def get(self):
        self.render('novo.html')
    
    def post(self):
        nome = self.get_argument('nome', None)
        preco = self.get_argument('preco', None)

        produto = Produto(nome=nome, preco=preco)
        produto.salvar()

        self.redirect('/')


class Atualiza(RequestHandler):

    def get(self, id, status):
        produto = Produto.get_produto(id)
        produto.status = status
        produto.atualizar()

        self.redirect('/')

class Deleta(RequestHandler):

    def get(self, id):
        produto = Produto.get_produto(id)
        produto.deletar()

        self.redirect('/')

