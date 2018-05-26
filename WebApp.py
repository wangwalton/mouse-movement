from __future__ import print_function # In python 2.7
from flask import Flask
from flask import render_template
from flask import request
import sys
app = Flask(__name__)

@app.route("/")
def home():
    print('Hello world!', file=sys.stderr)
    return render_template('home.html')

@app.route('/sendjs', methods = ['POST'])
def get_javascript_data():
    jsdatax = request.form['javascript_data_x']
    jsdatay = request.form['javascript_data_y']
    print('X:%s' % jsdatax, file=sys.stderr)
    print('Y:%s' % jsdatay, file=sys.stderr)
    #Send jsdata to backend
    return "nothing"

if __name__ == "__main__":
    app.run(debug=True)
