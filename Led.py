import time
import RPi.GPIO as GPIO
import threading as thr


class Led():
    def __init__(self, pinNrLed=12, dcinit=4):
        self.dutyCycle = dcinit
        self.waitTime = 1
        self.initPin(pinNrLed)       
    
    def initStrob(self):
        def loop(p, thr, t):
            p.ChangeDutyCycle(100)
            while not thr.is_set():
                p.ChangeDutyCycle(100)
                time.sleep(t)
                p.ChangeDutyCycle(0)
                time.sleep(t)
        
        # MAKE SURE THE THREAD IS KILLED PROPERLY
        self.threadStrobStop = thr.Event()
        self.threadStrob = thr.Thread(target=loop, args=(self.pinLed, self.threadStrobStop, self._waitTime))
    
    def getDC(self):
        return self.dutyCycle

    def initPin(self, pinNrLed):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinNrLed, GPIO.OUT)
        
        # freq = 500
        self.pinLed = GPIO.PWM(pinNrLed, 500)
        self.pinLed.start(self.dutyCycle)
        
    def doTask(self, task, *args):
        try:
            self.threadStrobStop.set()
        except:
            pass

        task(*args)

    def doStop(self):
        self.dutyCycle = 0
        self.pinLed.ChangeDutyCycle(self.dutyCycle)
   
    def doToogle(self):
        if self.dutyCycle > 0:
            self.dutyCycle = 0
        else:
            self.dutyCycle = 100
            
        self.pinLed.ChangeDutyCycle(self.dutyCycle)
        
    def doSetLum(self, incr):
        newdc = self.dutyCycle + incr
        if newdc < 0:
            self.dutyCycle = 0
        elif newdc > 100:
            self.dutyCycle = 100
        else:
            self.dutyCycle += incr
            
        self.pinLed.ChangeDutyCycle(self.dutyCycle)
    
    def doStrob(self, spd):
        self.waitTime = spd/float(100)
        print "doStrob", spd, self.waitTime
        
        # MAKE SURE THE THREAD IS KILLED PROPERLY
        self.threadStrobStop.clear()
        self.threadStrob.start()
       
    # feels like it's from an another file
    def processReqData(self, json):
        if json['op'] == "stop":
            self.doTask(self.doStop)
        elif json['op'] == "toogle":
            self.doTask(self.doToogle)
        elif json['op'] == "setLum":
            self.doTask(self.doSetLum, int(json['incr']))
        elif json['op'] == "strob":
            self.doTask(doStrob, int(json['spd']))
    
