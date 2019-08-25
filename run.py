import tkinter as tk
from car.infra.infraControl import *
from car.keyboard.keyboardInput import *

#待添加
    #LED交互
    #提示音完善
    #电机通电开关
    #地图建立算法
    #路径规划主算法

init()
initInfra()

command = tk.Tk()
command.bind('<KeyPress>',keyInput)
InfraControl()
command.mainloop()

GPIO.cleanup()

