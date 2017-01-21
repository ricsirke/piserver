import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)             #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
IO.setup(19, IO.OUT)           # initialize GPIO19 as an output.

p = IO.PWM(19, 100)            #GPIO19 as PWM output, with 100Hz frequency
p.start(0)                     #generate PWM signal with 0% duty cycle

while 1:
    for x in range (50):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
      
    for x in range (50):
        p.ChangeDutyCycle(50-x)
        time.sleep(0.1)