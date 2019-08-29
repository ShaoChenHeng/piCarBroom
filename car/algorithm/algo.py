from car.infra.infraControl import *
from car.motor.motor_ctl import *
from car.keyboard.keyboardInput import *
from car.getDistance.ver0 import *

def isBackBlock():
    return GPIO.input(infraBack) == GPIO.LOW

def is

def isSideBlock(num,cnt):
    ans = GPIO.input(num)
    if cnt >= 3:
        #卡住了，前后无路
        return
    if (ans == GPIO.LOW):
        #默认设置正前方和左侧方遮挡顺时针旋转
        if num == infraRightSide:
            for i in range(0,2):
                CCW()
        else:
            for i in range(0,2):
                CW()
        pause()
        # 检查是否卡死
        if isBackBlock():
            pause()
            time.sleep(1)
            cnt += 1
        else:
            down()
        pause()
        time.sleep(0.2)
        return isSideBlock(num, cnt)

def isBlock(cnt):
    if ( (infraLeft == GPIO.LOW and infraRight == GPIO.LOW ) or (infraLeftSide == GPIO.LOW and infraRightSide == GPIO.LOW) ):
        for i in range(0,2):
           down()
        pause()
        if cnt < 3:
            cnt += 1
            return isBlock( cnt )
        else:
            cnt = 0
            for i in range(0,3):
                CW()
                return isBlock( cnt )

def simpleGo():
    cnt = 0
    keyPress = ''
    # 没有按下 t 就一直自动驾驶
    while ( keyPress != 't'):
        keyPress = kbhit()
        isBlock(cnt)
        isSideBlock(infraFront, 0)
        isSideBlock(infraLeftSide, 0)
        isSideBlock(infraRightSide, 0)
        up()
        pause()
        time.sleep(0.2)
