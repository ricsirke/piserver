import Led, Radio

led = Led()
radio = Radio()




import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    if led.dutyCycle > 0:
        toogleBtnText = 'off'
    else:
        toogleBtnText = 'on'
        
    return render_template('index.html', toogleBtnVal=toogleBtnText)


@app.route("/led", methods=['POST'])
def led():
    # have to store the state of the led
    json = request.get_json()
    print "\n\njson:", json, "\n\n"
    
    if json['dev'] == "led":
        led.processReqData(json)
        print led.dutyCycle

    # TODO in contradiction with the url path
    elif json['targetDevType'] == "radio":
        radio.processReqData(json)
    
    return 'ok'

if __name__ == "__main__":   
    app.run(host="0.0.0.0")
