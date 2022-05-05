import math
from Graph import Graph, printGraph


def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2


def welcome():
    print("Bem vindo ao gerenciador de grafos:\n")
    size = 1
    while not is_square(size) or size<4 or size>16: 
        print("Qual sera o tamanho do seu sudoku? - defina quantidade de colunas")
        size = int(input())
    graph = Graph(size)

    return graph


def main():
    graph = welcome()
    graph.createGraph()
    segmentedMap = graph.createSegmentedMap()
    degreeMap = graph.createDegreeMap(segmentedMap)
    listOfRelations = graph.listRelations(degreeMap)
    print(listOfRelations)
    adjMatrix = graph.createAdjMatrix(listOfRelations)
    startingPoint = graph.getStartingPoint()
    colorGraph = graph.createColorGraph(startingPoint,adjMatrix,listOfRelations)


main()