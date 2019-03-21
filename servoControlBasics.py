import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm = GPIO.PWM(11,50)

pwm.start(10)
time.sleep(0.25)
pwm.ChangeDutyCycle(7.5)
time.sleep(0.25)
pwm.ChangeDutyCycle(10)
time.sleep(0.25)
pwm.ChangeDutyCycle(2)
time.sleep(0.25)
pwm.ChangeDutyCycle(12)
time.sleep(0.25)

pwm.stop()

GPIO.cleanup()