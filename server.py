from flask import Flask, render_template, request, redirect
import os, json
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 500)
dc = 0
p.start(dc)



app = Flask(__name__)


def doToogle():
    global dc

    if dc > 0:
        dc = 0
    else:
        dc = 100

    p.ChangeDutyCycle(dc)


def doSetLum(incr):
    global dc
    
    newdc = dc + incr
    if newdc < 0:
        dc = 0
    elif newdc > 100:
        dc = 100
    else:
        dc += incr
    p.ChangeDutyCycle(dc)


@app.route("/")
def hello():
    return render_template('index.html', toogleBtnVal='toogle')
    
@app.route("/led", methods=['POST'])
def led():
    # have to store the state of the led
    form = request.form
    print form
    
    if form['dev'] == "led":
        global dc
        if form['op'] == "toogle":
            doToogle()
        elif form['op'] == "setLum":
            doSetLum(int(request.form['incr']))

        print dc
    
    elif request.form['targetDevType'] == "radio":
        if request.form['op'] == "start":
            pass
        elif form['op'] == "stop":
            pass
        elif form['op'] == "next":
            pass
        elif form['op'] == "prev":
            pass
    
    return 'ok'

if __name__ == "__main__":   
    app.run(host="0.0.0.0")
