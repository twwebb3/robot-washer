import time
import RPi.GPIO as GPIO
import numpy as np
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

base = GPIO.PWM(11, 50)
base.start(0)

try:
    while 1:
            base.ChangeDutyCycle(3)
            time.sleep(0.25)
            base.ChangeDutyCycle(7.5)
            time.sleep(0.25)
            base.ChangeDutyCycle(12)
            time.sleep(0.25)
            base.ChangeDutyCycle(7.5)
            time.sleep(0.25)
        
except KeyboardInterrupt:
    pass
base.stop()
GPIO.cleanup()