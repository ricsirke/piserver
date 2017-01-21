from flask import Flask, render_template, request, redirect
import os, json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', toogleBtnVal='ON')
    
@app.route("/led", methods=['POST'])
def led():
    # {"op": "incr", "arg": -20}  ????
    # incr, decr
    # toogle
    # have to store the state of the led
    data = request.form
    print data
    return 'ok'

if __name__ == "__main__":   
    app.run(host="0.0.0.0")
