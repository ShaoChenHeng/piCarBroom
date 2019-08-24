from car.infra.infraControl import *
from car.motor.motor_ctl import *
import tkinter as tk

def simpleGo():
    n = 20
    cal = 0

    while ( n > 0 ):

        inF = GPIO.input(infraFront)
        inL = GPIO.input(infraLeft)
        inB = GPIO.input(infraBack)
        inR = GPIO.input(infraRight)
        if ( inF == GPIO.LOW ):
            for i in range(0,12):
                CW()
                pause()
                time.sleep(0.1)
            n = n - 1    
            continue
        if ( inL == GPIO.LOW ):
            for i in range(0,5):
                CW()
                pause()
                time.sleep(0.2)
            n = n - 1
            continue
        if ( inR == GPIO.LOW ):
            for i in range(0,5):
                CCW()
                pause()
                time.sleep(0.2)
            n = n - 1
            continue
        if ( inL == GPIO.LOW & inR == GPIO.LOW):
            for i in range(0,20):
                back
                pause()
                time.sleep(0.1)
            for i in range(0,24):
                CW()
                pause()
                time.sleep(0.2)
            n = n - 1
            continue 
        up()
        pause()
        time.sleep(0.2)
      
