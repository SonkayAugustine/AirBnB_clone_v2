#!/usr/bin/python3
'''
a script starts a Flask web_application
'''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    displays Hello HBNB!
    '''

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def disp_hbnb():
    '''
    display HBNB
    '''

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
    display C followed by value of text
    '''

    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
