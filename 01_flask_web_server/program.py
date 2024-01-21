# Install python module flask:
# > python -m pip install flask
#
# Run this program:
# > python program.py
#
# Use this program/web server:
# - Find the url in the console and open this in the browser (For example http://127.0.0.1:5000/). It should now display "Hellow world" in the browser.
# - Add a number at the end of the url (For example http://127.0.0.1:5000/42). It should now display "Hello, world with number: 42" in the browser.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return f'Hello, world'

@app.route('/<int:number>')
def hello_number(number):
    return f'Hello, world with number: {number}'

if __name__ == '__main__':
    app.run()
