from __future__ import print_function  # In python 2.7
from flask import Flask, render_template, request
from main import API_KEY, get_data

import pprint

pp = pprint.PrettyPrinter(indent=2)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("POST")
        address = request.form['jobnumber']
        elections = get_data(address)
        html = "<div>"
        html += "Address: %s </br>" % address
        html += "Elections: </br>"
        html += "<ul>"
        for name, day, division in elections:
            html += "<li>" + name + "</li>"
            html += "<ul>"
            html += "<li>Election day: " + day + "</li>"
            html += "<li>Division: " + division + "</li>"
            html += "</ul>"
        html += "</ul>"
        html += "</div>"
        return html
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', threaded=True, debug=True)
