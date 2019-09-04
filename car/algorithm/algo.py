from car.infra.infraControl import *
from car.motor.motor_ctl import *
from car.keyboard.keyboardInput import *
from car.getDistance.ver0 import *
import numpy as np

distArr = []
total = 0
#考虑到使用多进程测距再计算会造成多次测距的重复问题，每一次移动后测距并添加到列表

def isBackBlock():
    return GPIO.input(infraBack) == GPIO.LOW


def sendSignal():
    # 在机器无法自己驶出复杂地形的时候对外发送音乐寻求帮助
    pass

def confirmStuck():
    #确认是否真的堵住，由于递归isStuck()会造成距离列表读取写入混乱，并且影响行进，所以再开一个确认函数
    #因为存在堵住的嫌疑，所以前进一步再获取距离
    confirmList = []
    total = 0
    for i in range(0,12):
        up()
        dist = distance()
        confirmList.append(dist)
        total += dist
        if total > 12000:
            #超声波装置碰壁会刷出2000+的距离，直接返回被挡
            confirmList = []    
            return True
    #删除最大和最小值，防止意外波动
    del(confirmList[confirmList.index(max(confirmList))])
    del(confirmList[confirmList.index(min(confirmList))])
    #转为numpy数组便于进行方差计算
    npDist = np.array(confirmList)
    Dx = np.var(npDist)
    
    #调试用
    print("-------------------")
    print('confirm data')
    for i in npDist:
        print( "The distance is {:.2f} cm".format(i) )
    print("-------------------")

    #方差小于3可以认为是卡住了
    print("The Dx is %s"%Dx)
    distArr = [] 
    if ( Dx < 3 ):
        return True
    return False

def distAppend():
    global distArr
    global total
    dist = distance()
    total += dist
    distArr.append(dist)
    # 调试用
    #print"The distance is {:.2f} cm".format(dist))

def isStuck():
    #超声波获取距离，根据距离变化(方差计算)判断小车是否正在移动。
    global distArr
    global total
    print('here')
    # 数据太少
    if len(distArr) < 12:
        return False
    print('here!!')

    #超声波装置碰壁会刷出2000+的距离，直接返回被挡
    if total >= 12000:
        distArr = []     
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

    #方差小于3可以认为是卡住了
    print("The Dx is %s"%Dx)
    distArr = [] 
    if ( Dx < 3 ):
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
        if vector.index(i) == 0:
            # 因为前方使被挡住的（红外线被黑色吸收所以会是LOW，或者因为高度差）
            continue
        if i == '1':
            print('direction is',vector.index(i))
            return vector.index(i)
    
    #四周都有阻挡就准备进行随机碰撞
    return 10000

def escape(esCount):
    if esCount >= 10:
        # 完全卡死了，只能向人类发送信号
        sendSignal()
    print("try %s escape"%esCount)
    #count记录随即碰撞次数
    #观察红外线四个方向，选一个没有阻挡的地方往外走
    direction = selctDirection()
    # 完全被挡住了，随机碰撞找出路
    print("here")
    print("direction is %s"%direction)
    ite = 0
    if direction ==  10000:
        print("start random escape...")
        #2000是超声装置被挡住的返回值，5以下也可以认为使前方仍有障碍
        while ( ite == 0 or distance() > 2000 or distance() < 5 ):
            for i in range(0,3):
                down()
            for i in range(0,3):
                CCW()
            for i in range(0,3):
                up()
            ite += 1
            esCount += 1
            escape(esCount)
    else:
        print("start a dull escape...")
        for i in range( 0, direction * 2 ):
            CW()
        for i in range(0,3):
            up()
        pause()
        print("here!!!")
        if ( ite == 0 or distance() > 2000 or distance() < 5 ):
            print("remain stuck!")
            ite += 1
            esCount += 1
            escape(esCount)


def checkStuck():
    #检验三次是否卡住
    cnt = 0
    if isStuck() == True:
        print('may stuck')
        for i in range(0,2):
            #进行确认是否真的卡住
            if confirmStuck() == True:
                cnt += 1
        if cnt >= 1:
            print('oh stuck')
            escape(0) 


def isSideBlock(num,cnt):
    ans = GPIO.input(num)

    if cnt >= 3:
        #卡住了，前后无路
        return
    if ( ans == GPIO.LOW ):
        #默认设置正前方和左侧方遮挡顺时针旋转
        print('sideBlock',cnt)
        print('num is ',num)
        if num == infraRightSide:
            for i in range(0,2):
                CCW()
        else:
            for i in range(0,2):
                CW()
        distAppend()       
        pause()
        # 检查是否卡死
        if isBackBlock():
            pause()
            time.sleep(1)
            cnt += 1
        else:
            down()
        distAppend()        
        pause()
        time.sleep(0.2)
        return isSideBlock(num, cnt)

def isBlock(cnt):
     if ( (infraLeft == GPIO.LOW and infraRight == GPIO.LOW ) or (infraLeftSide == GPIO.LOW and infraRightSide == GPIO.LOW) ):
        #左右两侧被挡，就先后退
        print("block!",cnt)
        
        for i in range(0,2):
           down()
        pause()
        distAppend()
        if cnt < 2:
            cnt += 1
            return isBlock( cnt )
        else:
            cnt = 0
            for i in range(0,3):
                CW()
            distAppend()
            return isBlock(cnt)

def simpleGo():
    cnt = 0   # 记录卡住次数，来辨别是否卡死
    count = 0 # 一段路程内进行isStuck()检测
    keyPress = ''
    # 没有按下 t 就一直自动驾驶
    while ( keyPress != 't'):
        keyPress = kbhit()
        checkStuck()
        isBlock(cnt)
        isSideBlock(infraFront, 0)
        isSideBlock(infraLeftSide, 0)
        isSideBlock(infraRightSide, 0)
        up()
        print('upup')
        distAppend()
        pause()
        time.sleep(0.2)
        count += 1
