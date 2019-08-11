filePath = '/home/scheng/PYcode/algorithm/floodfill/map.txt'

class Array2D:
    def __init__(self, w, h, path):
        self.w = w 
        self.h = h
        self.path = path
        self.matrix = []
        #self.matrix = [[0 for y in range(h)] for x in range(w)]

    def showArray2D(self):
        for i in range(self.w):
            for j in range(self.h):
                print(self.matrix[i][j], end = ' ')
            print("")

    def inputFilePath(self):
        with open(self.path, 'r') as f:
            line = f.readline()      #readline()读取一行数据 
            while line:
                #split()分割字符串，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
                #map(function,ite),对ite进行function的操作。此处将当前行的数据按空格分割并转为int类型。
                data = list(map(int,line.split()))
                self.matrix.append(data)
                line = f.readline()
        f.close()
        #print(self.matrix)
        
    def  __getitem__(self , item):
        return self.matrix[item]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True

    def __str__(self):
        return "x:" + str(self.x) + "y:" + str(self.y)

class FloodFill:    
    def __init__( self, map2d, passTag = 0):
        self.map2d = map2d
        self.vector1 = [ 0, 0, -1, 1 ]
        self.vector2 = [ -1, 1, 0, 0]
        self.passTag = passTag
        self.cnt = 0

    def startDfs(self, x, y,cnt):
        #越界检测     
        if x < 0 or x > self.map2d.w - 1 or y < 0 or y > self.map2d.h - 1:
            return
        #障碍检测
        if self.map2d[x][y] != self.passTag:
            return
        self.map2d[x][y] = 2
        for i, j in zip(self.vector1,self.vector2):
                    self.startDfs(i+x,j+y,self.cnt);

    def main(self):      
        #找到不是障碍的一个点作为起点
        for i in range(self.map2d.h):
            for j in range(self.map2d.w):
                if self.map2d[i][j] == 0:
                    self.cnt += 1
                    self.startDfs(i,j,self.cnt)
                    ###aStack.push(self.currentPoint)
        print('here')
        print(self.cnt)

if __name__ == '__main__':
    map2d = Array2D(10,10,filePath)
    map2d.inputFilePath()
    map2d.showArray2D()
    floodfill = FloodFill(map2d)
    floodfill.main()
    print("-------------")
    map2d.showArray2D()
