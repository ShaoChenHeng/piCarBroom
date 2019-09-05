import RPi.GPIO as GPIO

#红外线接口
infraFront = 24
infraBack  = 23
#12前左侧 19前右侧
infraLeftSide = 12
infraRightSide = 19


#初始化红外线端口
def initInfra():
    GPIO.setup(infraFront, GPIO.IN)
    GPIO.setup(infraBack,  GPIO.IN)
    GPIO.setup(infraLeftSide, GPIO.IN) 
    GPIO.setup(infraRightSide, GPIO.IN) 
    

#获取红外输入
def InfraControl():
    vector = []
    inF = GPIO.input(infraFront)
    inB = GPIO.input(infraBack)
    inLS = GPIO.input(infraLeftSide)
    inRS = GPIO.input(infraRightSide) 
    vector.extend(str(inF))
    vector.extend(str(inB))
    vector.extend(str(inLS))
    vector.extend(str(inRS))
    for i in vector:
        print(i)

#initInfra()
#InfraControl()
