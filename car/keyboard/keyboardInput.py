import tkinter as tk
from car.algorithm.algo import *
from car.motor.motor_ctl import *
 
#根据键盘输入使小车做出相应运动
#利用tkinter得到键盘输入
def keyInput(event):
    print("pressed",repr(event.char))
    keyPress = event.char
    print(keyPress.lower())

    if keyPress.lower() == 'w':
        up()
    elif keyPress.lower() == 's':
        down()
    elif keyPress.lower() == 't':      #停止按钮
        stop()
    elif keyPress.lower() == 'e':
        turnRight1()
    elif keyPress.lower() == 'c':
        turnRight2()
    elif keyPress.lower() == 'q':
        turnLeft1()
    elif keyPress.lower() == 'z':
        turnLeft2()
    elif keyPress.lower() == 'a':
        CW()
    elif keyPress.lower() == 'd':
        CCW()
    elif keyPress.lower() == 'm':
        simpleGo()    
    elif keyPress.lower() == '\x1b':   #退出按钮
        exit()
