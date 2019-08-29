import tkinter as tk
from car.infra.infraControl import *
from car.keyboard.keyboardInput import *
from car.motor.motor_ctl import *
from car.algorithm.algo import *
from car.getDistance.ver0 import *

#待添加
    #LED交互
    #提示音完善
    #电机通电开关
    #地图建立算法
    #路径规划主算法


def keyInput():
    keyPress = kbhit()
    if ( len(keyPress) > 0 ):
        print("pressed %s"%keyPress)

    if  keyPress == 'w':
        up()
    elif keyPress == 's':
        down()
    elif keyPress == 't':      #停止按钮
        pause()
    elif keyPress == 'e':
        turnRight1()
    elif keyPress == 'c':
        turnRight2()
    elif keyPress == 'q':
        turnLeft1()
    elif keyPress == 'z':
        turnLeft2()
    elif keyPress == 'a':
        CW()
    elif keyPress == 'd':
        CCW()
    elif keyPress == 'm':
        simpleGo()    
    elif keyPress == '\x1b':   #退出按钮
        GPIO.cleanup()
        exit()

init()
initInfra()
InfraControl()
while True:
    keyInput()

GPIO.cleanup()

