import iris
import helpers as h
import math as m
import random as r
import copy as c

def createRandomCentroids(points_Array, numCentroids):

    upperSepL = 0
    upperSepW = 0
    upperPetL = 0
    upperPetW = 0
    
    lowerSepL = 1000
    lowerSepW = 1000
    lowerPetL = 1000
    lowerPetW = 1000
    
    for i in points_Array: #gets the upper and lower bounds of each attribute
        
        if(i.getSepelL() > upperSepL):
            upperSepL = i.getSepelL()
        elif(i.getSepelL() < lowerSepL):
            lowerSepL = i.getSepelL()
        
        if(i.getSepelW() > upperSepW):
            upperSepW = i.getSepelW()
        elif(i.getSepelL() < lowerSepW):
            lowerSepW = i.getSepelW()
            
        if(i.getPetalL() > upperPetL):
            upperPetL = i.getPetalL()
        elif(i.getPetalL() < lowerPetL):
            lowerPetL = i.getPetalL()
            
        if(i.getPetalW() > upperPetW):
            upperPetW = i.getPetalW()
        elif(i.getPetalW() < lowerPetW):
            lowerPetW = i.getPetalW()
            
    centroid_Array = []

    while(len(centroid_Array) < numCentroids):
        nSepL = round(r.uniform(lowerSepL, upperSepL), 1)
        nSepW = round(r.uniform(lowerSepW, upperSepW), 1)
        nPetL = round(r.uniform(lowerPetL, upperPetL), 1)
        nPetW = round(r.uniform(lowerPetW, upperPetW), 1)
        
        centroid_Array.append(iris.Iris(nSepL, nSepW, nPetL, nPetW, "Centroid"))
            
    return centroid_Array

def createArraysFromCentroids(points_Array, centroid_Array):
    
    c1_Array = []
    c2_Array = []
    c3_Array = []
    
    for i in range(0, len(points_Array)):
        c1Dis = h.Euclid4D(centroid_Array[0], points_Array[i])
        c2Dis = h.Euclid4D(centroid_Array[1], points_Array[i])
        c3Dis = h.Euclid4D(centroid_Array[2], points_Array[i])
        
        if(c1Dis < c2Dis and c1Dis < c3Dis): #c1 is the closest to the point i
            cop = c.deepcopy(points_Array[i])
            c1_Array.append(cop)
        elif(c2Dis < c1Dis and c2Dis < c3Dis): #c2 is the closest to the point i
            cop = c.deepcopy(points_Array[i])
            c2_Array.append(cop)
        elif(c3Dis < c1Dis and c3Dis < c2Dis): #c3 is the closest to the point i
            cop = c.deepcopy(points_Array[i])
            c3_Array.append(cop)
            
    return c1_Array, c2_Array, c3_Array

def createtrainingSet(points_Array, centroid_Array):

    for i in range(0, 5):
        c1_Array, c2_Array, c3_Array = createArraysFromCentroids(points_Array, centroid_Array)
        
        centroid_Array = updateAllCentroids(c1_Array, c2_Array, c3_Array, centroid_Array)
        
    return c1_Array, c2_Array, c3_Array       

def updateAllCentroids(c1_Array, c2_Array, c3_Array, centroid_Array):
    
    centroid_Array[0] = updateCentroid(c1_Array, centroid_Array[0])
    centroid_Array[1] = updateCentroid(c2_Array, centroid_Array[1])
    centroid_Array[2] = updateCentroid(c3_Array, centroid_Array[2])
    
    return centroid_Array
    
def updateCentroid(centroid_Array, oldCentroid):
    if(len(centroid_Array) == 0):
        return oldCentroid
    c_SepelLsAvg = 0
    c_SepelWsAvg = 0 
    c_PetalLsAvg = 0
    c_PetalWsAvg = 0
    for i in centroid_Array:
        c_SepelLsAvg += i.getSepelL()
        c_SepelWsAvg += i.getSepelW()
        c_PetalLsAvg += i.getPetalL()
        c_PetalWsAvg += i.getPetalW()
    
    c_SepelLsAvg = c_SepelLsAvg/len(centroid_Array)
    c_SepelWsAvg = c_SepelWsAvg/len(centroid_Array)
    c_PetalLsAvg = c_PetalLsAvg/len(centroid_Array)
    c_PetalWsAvg = c_PetalWsAvg/len(centroid_Array)
    
    c_AvgCentroid = iris.Iris(c_SepelLsAvg, c_SepelWsAvg, c_PetalLsAvg, c_PetalWsAvg, "AVERAGE")

    return c_AvgCentroid

def updateCentroidClass(c1_Array, c2_Array, c3_Array, centroid_Array):
    
    points_Array = [c1_Array, c2_Array, c3_Array]
    
    for i in range(0, len(centroid_Array)):
        numSetosa = 0
        numVersicolour = 0
        numViginica = 0
        for j in points_Array[i]:
            if(j.getType() == "Iris-setosa"):
                numSetosa += 1
                
            if(j.getType() == "Iris-versicolor"):
                numVersicolour += 1
                
            if(j.getType() == "Iris-virginica"):
                numViginica += 1
    
        if(numSetosa > numVersicolour and numSetosa > numViginica):
            centroid_Array[i].setType("Iris-setosa")
            
        elif(numVersicolour > numSetosa and numVersicolour > numViginica):
            centroid_Array[i].setType("Iris-versicolor")
            
        elif(numViginica > numSetosa and numViginica > numVersicolour):
            centroid_Array[i].setType("Iris-virginica")
            
    return centroid_Array

def runTestingSet(testing_Array, centroids):
    overallAccuracy = 0
    setosaAccuracy = 0
    versiAccuracy = 0
    virginAccuracy = 0
    
    numSetosa = 0
    numVersi = 0
    numVirgin = 0
    
    for i in testing_Array:
        c1Dist = h.Euclid4D(i, centroids[0])
        c2Dist = h.Euclid4D(i, centroids[1])
        c3Dist = h.Euclid4D(i, centroids[2])
        
        if(i.getType() == "Iris-setosa"):
            numSetosa += 1
        elif(i.getType() == "Iris-versicolor"):
            numVersi += 1
        elif(i.getType() == "Iris-virginica"):
            numVirgin += 1
        
        if(c1Dist < c2Dist and c1Dist < c3Dist):
            if(i.getType() == centroids[0].getType()): #accurate clustering
                overallAccuracy += 1
                if(i.getType() == "Iris-setosa"):
                    setosaAccuracy += 1
                elif(i.getType() == "Iris-versicolor"):
                    versiAccuracy += 1
                elif(i.getType() == "Iris-virginica"):
                    virginAccuracy += 1
                
        if(c2Dist < c1Dist and c2Dist < c3Dist):
            if(i.getType() == centroids[1].getType()): #accurate clustering
                overallAccuracy += 1
                if(i.getType() == "Iris-setosa"):
                    setosaAccuracy += 1
                elif(i.getType() == "Iris-versicolor"):
                    versiAccuracy += 1
                elif(i.getType() == "Iris-virginica"):
                    virginAccuracy += 1
                
        if(c3Dist < c1Dist and c3Dist < c2Dist):
            if(i.getType() == centroids[2].getType()): #accurate clustering
                overallAccuracy += 1
                if(i.getType() == "Iris-setosa"):
                    setosaAccuracy += 1
                elif(i.getType() == "Iris-versicolor"):
                    versiAccuracy += 1
                elif(i.getType() == "Iris-virginica"):
                    virginAccuracy += 1
                    
    overallAccuracy = round(float(overallAccuracy/len(testing_Array)) * 100, 2)
    setosaAccuracy = round(float(setosaAccuracy/numSetosa) * 100, 2)
    versiAccuracy = round(float(versiAccuracy/numVersi) * 100, 2)
    virginAccuracy = round(float(virginAccuracy/numVirgin) * 100 ,2)
    
    return overallAccuracy, setosaAccuracy, versiAccuracy, virginAccuracy



data = open("iris.data", "r")

flowers_Array = []
for i in range(0, 150):
    line = data.readline()
    flowers_Array.append(h.createIris(line))

testing_Array = h.createTestingSet(flowers_Array)

minDistortionCentroids = []
minDistortion = 1000
for i in range(0, 30):
    centroid_Array = createRandomCentroids(flowers_Array, 3)

    c1_Array, c2_Array, c3_Array = createtrainingSet(flowers_Array, centroid_Array)

    setDistortion = h.calculateDistortion(c1_Array, c2_Array, c3_Array, centroid_Array)
    
    if(setDistortion < minDistortion):
        minDistortionCentroids = []
        minDistortion = setDistortion
        
        centroid_Array = updateCentroidClass(c1_Array, c2_Array, c3_Array, centroid_Array)
        for j in range(0, 3):
            minDistortionCentroids.append(c.deepcopy(centroid_Array[j]))
            
overallAccuracy, setosaAcc, versiAcc, virgAcc = runTestingSet(testing_Array, minDistortionCentroids)

print("Overall Accuracy: " + str(overallAccuracy) + "\n")
print("Setosa Accuracy: " + str(setosaAcc))
print("Versicolour Accuracy: " + str(versiAcc))
print("Virginica Accuracy: " + str(virgAcc))

data.close()