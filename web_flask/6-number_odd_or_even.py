#!/usr/bin/python3
'''
a script that starts a flask web application
'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''returns Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def disp_hbnb():
    '''returns HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''dipslay C followed by the value of the text'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def disp_py(text='is cool'):
    '''display Python followed by the value of the text'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def disp_num(n):
    '''display n is a number only n is an integer'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    '''dislay a HTML page only if n is an integer'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    '''dislpays a HTML page only if n is an integer'''
    if n % 2 == 0:
        is_even = 'even'
    else:
        is_even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           is_even=is_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
