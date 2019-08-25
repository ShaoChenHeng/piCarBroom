import tkinter as tk
import select
import sys
import time
import os
import termios
from car.motor.motor_ctl import *
# 别说理解程序了，注释我都理解不了。 代码网上找的。
# 功能是实现非阻塞输入，kbhit()功能类似 windows下c的kbhit()


def kbhit():
    # 获取标准输入的描述符
    fd = sys.stdin.fileno()
    r = select.select([sys.stdin],[],[],0.01)
    rcode = ''
    if len(r[0]) >0:
        rcode  = sys.stdin.read(1)
    return rcode

def inputInit():
    fd = sys.stdin.fileno()
    # 获取标准输入(终端)的设置
    old_settings = termios.tcgetattr(fd)
    new_settings = old_settings
    #new_settings[3] = new_settings[3] & ~termios.ISIG
    new_settings[3] = new_settings[3] & ~termios.ICANON
    new_settings[3] = new_settings[3] & ~termios.ECHONL
    # print ('old setting %s'%(repr(old_settings)))
    termios.tcsetattr(fd,termios.TCSAFLUSH,new_settings)



inputInit()
