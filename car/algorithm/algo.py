from car.infra.infraControl import *
from car.motor.motor_ctl import *
from car.keyboard.keyboardInput import *
from car.getDistance.ver0 import *
import numpy as np

def isBackBlock():
    return GPIO.input(infraBack) == GPIO.LOW


def sendSignal():
    # 在机器无法自己驶出复杂地形的时候对外发送音乐寻求帮助
    pass

def isStuck():
    #超声波获取距离，根据距离变化(方差计算)判断小车是否正在移动。
    distArr = []
    total = 0
    for i in range(0,12):
        dist = distance()
        distArr.append(dist)
        time.sleep(0.2)
        total += dist
        if total >= 12000:
            #超声波碰壁会刷出2000+的距离，直接返回被挡
            return True
    #删除最大和最小值，防止意外波动
    del(distArr[distArr.index(max(distArr))])
    del(distArr[distArr.index(min(distArr))])
    #转为numpy数组便于进行方差计算
    npDist = np.array(distArr)
    Dx = np.var(npDist)
    #调试用
    for i in npDist:
        print( "The distance is {:.2f} cm".format(i) )

    #方差小于1可以认为是卡住了
    print("The Dx is %s"%Dx)
    distArr = [] 
    if ( Dx < 1 ):
        return True
    return False

def selctDirection():
    print("select a suitable direction...")
    vector = []
    inF = GPIO.input(infraFront)
    inB = GPIO.input(infraBack)
    inLS = GPIO.input(infraLeftSide)
    inRS = GPIO.input(infraRightSide) 
    vector.extend(str(inF))
    vector.extend(str(inRS))
    vector.extend(str(inB))
    vector.extend(str(inLS))
    
    print("-------------------")
    for i in vector:
        print(i)
        print(vector.index(i))
    print("-------------------")
    for i in vector:
        # 返回一个没有被阻挡的下标
        if i == '1':
            print(vector.index(i))
            return vector.index(i)
    
    #四周都有阻挡就准备进行随机碰撞
    return 10000

def escape(esCount):
    print("try %s escape"%esCount)
    #count记录随即碰撞次数
    #观察红外线四个方向，选一个没有阻挡的地方往外走
    direction = selctDirection()
    # 完全被挡住了，随即碰撞找出路
    print("here")
    print("direction is %s"%direction)

    if direction ==  10000:
        print("start random escape...")
        while ( esCount < 10 or isStuck() ):
            for i in range(0,3):
                down()
            for i in range(0,3):
                CCW()
            for i in range(0,3):
                up()
            esCount += 1
    else:
        print("start a dull escape...")
        for i in range( 0, direction * 2 ):
            CW()
        for i in range(0,3):
            up()
        pause()
        print("here!!!")
        if isStuck():
            print("oh!!")
            esCount += 1
            escape(escape)


def checkStuck(stCnt):
    #检验三次是否卡住
    if stCnt >= 3:
        #多次检验后发现的确卡住了，就设法逃离复杂地形
        print("oh stuck!")
        escape(0)
    elif isStuck() == True:
        print("checkStuck! %s"%stCnt)
        stCnt += 1
        checkStuck(stCnt)
    


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
                return isBlock(cnt)

def simpleGo():
    cnt = 0   # 记录卡住次数，来辨别是否卡死
    count = 0 # 一段路程内进行isStuck()检测
    keyPress = ''
    # 没有按下 t 就一直自动驾驶
    while ( keyPress != 't'):
        keyPress = kbhit()
        
        if ( count >= 25 ):
            #待添加escape()失败后的解决方案
            checkStuck(0)
            count = 0
        isBlock(cnt)
        isSideBlock(infraFront, 0)
        isSideBlock(infraLeftSide, 0)
        isSideBlock(infraRightSide, 0)
        up()
        pause()
        time.sleep(0.2)
        count += 1
