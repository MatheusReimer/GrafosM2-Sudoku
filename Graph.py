import imp
from enum import Enum
from posixpath import split
from MatrixTypes import Matrix
import numpy as np
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3



class Graph(object):
    def __init__(self,size):
        self.size = int(size)
        self.vertices = size * size
        self.conexionList = list()


    def createGraph(self):
        arrayGraph = np.zeros([self.size,self.size])
        print(arrayGraph)
        return arrayGraph

    def createDegreeMap(self):
        #+2 to make the bounds
        sizeWithBounds = self.size+2
        #Its always going to have at least those connections
        currentConnection = self.size
        degreeArray = np.zeros([self.size,self.size])
        count = 0
        for i in range (len(degreeArray)):
            for j in range (len(degreeArray)):
                degreeArray[i][j] = count
                count = count +1 

        x = Matrix(degreeArray)
        if self.size==4:
            x.Matrix4x4()
        elif self.size==9:
            x.Matrix9x9()
        elif self.size==16:
            x.Matrix16x16()                

    def fillInGraph(self):
        print()

    def graphToDict(self):
        ##TURNS THE MATRIX OF 1 AND 0 INTO A DICTONARY OF THE INDEXES
        graph = {}
        for i in range(self.arr.shape[0]):
            graph[i]=[]
            for j in range(self.arr.shape[0]):
                if(self.arr[i][j]!=0):
                    graph[i].append(j)
        print(graph)
        return graph
    def helperFunction(self):
        arrayOfIndexes = []
        for i in range(self.arr.shape[0]):
            arrayOfIndexes.append(i)
        return arrayOfIndexes 

def printGraph(graph):
    print(graph)