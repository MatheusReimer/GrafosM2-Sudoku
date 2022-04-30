import imp
from enum import Enum
from posixpath import split
from xml.dom.minidom import Element

from matplotlib.style import use
from MatrixTypes import Matrix
import numpy as np


#CRIAR UMA FUNCAO QUE CRIE UMA MATRIZ DE 1-16 E QUE COMPARANDO COM AS CONEXOES OBTIDAS NA FUNCAO CREATE SEGMENTED, PEGANDO AO INVES DOS INDICES, OS NUMEROS QUE CADA VERTICE FAZ CONEXAO COM. DEPOIS APLICAR NA MATRIZ VERTICES X VERTICES

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

    def listRelations(self,degreeMap):
        matrixOfRelations = np.zeros((self.size,self.size))
        count  =0
        for i in range(len(matrixOfRelations)):
            for j in range(len(matrixOfRelations)):
                matrixOfRelations[i][j] = count
                count = count +1
        shape = (np.shape(degreeMap))

        listOfList = list()
        for i in range(shape[0]):
            listOfConections = list()
            for j in range(shape[1]):
                listOfConections.append(matrixOfRelations[degreeMap[i][j][0]][degreeMap[i][j][1]])

            listOfList.append(listOfConections)
        return listOfList
    
    def createAdjMatrix(self,listOfRelations):
        matrixOfRelations = listOfRelations
        adjMatrix = np.zeros((self.vertices,self.vertices))
        for i in range(len(adjMatrix)):
            for j in range(len(matrixOfRelations[i])):
                adjMatrix[i][int(matrixOfRelations[i][j])] = 1

        print(adjMatrix)
    def createDegreeMap(self,segmentedMap):
        #Create first a list of indexes connected to each index
        print(segmentedMap)
        arrayGraph = segmentedMap
        listOfTuplesList = list()
        for i in range(len(arrayGraph)):
            for j in range(len(arrayGraph)):
                currentConexions  = [[0]*len(arrayGraph) for u in range(len(arrayGraph))]
                x = arrayGraph[i][:]
                #Remove current item
                xpop = [t for t,x in enumerate(x) if t!=j]
                y = arrayGraph[:,j]
                ypop = [t for t,x in enumerate(y) if t!=i]

                ################ x  x  x  y  y  y
                #xpop example = [1, 2, 3, 1, 2, 3]
                listOfTuples = list()
                for z in xpop:
                    xtuple = (i,z)
                    #print(xtuple)
                    listOfTuples.append(xtuple)
                for z in ypop:
                    ytuple = (z,j)
                    #print(ytuple)
                    listOfTuples.append(ytuple)
                #Check Diagonals for element in the same group
                
                if(i<(len(arrayGraph)-1) and j>0 and arrayGraph[i+1][j-1] == arrayGraph[i][j] ):
                    tuplet = (i+1,j-1)
                    listOfTuples.append(tuplet)
                                    
                if(j<(len(arrayGraph)-1) and i>0 and arrayGraph[i-1][j+1] == arrayGraph[i][j] ):
                    tuplet = (i-1,j+1)
                    listOfTuples.append(tuplet)
                if(i>0 and j>0 and arrayGraph[i-1][j-1]==arrayGraph[i][j]):
                    tuplet = (i-1,j-1)
                    listOfTuples.append(tuplet)
                if(i<len(arrayGraph)-1 and j<len(arrayGraph)-1 and arrayGraph[i+1][j+1] == arrayGraph[i][j]):
                    tuplet = (i+1,j+1)
                    listOfTuples.append(tuplet)                         
                listOfTuplesList.append(listOfTuples)
        return listOfTuplesList

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
