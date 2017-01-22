from flask import Flask, render_template, request, redirect
import os, json, time
import RPi.GPIO as GPIO
from ThreadX import ThreadX

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 500)
dc = 0
p.start(dc)

global thrStrob

app = Flask(__name__)


def doTask(task):
    global thrStrob
    
    try:
        thrStrob.stop()
    except:
        pass
        
    task()

    

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
    
def doStrob(spd):
    global dc
    global thrStrob
    
    thrStrob = ThreadX()
    
    def loop():
        p.ChangeDutyCycle(100)
        time.sleep(spd/100)
        p.ChangeDutyCycle(0)
        time.sleep(spd/100)

    thrStrob.run(loop)
    
    

@app.route("/")
def hello():
    return render_template('index.html', toogleBtnVal='toogle')
    
@app.route("/led", methods=['POST'])
def led():
    # have to store the state of the led
    json = request.get_json()
    print "json:", json, "\n\n"
    
    if json['dev'] == "led":
        global dc
        if json['op'] == "toogle":
            doToogle()
        elif json['op'] == "setLum":
            doSetLum(int(json['incr']))
        elif json['op'] == "strob":
            doStrob(int(json['spd']))

        print dc
    
    elif request.json['targetDevType'] == "radio":
        if request.json['op'] == "start":
            pass
        elif json['op'] == "stop":
            pass
        elif json['op'] == "next":
            pass
        elif json['op'] == "prev":
            pass
    
    return 'ok'

if __name__ == "__main__":   
    app.run(host="0.0.0.0")
