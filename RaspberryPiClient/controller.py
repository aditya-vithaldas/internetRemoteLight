import  RPi.GPIO as GPIO
import requests

GPIO.setwarnings(False)

ledPin = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

while 1:
    command  = requests.get("http://internetRemote.adityavithaldas.repl.co/getcontrol").text
    if command == "start":
        GPIO.output(ledPin, GPIO.HIGH)
    elif command == "stop":
        GPIO.output(ledPin, GPIO.LOW)