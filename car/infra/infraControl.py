import RPi.GPIO as GPIO

#红外线接口
Infra_back = 23
Infra_left  = 5
Infra_front  = 24
Infra_right = 6

#初始化红外线端口
def init_infra():
    GPIO.setup(Infra_front, GPIO.IN)
    GPIO.setup(Infra_left, GPIO.IN)
    GPIO.setup(Infra_back, GPIO.IN)
    GPIO.setup(Infra_right, GPIO.IN)

#获取红外输入
def InfraControl():
    vector = []
    in_F = GPIO.input(Infra_front)
    in_L = GPIO.input(Infra_left)
    in_B = GPIO.input(Infra_back)
    in_R = GPIO.input(Infra_right)
    vector.extend(str(in_F))
    vector.extend(str(in_L))    
    vector.extend(str(in_B))
    vector.extend(str(in_R))
    for i in vector:
        print(i)

