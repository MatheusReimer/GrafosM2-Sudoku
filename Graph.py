import imp
from enum import Enum
from posixpath import split
from xml.dom.minidom import Element

from matplotlib.style import use
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

    def createSegmentedMap(self):
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
            return x.Matrix4x4()
        elif self.size==9:
            return x.Matrix9x9()
        elif self.size==16:
            return x.Matrix16x16()                


    
    def createDegreeMap(self,segmentedMap):
        #Create first a list of indexes connected to each index
        print(segmentedMap)
        arrayGraph = segmentedMap
        for i in range(len(arrayGraph)):
            for j in range(len(arrayGraph)):
                currentConexions = []
                x = arrayGraph[i][:]
                #Remove current item
                xpop = [t for k,t in enumerate(x) if k!=j] 
                y = arrayGraph[:,j]
                ypop = [t for k,t in enumerate(y) if k!=i]

                print(ypop)
                for elem in ypop:
                    xpop.append(elem)
                #Check Diagonals for element in the same group

                
                #try:
                #    if(arrayGraph[i-1][j+1] == arrayGraph[i][j]):
                #        print("1-Deu boa",i,j) 
                #    if(arrayGraph[i-1][j-1]== arrayGraph[i][j]):
                #        print("2-Deu boa",i,j) 
                #    if(arrayGraph[i+1][j+1]== arrayGraph[i][j]):
                #        print("3-Deu boa",i,j) 
                #    if(arrayGraph[i+1][j-1]== arrayGraph[i][j]):
                #        print("4-Deu boa",i,j) 
                #except IndexError:
                #    print("Deu ruim")
                #currentConexions.append(xpop)


             


    def getStartingPoint(self):
        userInput = (-1,-1)
        while(userInput[0]>self.size or userInput[0]<=0 or userInput[1]>self.size or userInput[1]<=0):
            print("Qual sera o ponto inicial do grafo? Digite Linha ->Enter ->Coluna -> Enter")
            x = int(input())
            y = int(input())
            userInput = (x,y)
        
        return userInput

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