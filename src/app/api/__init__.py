from gevent import monkey
monkey.patch_all()

from .views import routes
import os
import sys
from flask import Flask


# prevent RecursionError: maximum recursion depth exceeded while calling a Python object
sys.setrecursionlimit(100000000)

application = Flask(__name__)
application.register_blueprint(routes)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
