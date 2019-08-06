import tkinter as tk
from car.motor.motor_ctl import *
from car.infra.infraControl import *
from car.algh import *


#待添加
    #LED交互
    #语音
    #树梅派开机关机按钮
    #电机通电开关

#路径规划主算法
def FloodFill():
    pass
 
#根据键盘输入使小车做出相应运动
#利用tkinter得到键盘输入
def key_input(event):
    print("pressed",repr(event.char))
    key_press = event.char
    print(key_press.lower())

    if key_press.lower() == 'w':
        up()
    elif key_press.lower() == 's':
        down()
    elif key_press.lower() == 't':      #停止按钮
        stop()
    elif key_press.lower() == 'e':
        turn_right1()
    elif key_press.lower() == 'c':
        turn_right2()
    elif key_press.lower() == 'q':
        turn_left1()
    elif key_press.lower() == 'z':
        turn_left2()
    elif key_press.lower() == 'a':
        CW()
    elif key_press.lower() == 'd':
        CCW()
    elif key_press.lower() == 'm':
        simpleGo()    
    elif key_press.lower() == '\x1b':   #退出按钮
        exit()

init()
init_infra()

command = tk.Tk()
command.bind('<KeyPress>',key_input)
InfraControl()
command.mainloop()

GPIO.cleanup()

