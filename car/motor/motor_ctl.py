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
enableA = 20
enableB = 21

speed  = 25
GPIO.setup(enableA, GPIO.OUT)
GPIO.setup(enableB, GPIO.OUT)
motorA = GPIO.PWM(enableA,100)
motorB = GPIO.PWM(enableB,100)


def init(): 
    #初始化
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)  
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    motorA.start(0)
    motorB.start(0)
    
   
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
    time.sleep(0.1)
    motorA.ChangeDutyCycle(25)
    motorB.ChangeDutyCycle(25)
    pause()
    #GPIO.output(IN1,GPIO.LOW)

#顺时针旋转
def CW():
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    time.sleep(0.1)
    motorA.ChangeDutyCycle(25)
    motorB.ChangeDutyCycle(25)
    pause()

# 逆时针旋转
def CCW():
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(0.1)
    motorA.ChangeDutyCycle(25)
    motorB.ChangeDutyCycle(25)
    pause()

def down():
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN1, GPIO.HIGH)
    motorA.ChangeDutyCycle(25)
    motorB.ChangeDutyCycle(25)
    time.sleep(0.1)
    pause()

def turn_right1():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    motorA.ChangeDutyCycle(25)
    motorB.ChangeDutyCycle(25)    
    time.sleep(0.1)
    pause()

def turn_right2():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(0.1)
    pause()

def turn_left1():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    motorA.ChangeDutyCycle(25)
    motorB.ChangeDutyCycle(25)
    time.sleep(0.1)
    pause()

def turn_left2():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    motorA.ChangeDutyCycle(25)
    motorB.ChangeDutyCycle(25)
    time.sleep(0.1)
    pause()

def stop():
    print("Stoping")
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

