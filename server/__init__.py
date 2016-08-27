from time import sleep

from flask import Flask
from flask import redirect
from flask import render_template

from gpiozero import OutputDevice


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/unlock', methods=['POST'])
def unlock():
    buzzer = OutputDevice(17)
    buzzer.on()
    sleep(3)
    buzzer.off()   
    return redirect('/')

