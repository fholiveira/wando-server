from bottle import route, default_app, template
from wando import run_simple

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run_simple('localhost', 8080, default_app()) 
