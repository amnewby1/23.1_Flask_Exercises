# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

import operations

@app.route('/add')
def adding():
    a = (int(request.args.get('a')))
    b = (int(request.args.get('b')))
    return (str(operations.add(a,b)))

@app.route('/sub')
def subtracting():
    a = (int(request.args.get('a')))
    b = (int(request.args.get('b')))
    return (str(operations.sub(a,b)))

@app.route('/mult')
def multiply():
    a = (int(request.args.get('a')))
    b = (int(request.args.get('b')))
    return (str(operations.mult(a,b)))

@app.route('/div')
def divide():
    a = (int(request.args.get('a')))
    b = (int(request.args.get('b')))
    return (str(operations.div(a,b)))

FUNCTIONS = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div
}

@app.route('/math/<function>')
def my_math(function):
    a = (int(request.args.get('a')))
    b = (int(request.args.get('b')))
    my_answer = FUNCTIONS.get(function, "the function does not exist")(a,b)

    return str(my_answer)