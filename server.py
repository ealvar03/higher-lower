from flask import Flask
import random

app = Flask(__name__)
rand_number = random.randint(0, 9)

@app.route('/')
def guess_number():
    return '<h1> Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def compare_numbers(number):

    if number < rand_number:
        return '<h1 style="color:red;">Oh, too low! Try again!</h1>' \
               '<img src="https://media0.giphy.com/media/XB3fsooiXcLVqCa7xe/giphy.gif?cid=ecf05e4713b2s4i350pejbp5alr' \
               '8y77v71i5jg16axu0u0qd&rid=giphy.gif&ct=g">'
    elif number > rand_number:
        return '<h1 style="color:blue;">Too high, try again!</h1>' \
               '<img src="https://media0.giphy.com/media/jC3ch3iS5459ozziVv/giphy.gif?cid=ecf05e4777vwicd604q5eddcd' \
               'xvvt45us84mjg7ys5ac60m0&rid=giphy.gif&ct=g">'
    else:
        return '<h1 style="color:green;">Well done!</h1>' \
               '<img src="https://media1.giphy.com/media/CPuFj9CBRRtBPGK3MY/giphy.gif?cid=ecf05e47duhk7jertpawkrxg' \
               '4bthz6mj6gaud11l59bdv1jy&rid=giphy.gif&ct=g">'


if __name__ == '__main__':
    app.run(debug=True)
