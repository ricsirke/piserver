import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)


t = 0.01
fr = 500

p = GPIO.PWM(12, fr) # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(t)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(t)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    








def test_led():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    
    t=0.6
    try:
        while True:
            print 'on'
            GPIO.output(12, 1)
            time.sleep(t)
            print 'off'
            GPIO.output(12, 0)
            time.sleep(t)
    except KeyboardInterrupt:
        GPIO.cleanup()
    

