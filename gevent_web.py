# ref: http://flask.pocoo.org/docs/0.10/deploying/wsgi-standalone/
from gevent.wsgi import WSGIServer
from server import app

http_server = WSGIServer(('', 80), app)
http_server.serve_forever()
