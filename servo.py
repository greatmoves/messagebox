import RPi.GPIO as GPIO
import time

def move():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(13, GPIO.OUT)
    servo1 = GPIO.PWM(13, 50)

    servo1.start(0)
    for i in range(9):
        servo1.ChangeDutyCycle(5)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(10)
        time.sleep(0.5)
        #servo1.ChangeDutyCycle(12.5)
    #time.sleep(0.5)
    servo1.ChangeDutyCycle(5)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(10)
    servo1.stop()
    GPIO.cleanup()