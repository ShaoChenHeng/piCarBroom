import RPi.GPIO as GPIO
import time 
import sys


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#电机接口
IN1 = 17 #leftside  -
IN2 = 18 #leftside  +
IN3 = 27 #rightside -
IN4 = 22 #rightside +

#使能接口
enable = 20
speed  = 25
GPIO.setup(enable, GPIO.OUT)
motor = GPIO.PWM(enable,100)


def init(): 
    #初始化
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)  
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    motor.start(0)
    
   
def pause():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

#四个转向以及向前向后行进的控制
def up(): 
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    motor.ChangeDutyCycle(40)
    time.sleep(0.1)
    pause()
    #GPIO.output(IN1,GPIO.LOW)

#顺时针旋转
def CW():
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    time.sleep(0.1)
    motor.ChangeDutyCycle(40) #转速根据小车载重决定
    pause()

# 逆时针旋转
def CCW():
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(0.1)
    motor.ChangeDutyCycle(40)
    pause()

def down():
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN1, GPIO.HIGH)
    motor.ChangeDutyCycle(55)
    time.sleep(0.2)
    pause()

def turnRight1():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    motor.ChangeDutyCycle(35)
    time.sleep(0.1)
    pause()

def turnRight2():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    motor.ChangeDutyCycle(35)
    time.sleep(0.1)
    pause()

def turnLeft1():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    motor.ChangeDutyCycle(35)
    time.sleep(0.1)
    pause()

def turnLeft2():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    motor.ChangeDutyCycle(35)
    time.sleep(0.1)
    pause()

def stop():
    print("Stoping")
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

