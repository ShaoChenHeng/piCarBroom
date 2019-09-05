#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os,sys
import signal
time.sleep(5) #开机后部分服务及应用可能未开启
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#define GPIO pin
pinBtn=16
pinLed=4
 
GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pinLed, GPIO.OUT, initial = GPIO.LOW)
 
pressTime = 0
countDown = 10
ledOn = 1

autoPinBtn = 21
press2Time = 0

GPIO.setup(autoPinBtn, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def cleanup():
    '''释放资源
    '''
    print('clean up...')
    GPIO.cleanup()
 
def handleSIGTERM(signum, frame):
    #cleanup()
    sys.exit()#raise an exception of type SystemExit
 
def onPress(channel):
    global pressTime,countDown
    print('pressed')
    pressTime += 1
    if pressTime > 3:
        pressTime = 1
    if pressTime == 1:
        GPIO.output(pinLed, 1)
        print('system will restart in %s'%(countDown))
    elif pressTime==2:
        print('system will halt in %s'%(countDown))
    elif pressTime==3:
        GPIO.output(pinLed, 0)
        print ('cancel ')
        countDown=10
 
def onPress2(channel):
    global press2Time
    print('press2 begin')
    press2Time += 1
    if press2Time > 3:
        press2Time = 1
    if press2Time == 1:
        print('begin auto work')
    elif press2Time == 2:
        print('auto work cancel')




#print("hello") 调试用
#在开机时文件所在目录为“/”，通过os.chdir()将位置转到提示音所在目录
#print(os.getcwd()) 调试用
#os.system("cd /home/pi/powerControl/")
#开机提示音
os.chdir("/home/pi/piCar")
os.system("sudo ./poweron")
from car.infra.infraControl import *
from car.keyboard.keyboardInput import *
from car.motor.motor_ctl import *
from car.algorithm.algover2 import *
from car.getDistance.ver0 import *
GPIO.add_event_detect(pinBtn, GPIO.FALLING, callback= onPress,bouncetime=500)
GPIO.add_event_detect(autoPinBtn, GPIO.FALLING, callback= onPress2,bouncetime=500)

init()
initInfra()
InfraControl()

def simpleGo():
    count = 0 # 一段路程内进行isStuck()检测
    # 没有按下 t 就一直自动驾驶
    global press2Time
    print('hello')
    while ( press2Time == 1 ):
        print('hello2')    
        checkStuck()
        checkBlock()
        up()
        print('upup')
        distAppend()
        pause()
        time.sleep(0.2)
        count += 1


#signal.signal(signal.SIGTERM, handleSIGTERM)
try:
    while True:
        if pressTime==1:
            if countDown == 1:
                os.system("sudo ./poweroff")
                time.sleep(8) #防止在提示音未放完就关机了
            if countDown==0:
                print ("start restart")
                os.system("sudo reboot")
                sys.exit()
            ledOn = not ledOn
            GPIO.output(pinLed, ledOn)# blink led
        
        if press2Time == 1:
            print('press2time1')
            os.system("sudo ./autooff")
            simpleGo()

        if press2Time == 2:
            os.system("sudo ./autoon")
            pause()

        if pressTime==2:
            if countDown == 1:
                os.system("sudo ./poweroff")
                time.sleep(8)
            if countDown <= 0:
                print("start shutdown")
                os.system("sudo poweroff")
                sys.exit()
 
        if pressTime == 1 or pressTime == 2:
            countDown -= 1
            print ("%s second"%(countDown))
        time.sleep(1)
        
except KeyboardInterrupt:
    print('User press Ctrl+c ,exit;')
finally:
    cleanup()

