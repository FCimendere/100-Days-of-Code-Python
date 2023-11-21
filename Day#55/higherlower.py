#Project : Higher Lower Game 
"""
PRACTISE: HTML&URL Parsing with Flask
PROJECT: This is a basic HTML and URL parsing with Flask.
The program will start on the home page, with a welcome and a picture. 
A random will have been created and the user will try to guess it. 
Users need to put a number at the end of the URL. E.g. http://127.0.0.1:5000/1
Depending on the user's guess, the screen will show low, high, or found replies with related images.
"""

from flask import Flask
import random

app = Flask(__name__)
# print(__name__)

# random number will be created
random_number = random.randint(0, 9)

#comparison between ser guess and random number. 
#decorator function will change the color and picture. 
@app.route('/<int:number>')
def greet(number):
    if number > random_number:
        text = "<h1 style='color:red;'>Too high, try again!</h1>" \
                "<img src='https://media2.giphy.com/media/Jd5YlXOVTcQtW/200w.webp?cid=ecf05e4773yti6dvcx779j6qfw61h03taqqd3tc2382o18jz&ep=v1_gifs_search&rid=200w.webp&ct=g' width='300' >"
    elif number < random_number:
        text = "<h1 style='color:blue;'>Too low, try again!</h1>" \
                "<img src='https://media3.giphy.com/media/ykS9B0nqIydvq/200.webp?cid=ecf05e4757vsheu711itf4tpgbm15d8kcbrcpfaaugi8xo72&ep=v1_gifs_search&rid=200.webp&ct=g' width='300' >"
    else:
        text = "<h1 style='color:purple;'>You found me!</h1>" \
                "<img src='https://media3.giphy.com/media/7SfAXqgRgh0li/200.webp?cid=ecf05e47imzn1mf6600d877fjkcfpajzn7ke7zdzxgc97dvc&ep=v1_gifs_search&rid=200.webp&ct=g' width='300' >"
    return text

#home page setting
@app.route('/')
def start_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='300' >"


if __name__ == "__main__":
    app.run(debug=True)
