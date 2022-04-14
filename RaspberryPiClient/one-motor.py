import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
speed = 20
GPIO.setwarnings(False)
Ena, In1, In2 = 2,3,4
Enb, In3, In4 = 14,15,18

GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)
pwm = GPIO.PWM(Ena, 100)
pwm.start(0)

GPIO.setup(Enb, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)
pwm2 = GPIO.PWM(Enb, 10)
pwm2.start(0)


if True:
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)

    GPIO.output(In3, GPIO.HIGH)
    GPIO.output(In4, GPIO.LOW)
    pwm2.ChangeDutyCycle(speed)
    sleep(2)
    
    
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)
    
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.HIGH)
    pwm2.ChangeDutyCycle(speed)
    
    sleep(2)
    
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.LOW)
    pwm.ChangeDutyCycle(0)
    