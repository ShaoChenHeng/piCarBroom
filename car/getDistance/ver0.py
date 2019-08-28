import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
trigger = 25
echo = 26
  
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
  
def distance():
    # 发送高电平信号到 Trig 引脚
    GPIO.output(trigger, True) 
    # 持续 10 us 
    time.sleep(0.00001)
    GPIO.output(trigger, False)
  
    # time.time()返回当前时间
    starTime = time.time()
    stopTime = time.time()
  
    # 记录发送超声波的时刻1
    while GPIO.input(echo) == 0:
        startTime = time.time()
  
    # 记录接收到返回超声波的时刻2
    while GPIO.input(echo) == 1:
        stopTime = time.time()
  
    # 计算超声波的往返时间 = 时刻2 - 时刻1
    timeElapsed = stopTime - startTime
    # 声波的速度为 343m/s， 转化为 34300cm/s。
    distance = (timeElapsed * 34300) / 2
    return distance

def showDistance():
    try:
        while True:
            dist = distance()
            print("Measured Distance = {:.2f} cm".format(dist))
            time.sleep(1)
  
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()


if __name__ == '__main__':
    showDistance()    

