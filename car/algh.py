from car.infra.infraControl import *
from car.motor.motor_ctl import *


def simpleGo():
    n = 20
    cal = 0
    while ( n > 0 ):
        in_F = GPIO.input(Infra_front)
        in_L = GPIO.input(Infra_left)
        in_B = GPIO.input(Infra_back)
        in_R = GPIO.input(Infra_right)
        if ( in_F == GPIO.LOW ):
            for i in range(0,12):
                CW()
                pause()
                time.sleep(0.1)
            n = n - 1    
            continue
        if ( in_L == GPIO.LOW ):
            for i in range(0,5):
                CW()
                pause()
                time.sleep(0.2)
            n = n - 1
            continue
        if ( in_R == GPIO.LOW ):
            for i in range(0,5):
                CCW()
                pause()
                time.sleep(0.2)
            n = n - 1
            continue
        if ( in_L == GPIO.LOW & in_R == GPIO.LOW):
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
      
