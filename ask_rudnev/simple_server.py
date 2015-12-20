from wsgiref import simple_server
from simple_wsgi import app

server = simple_server.WSGIServer(
            ('', 8085),
            simple_server.WSGIRequestHandler,
        )
server.set_app(app)
server.serve_forever()

