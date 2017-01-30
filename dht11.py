import Adafruit_DHT, time
from datetime import datetime

def avg(l):
    return sum(l)/len(l)

def printData(temperature, humidity):
    print "t", datetime.now(), "T", str(temperature) + "C", "h", str(humidity) + "%"

def log(logfile, temp, hum):
    with open(logfile, "a") as f:
        f.write(str(datetime.now()) + "," + str(temp) + "," + str(hum) + "\n")

def monitor(sleep, bLog):
    try:
        while 1:
            hum, temp = avgData(4)
            printData(temp, hum)
            if bLog:
                log("log/temphum.log", temp, hum)
            time.sleep(sleep)
            #time.sleep(sleep)
    except KeyboardInterrupt:
        pass

def avgData(samplesize):
    hums = []
    temps = []
    for i in range(samplesize):
        hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, '4')
        hums.append(hum)
        temps.append(temp)
        time.sleep(0.1)
    
    avg_hum = avg(hums)
    avg_temp = avg(temps)

    return avg_temp, avg_hum

#avg_temp, avg_hum = avgData(5)
#printData(avg_temp, avg_hum)


monitor(0, False)
