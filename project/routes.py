from tornado.web import Application
from api import API, Index

class Routes(Application):
    def __init__(self):

        handlers = [
            ('/home', Index),
            ('/produto/new', API._post),
            ('/produto/update/(\d+)/id/(\d+)', API._put),
            ('/produto/delete/(\d+)', API._remove)
        ]

        settings = dict(
            debug=True,
            template_path='template',
            static_path='static',
        )

        Application.__init__(self, handlers, **settings)
