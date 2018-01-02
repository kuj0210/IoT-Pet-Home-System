import RPi.GPIO as GPIO
import time

def water():
    pin = 12 # PWM pin num 32

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin, 50)
    p.start(0)
    try:
        p.ChangeDutyCycle(18)
        time.sleep(1)
        p.ChangeDutyCycle(7)
        time.sleep(5)
        p.ChangeDutyCycle(1)
        time.sleep(4)
        p.stop()
    except KeyboardInterrupt:
        p.stop()
    GPIO.cleanup()

def prey():
    pin = 19 # PWM pin num 35

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin, 50)
    p.start(0)
    try:
        p.ChangeDutyCycle(6)
        time.sleep(1)
        p.ChangeDutyCycle(3)
        time.sleep(0.5)
        p.stop()
    except KeyboardInterrupt:
        p.stop()
    GPIO.cleanup()

def door():
    pin = 18 # PWM pin num 12

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin, 50)
    p.start(0)
    try:
        p.ChangeDutyCycle(18)
        time.sleep(6)
        p.stop()
    except KeyboardInterrupt:
        p.stop()
    GPIO.cleanup()
