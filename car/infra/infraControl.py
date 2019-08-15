import RPi.GPIO as GPIO

#红外线接口
infraFront = 24
infraBack  = 23
infraLeft  = 5
infraRight = 6
#12前左侧 19前右侧
infraLeftSide = 12
infraRightSide = 19


#初始化红外线端口
def initInfra():
    GPIO.setup(infraFront, GPIO.IN)
    GPIO.setup(infraLeft,  GPIO.IN)
    GPIO.setup(infraBack,  GPIO.IN)
    GPIO.setup(infraRight, GPIO.IN)
    GPIO.setup(infraLeftSide, GPIO.IN) 
    GPIO.setup(infraRightSide, GPIO.IN) 
    

#获取红外输入
def InfraControl():
    vector = []
    inF = GPIO.input(infraFront)
    inL = GPIO.input(infraLeft)
    inB = GPIO.input(infraBack)
    inR = GPIO.input(infraRight)
    inLS = GPIO.input(infraLeftSide)
    inRS = GPIO.input(infraRightSide) 
    vector.extend(str(inF))
    vector.extend(str(inL))    
    vector.extend(str(inB))
    vector.extend(str(inR))
    vector.extend(str(inLS))
    vector.extend(str(inRS))
    for i in vector:
        print(i)

#initInfra()
#InfraControl
