import iris
import math as m
import random as r
import copy as c

def createIris(line):
    
    irisData = line.split(",")
    
    return iris.Iris(round(float(irisData[0]), 1), round(float(irisData[1]), 1), round(float(irisData[2]), 1), round(float(irisData[3]), 1), irisData[4].strip())

def createTestingSet(points_Array):
    testing_Array = []

    while(len(testing_Array) < 30):
        indx = r.randint(0, len(points_Array) - 1)
        if(testing_Array.count(points_Array[indx]) == 0): #if the testing_Array does not have that value yet (avoids duplicates)
            cop = c.deepcopy(points_Array[indx])
            points_Array.pop(indx)
            testing_Array.append(cop)
    
    return testing_Array

def Euclid4D(point1, point2):
    
    sepLDif = point2.getSepelL() - point1.getSepelL()
    sepWDif = point2.getSepelW() - point1.getSepelW()
    petLDif = point2.getPetalL() - point1.getPetalL()
    petWDif = point2.getPetalW() - point1.getPetalW()
    
    distance = m.sqrt(sepLDif**2 + sepWDif**2 + petLDif**2 + petWDif**2)

    return distance

def calculateDistortion(c1_Array, c2_Array, c3_Array, centroid_Array):
    distortion = 0
    
    points_Array = [c1_Array, c2_Array, c3_Array]
    
    for i in range(0, len(points_Array)):
        for j in range(0, len(points_Array[i])):
            distortion += (Euclid4D(centroid_Array[i], points_Array[i][j]))**2
            
    return distortion

def getNumClasses(iris_Array):

    numSetosa = 0
    numVersi = 0
    numVirgin = 0

    for i in iris_Array:
        if(i.getType() == "Iris-setosa"):
            numSetosa += 1
        elif(i.getType() == "Iris-versicolor"):
            numVersi += 1
        elif(i.getType() == "Iris-virginica"):
            numVirgin += 1

    return numSetosa, numVersi, numVirgin