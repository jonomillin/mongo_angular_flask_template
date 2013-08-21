#!venv/bin/python
from flask import Flask
import blueprints.blueprints 
# import blueprints.registration
import blueprints.api
from models.models import connection
import os
# from cherrypy import wsgiserver
import flask
from werkzeug import wsgi
import json
import logging
import os
import os.path
import threading
import types

app = Flask(__name__)
app.config.from_pyfile('config/config.py')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.register_blueprint(blueprints.blueprints.page)
# app.register_blueprint(blueprints.registration.registration_pages)
app.register_blueprint(blueprints.api.api_pages)
	
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)


