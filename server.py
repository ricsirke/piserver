from flask import Flask, render_template, request, redirect
import os, json, time
import RPi.GPIO as GPIO
import thread as thr

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 500)
dc = 0
p.start(dc)

global thrStrob

app = Flask(__name__)


def doTask(task, *args):
    global thrStrob
    
    try:
        thrStrob.set()
    except:
        pass
        
    task(*args)

    

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
    global thrStrob
    
    t = spd/float(100)
    print "doStrob", spd, t
    
    
    thrStrob = thr.Event()
    
    def loop(thrStrob):
        while not thrStrob.is_set():
            print "inWhile"
            p.ChangeDutyCycle(100)
            time.sleep(t)
            p.ChangeDutyCycle(0)
            time.sleep(t)
        
    #thr.start_new_thread(loop, (thrStrob, ))
    
    
    

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
            doTask(doToogle)
        elif json['op'] == "setLum":
            doTask(doSetLum, int(json['incr']))
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
