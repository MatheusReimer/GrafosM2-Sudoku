import imp
from enum import Enum
from itertools import accumulate
from posixpath import split
from turtle import color
from xml.dom.minidom import Element

from matplotlib.style import use
from MatrixTypes import Matrix
import numpy as np


#CRIAR UMA FUNCAO QUE CRIE UMA MATRIZ DE 1-16 E QUE COMPARANDO COM AS CONEXOES OBTIDAS NA FUNCAO CREATE SEGMENTED, PEGANDO AO INVES DOS INDICES, OS NUMEROS QUE CADA VERTICE FAZ CONEXAO COM. DEPOIS APLICAR NA MATRIZ VERTICES X VERTICES

class Color(Enum):
    YELLOW = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class Vertice(object):
        def __init__(self,number):
            self.colorsConnected = set()
            self.number = number

class Graph(object):
    def __init__(self,size):
        self.size = int(size)
        self.vertices = size * size
        self.connections = []

    def createGraph(self):
        arrayGraph = np.zeros([self.size,self.size])
        return arrayGraph

















    def createColorGraph(self,userInput,adjMatrix,listOfRelations,degreeMap):
        color = 0
        colorMatrix = np.zeros((self.size,self.size))
        colorMatrix[userInput[0]][userInput[1]] = color
        edgesRelations = listOfRelations
        accumulateGraph = self.createAccumulativeGraph()
        alreadyColored = []
        colorDegree = np.zeros((self.vertices))
        chosenNumber = int(accumulateGraph[userInput[0]][userInput[1]])
      
        alreadyColored.append(float(chosenNumber))
        arrayOfVertices = list()
        #numerando cada um dos vertices
        for i in range(self.vertices):
            vertice = Vertice(float(i))
            arrayOfVertices.append((vertice))
        print(edgesRelations[chosenNumber])
        for vertices in range(len(arrayOfVertices)):
            for item in edgesRelations[chosenNumber]:
                if(arrayOfVertices[vertices].number==item):
                    #ADDING COLOR TO ALL THE ITEMS THAT MAKE CONNECTION TO CHOSEN NUMBER
                    arrayOfVertices[vertices].colorsConnected.add(color)

        for allElements in range(self.vertices-1):

            index = 0
            maxDegree = 0      
            color = 0  
        
            ##GET NEXT ELEMENT
            for i in range(self.vertices):
                colorsConnected = arrayOfVertices[i].colorsConnected
                number = arrayOfVertices[i].number
                if(len(colorsConnected)>=maxDegree and  number not in alreadyColored):
                    maxDegree = len(colorsConnected)
                    index = number
            print("MAX DEGREEEEE", index)
            qty = arrayOfVertices[int(index)].colorsConnected
            for i in qty:
                while color== i:
                    color = color +1

            for vertices in range(len(arrayOfVertices)):
                for item in edgesRelations[int(index)]:
                    if(arrayOfVertices[vertices].number==item):
                        #ADDING COLOR TO ALL THE ITEMS THAT MAKE CONNECTION TO CHOSEN NUMBER
                        arrayOfVertices[vertices].colorsConnected.add(color)
            
            alreadyColored.append(index)
            i,j = np.where(accumulateGraph==index)
            colorMatrix[i[0]][j[0]] = color
        count = 0
        for all in arrayOfVertices:
            
            print(count," ",all.colorsConnected)
            count = count +1
        print(colorMatrix)

        #pegar proximo maxDegree

    




















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
        listOfList = list()
        for i in degreeMap:
            listOfConections = list()
            for j in i:
                x = j[0]
                y = j[1]
                listOfConections.append(matrixOfRelations[x][y])

            listOfList.append(listOfConections)
        for i in range(self.vertices):
            self.connections.insert(i,listOfList[i]) 
        return listOfList
    
    def createAdjMatrix(self,listOfRelations):
        matrixOfRelations = listOfRelations
        adjMatrix = np.zeros((self.vertices,self.vertices))
        for i in range(len(adjMatrix)):
            for j in range(len(matrixOfRelations[i])):
                adjMatrix[i][int(matrixOfRelations[i][j])] = 1
        return adjMatrix

    def createDegreeMap(self,segmentedMap):
        #Create first a list of indexes connected to each index
        arrayGraph = segmentedMap
        listOfTuplesList = []
        for i in range(len(arrayGraph)):
            for j in range(len(arrayGraph)):
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



    def createAccumulativeGraph(self):
        arr = np.zeros((self.size,self.size))
        count =0
        for i in range ((self.size)):
            for j in range ((self.size)):
                arr[i][j] = count
                count = count +1 
        return arr

    def getStartingPoint(self):
        userInput = (-1,-1)
        while(userInput[0]>self.size or userInput[0]<0 or userInput[1]>self.size or userInput[1]<0):
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
