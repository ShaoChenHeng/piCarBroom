import numpy as np

filePath = '/home/scheng/PYcode/algorithm/a*/map.txt'
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

class AStar:

    class Node:
        def __init__( self, point, endPoint, g = 0 ):
            self.point = point
            self.father = None
            self.g = g
            self.h = ( abs( endPoint.x - point.x ) + abs( endPoint.y - point.y ) ) * 10
    
    def __init__(self, map2d, startPoint, endPoint, passTag = 0):
        """
        构造AStar算法的启动条件
        :param map2d: Array2D类型的寻路数组
        :param startPoint: Point或二元组类型的寻路起点
        :param endPoint: Point或二元组类型的寻路终点
        :param passTag: int类型的可行走标记（若地图数据!=passTag即为障碍）
        """
        self.openList = []
        self.closeList = []
        self.map2d = map2d
        #设置起点和终点
        if isinstance( startPoint, Point ) and isinstance( endPoint, Point ):
            self.startPoint = startPoint
            self.endPoint = endPoint
        else:
            self.startPoint = Point(*startPoint)
            self.endPoint = Point(*endPoint)
            
        self.passTag = passTag
    
    def getMinNode(self):
        currentNode = self.openList[0]
        for node in self.openList:
            if node.g + node.h < currentNode.g + currentNode.h:
                currentNode = node
        return currentNode

    def pointInOpenList(self, point):
        for node in self.openList:
            if node.point == point:
                return node
        return None


    def pointInCloseList(self, point):
        for node in self.closeList:
            if node.point == point:
                return node
        return None

    def endPointInCloseList(self):
        for node in self.openList:
            if node.point == self.endPoint:
                return node
        return None
        
    def searchNear( self, minF, offsetX, offsetY ):
        """
        搜索节点周围的点
        :param minF:F值最小的节点
        :param offsetX:坐标偏移量
        :param offsetY:
        :return:
        """

        #越界检测
        if minF.point.x + offsetX < 0 or minF.point.x + offsetX > self.map2d.w - 1 or minF.point.y + offsetY < 0 or minF.point.y + offsetY > self.map2d.h - 1:
            return

        #障碍检测
        if self.map2d[minF.point.x + offsetX][minF.point.y + offsetY] != self.passTag:
            return

        #如果在关闭列表中就忽略
        currentPoint = Point(minF.point.x + offsetX, minF.point.y + offsetY)
        if self.pointInCloseList(currentPoint):
            return
        
        # 设置单位花费
        if offsetX == 0 or offsetY == 0:
            step = 10
        else:
            step = 14
        # 如果不再openList中，就把它加入openlist
        currentNode = self.pointInOpenList(currentPoint)
        if not currentNode:
            currentNode = AStar.Node(currentPoint, self.endPoint, g=minF.g + step)
            currentNode.father = minF
            self.openList.append(currentNode)
            return
        # 如果在openList中，判断minF到当前点的G是否更小
        if minF.g + step < currentNode.g:  # 如果更小，就重新计算g值，并且改变father
            currentNode.g = minF.g + step
            currentNode.father = minF

    def start(self):
        if self.map2d[self.endPoint.x][self.endPoint.y] != self.passTag:
            return None
        #将起点放入开启列表
        startNode = AStar.Node(self.startPoint, self.endPoint)
        self.openList.append(startNode)

        while True:
            minF = self.getMinNode()
            self.closeList.append(minF)
            self.openList.remove(minF)
            # 判断这个节点的上下左右节点
            self.searchNear(minF, 0, -1)
            self.searchNear(minF, 0, 1)
            self.searchNear(minF, -1, 0)
            self.searchNear(minF, 1, 0)
            point = self.endPointInCloseList()
            if point:
                cPoint = point
                pathList = []
                while True:
                    if cPoint.father:
                        pathList.append(cPoint.point)
                        cPoint = cPoint.father
                    else:
                        return list(reversed(pathList))
            if len(self.openList) == 0:
                return None



if __name__ == '__main__':
    map2d = Array2D(10,10,filePath)
    map2d.inputFilePath()
    map2d.showArray2D()
    #创建AStar对象,设置起点与终点
    aStar = AStar(map2d,Point(2,0),Point(3,6))
    pathList = aStar.start()
    for point in pathList:
        map2d[point.x][point.y] = 8
    print("-------------")
    map2d.showArray2D()
