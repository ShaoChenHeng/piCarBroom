import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leftCrush = 6
rightCrush = 5

def initCrush():
    GPIO.setup(leftCrush, GPIO.IN)
    GPIO.setup(rightCrush, GPIO.IN)

initCrush()
