from tornado.web import RequestHandler
from abc import ABCMeta, abstractmethod

class Page(RequestHandler, metaclass=ABCMeta):

    @abstractmethod
    def renderizer(self, *args, **kwargs):
        # Buscar Template Para renderizar
        (...)

    @abstractmethod
    def service(self):
        # Atribuir Servicos
        (...)

class APIMeta(RequestHandler, metaclass=ABCMeta):
    # Interface API
    @abstractmethod
    def _post(self):
        (...)

    @abstractmethod
    def _put(self):
        (...)

    @abstractmethod
    def _get_an(self):
        (...)

    @abstractmethod
    def _get(self):
        (...)