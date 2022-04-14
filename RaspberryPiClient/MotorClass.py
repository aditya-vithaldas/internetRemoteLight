import RPi.GPIO as GPIO
from time import sleep
import requests


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

class MotorClass:
    
    def __init__(self, Ena, In1, In2, In3, In4, Enb):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        self.Enb = Enb
        self.In3 = In3
        self.In4 = In4
        self.speed = 20
        
        GPIO.setup(Ena, GPIO.OUT)
        GPIO.setup(In1, GPIO.OUT)
        GPIO.setup(In2, GPIO.OUT)
        GPIO.setup(Enb, GPIO.OUT)
        GPIO.setup(In3, GPIO.OUT)
        GPIO.setup(In4, GPIO.OUT)
        self.pwm = GPIO.PWM(Ena, 100)
        self.pwm.start(0)
    
        self.pwm2 = GPIO.PWM(Enb, 100)
        self.pwm2.start(0)
        
    def stop(self):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.In3, GPIO.LOW)
        GPIO.output(self.In4, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
        
    def forward(self):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(self.speed)

        GPIO.output(self.In3, GPIO.HIGH)
        GPIO.output(self.In4, GPIO.LOW)
        self.pwm2.ChangeDutyCycle(self.speed)
        
    def back(self):
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(self.speed)
        
        GPIO.output(self.In3, GPIO.LOW)
        GPIO.output(self.In4, GPIO.HIGH)
        self.pwm2.ChangeDutyCycle(self.speed)
        
    def left(self):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(self.speed)

        GPIO.output(self.In3, GPIO.HIGH)
        GPIO.output(self.In4, GPIO.LOW)
        self.pwm2.ChangeDutyCycle(self.speed-10)
        
    
    def right(self):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(self.speed-10)

        GPIO.output(self.In3, GPIO.HIGH)
        GPIO.output(self.In4, GPIO.LOW)
        self.pwm2.ChangeDutyCycle(self.speed)