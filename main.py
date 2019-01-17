import utils
import numpy as np
import copy

shapeIDs = {
    1: [set(y for y in{(0,0),(0,1),(1,0),(1,1)}),set(y for y in {(0,0),(0,1),(-1,0),(-1,1)})],
    3: [set(y for y in {(0,0),(0,1),(0,2),(0,3)})],
    2: [set(y for y in {(0,0),(1,0),(2,0),(3,0)}),set(y for y in {(-1,0),(0,0),(1,0),(2,0)}),set(y for y in {(-2,0),(-1,0),(0,0),(1,0)}),set(y for y in {(-3,0),(-2,0),(-1,0),(0,0)})],
    4: [set(y for y in {(0,0),(1,0),(2,0),(2,1)}),set(y for y in {(-1,0),(0,0),(1,0),(1,1)}),set(y for y in {(-2,0),(-1,0),(0,0),(1,1)})],
    5: [set(y for y in {(0,0),(0,1),(0,2),(-1,2)})],
    6: [set(y for y in {(0,0),(0,1),(1,1),(2,1)})],
    7: [set(y for y in {(0,0),(1,0),(0,1),(0,2)}),set(y for y in {(0,0),(-1,0),(-1,1),(-1,2)})],
    8: [set(y for y in {(0,0),(0,1),(-1,1),(-2,1)})],
    9: [set(y for y in {(0,0),(0,1),(0,2),(1,2)})],
    10: [set(y for y in {(0,0),(1,0),(2,0),(0,1)}),set(y for y in {(-1,0),(0,0),(1,0),(-1,1)}),set(y for y in {(-2,0),(-1,0),(0,0),(-2,1)})],
    11: [set(y for y in {(0,0),(-1,0),(0,1),(0,2)}),set(y for y in {(0,0),(1,0),(1,1),(1,2)})],
    12: [set(y for y in {(0,0),(1,0),(2,0),(1,1)}),set(y for y in {(-1,0),(0,0),(1,0),(0,1)}),set(y for y in {(-2,0),(-1,0),(0,0),(-1,1)})],
    13: [set(y for y in {(0,0),(0,1),(0,2),(-1,1)})],
    14: [set(y for y in {(0,0),(0,1),(1,1),(-1,1)})],
    15: [set(y for y in {(0,0),(0,1),(0,2),(1,1)})],
    16: [set(y for y in {(0,0),(0,1),(-1,1),(-1,2)})],
    17: [set(y for y in {(0,0),(-1,0),(0,1),(1,1)}),set(y for y in {(0,0),(1,0),(1,1),(2,1)})],
    18: [set(y for y in {(0,0),(0,1),(1,1),(1,2)})],
    19: [set(y for y in {(0,0),(1,0),(0,1),(-1,1)}),set(y for y in {(0,0),(-1,0),(-1,1),(-2,1)})]
    }
        
def FindNextElementInShape(AdjacencyList, element,listOfPositions,listOfPlacedElements, labeledTarget):
    numberOfRows = len(labeledTarget)
    numberOfColumns = len(labeledTarget[0])  
    (j,i) = elementToCoord(element, numberOfRows,numberOfColumns)
    if len(listOfPlacedElements) == 4:
        listForRemovingFromAdjacencyMatrix = []
        if j + 1 < numberOfRows and labeledTarget[j+1][i] != 0:
            listForRemovingFromAdjacencyMatrix.append(labeledTarget[j+1][i])
        if i + 1 < numberOfColumns and labeledTarget[j][i+1] != 0:
            listForRemovingFromAdjacencyMatrix.append(labeledTarget[j][i+1])
        if j - 1 >= 0 and labeledTarget[j-1][i] != 0:
            listForRemovingFromAdjacencyMatrix.append(labeledTarget[j-1][i])
        if i - 1 >= 0 and  labeledTarget[j][i-1] != 0:
            listForRemovingFromAdjacencyMatrix.append(labeledTarget[j][i-1])            
        
        for toRemove in listForRemovingFromAdjacencyMatrix:
            try:
                AdjacencyList[toRemove].remove(element)   
            except ValueError:
                pass
        for piece in listOfPlacedElements:
            if len(AdjacencyList[piece]) > 0:
                AdjacencyList[piece] = []
        return 
    
    else:
        for neighbour in AdjacencyList[element]:
            listOfPositions.append([neighbour,len(AdjacencyList[neighbour])]) 
        ToFindMin = []
        for x in range(len(listOfPositions)):
            ToFindMin.append(listOfPositions[x][1])
        if ToFindMin == []:
            for y in listOfPlacedElements:
                for x in listOfPositions:
                    (j,i) = elementToCoord(x,numberOfRows,numberOfColumns)                      
                    if j + 1 < numberOfRows and labeledTarget[j+1][i] == y:
                        AdjacencyList[labeledTarget[j][i]].append(labeledTarget[j+1][i])
                    if i + 1 < numberOfColumns and target[j][i+1] == y:
                        AdjacencyList[labeledTarget[j][i]].append(labeledTarget[j][i+1])
                    if j - 1 >= 0 and target[j-1][i] == y:
                        AdjacencyList[labeledTarget[j][i]].append(labeledTarget[j-1][i])
                    if i - 1 >= 0 and  target[j][i-1] == y: 
                        AdjacencyList[labeledTarget[j][i]].append(labeledTarget[j][i-1])
                    

        else:
            indexOfSmallest = ToFindMin.index(min(x for x in ToFindMin))
            listOfPlacedElements.append(listOfPositions[indexOfSmallest][0])
            listForRemovingFromAdjacencyMatrix = []
            if j + 1 < numberOfRows and labeledTarget[j+1][i] != 0:
                listForRemovingFromAdjacencyMatrix.append(labeledTarget[j+1][i])
                #print('down')
            if i + 1 < numberOfColumns and labeledTarget[j][i+1] != 0:
                listForRemovingFromAdjacencyMatrix.append(labeledTarget[j][i+1])
                #print('right')   
            if j - 1 >= 0 and labeledTarget[j-1][i] != 0:
                listForRemovingFromAdjacencyMatrix.append(labeledTarget[j-1][i])
                #print('Up')
            if i - 1 >= 0 and  labeledTarget[j][i-1] != 0:
                listForRemovingFromAdjacencyMatrix.append(labeledTarget[j][i-1])            
                #print('left')
            for toRemove in listForRemovingFromAdjacencyMatrix:
                try:
                    AdjacencyList[toRemove].remove(element)
                except ValueError:
                    pass
            del listOfPositions[indexOfSmallest]
            for neighbour in AdjacencyList[element]:
                for position in range(len(listOfPositions)):
                    if neighbour == listOfPositions[position][0]:
                        listOfPositions[position][1] -= 1
            FindNextElementInShape(AdjacencyList,listOfPlacedElements[-1],listOfPositions, listOfPlacedElements, labeledTarget)
    

def findShapeID(listOfDirections,ShapeIds):
    for i in range(1,20):
        if listOfDirections in ShapeIds[i]:
            #print(i)
            return i

def createLabeledTarget(target):
    labeledTarget = copy.deepcopy(target)
    counter = 1
    numberOfRows = len(target)
    numberOfColumns = len(target[0])    
    for i in range(numberOfColumns):
        for j in range(numberOfRows):
            if labeledTarget[j][i] == 1:
                labeledTarget[j][i] = counter
            counter += 1
    return labeledTarget

def AdjacencyListOfLabeledTarget(labeledTarget):
    numberOfRows = len(labeledTarget)
    numberOfColumns = len(labeledTarget[0])     
    numberOfElements = numberOfColumns * numberOfRows
    #print(numberOfElements)

    AdjacencyList = [[] for _ in range(numberOfElements+1)]
    return AdjacencyList

def addNeighboursToNodes(AdjacencyList,labeledTarget):
    numberOfRows = len(labeledTarget)
    numberOfColumns = len(labeledTarget[0])    
    for i in range(numberOfColumns):
        for j in range(numberOfRows):
            if labeledTarget[j][i] != 0:
                if j + 1 < numberOfRows and labeledTarget[j+1][i] != 0:
                    AdjacencyList[labeledTarget[j][i]].append(labeledTarget[j+1][i])
                if i + 1 < numberOfColumns and labeledTarget[j][i+1] != 0:
                    AdjacencyList[labeledTarget[j][i]].append(labeledTarget[j][i+1])
                if j - 1 >= 0 and labeledTarget[j-1][i] != 0:
                    AdjacencyList[labeledTarget[j][i]].append(labeledTarget[j-1][i])
                if i - 1 >= 0 and  labeledTarget[j][i-1] != 0:
                    AdjacencyList[labeledTarget[j][i]].append(labeledTarget[j][i-1])

def createEmptySol(numberOfRows,numberOfColumns,solution):
    for i in range(numberOfRows):
        row = [(0,0) for _ in range(numberOfColumns)]
        solution.append(row)     

def elementToCoord(element,numberOfRows,numberOfColumns):
    if element%numberOfRows == 0:
        j = numberOfColumns - 1
        i = int(element/numberOfRows) -1   
    else:
        j = element%numberOfRows - 1
        i = int(element/numberOfRows)  
    return j,i


def Tetris(target):
    labeledTarget = createLabeledTarget(target)
    numberOfRows = len(labeledTarget)
    numberOfColumns = len(labeledTarget[0]) 
    numberOfElements = numberOfColumns*numberOfRows
    
    solution = []
    createEmptySol(numberOfRows,numberOfColumns,solution)
    AdjacencyList = AdjacencyListOfLabeledTarget(labeledTarget)
    addNeighboursToNodes(AdjacencyList,labeledTarget)
    
    count = 1
    
    for element in range(numberOfElements+1):
        if len(AdjacencyList[element]) > 0:
            listOfPositions = []
            listOfPlacedElements = [element]
            FindNextElementInShape(AdjacencyList,element,listOfPositions,listOfPlacedElements, labeledTarget)
            #print(listOfPlacedElements)
            jPositionsForShapeIds = []
            iPositionsForShapeIds = []           
            if len(listOfPlacedElements) == 4:
                for unomino in listOfPlacedElements:
                    (j,i)  = elementToCoord(unomino,numberOfRows,numberOfColumns)
                    jPositionsForShapeIds.append(j)
                    iPositionsForShapeIds.append(i)
                indexOfNewZero = iPositionsForShapeIds.index(min(iPositionsForShapeIds))
                
                toCheckForID = []
                for var in range(4):
                    y = jPositionsForShapeIds[var]-jPositionsForShapeIds[indexOfNewZero]
                    x = iPositionsForShapeIds[var]-iPositionsForShapeIds[indexOfNewZero]
                    toCheckForID.append((y,x))
                setToCheck = set(x for x in toCheckForID)
                    
                shapeID = findShapeID(setToCheck, shapeIDs)

                for unomino in listOfPlacedElements:
                    (j,i) = elementToCoord(unomino,numberOfRows,numberOfColumns) 
                    solution[j][i] = (shapeID,count)
                count += 1
                
    return solution