import RPi.GPIO as IO
import time

def initIO():
    IO.setwarnings(False)
    IO.setmode(IO.BCM)             #we are programming the GPIO by BCM pin numbers. (PIN35 as 'GPIO19')
    IO.setup(19, IO.OUT)           # initialize GPIO19 as an output.

def loop(p):
    while 1:
        for x in range (50):
            p.ChangeDutyCycle(x)
            time.sleep(0.1)
          
        for x in range (50):
            p.ChangeDutyCycle(50-x)
            time.sleep(0.1)
    



    
initIO()

p = IO.PWM(19, 100)            #GPIO19 as PWM output, with 100Hz frequency
p.start(0)                     #generate PWM signal with 0% duty cycle

pins = [ { "name": "lol", "pin": 19, "dc": 0, "obj": p } ]

press = False
if press:
    # ha megnyomom a gombot a honlapon, akkor kapcsoljon ki és be, majd csak csokkenti a fenyerot is masik gombbal...
    p.ChangeDutyCycle(p.)


