from __future__ import print_function  # In python 2.7
from flask import Flask, render_template, request
import main
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/officials', methods=['POST'])
def officials():
    print(request.form['address'])

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
