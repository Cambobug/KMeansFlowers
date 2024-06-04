
class Iris():
    def __init__(self, sepelL, sepelW, petalL, petalW, type):
        self.setSepelL(sepelL)
        self.setSepelW(sepelW)
        self.setPetalL(petalL)
        self.setPetalW(petalW)
        self.setType(type)

    def setSepelL(self, newSepelL):
        self.sepelL = round(newSepelL,1)

    def setSepelW(self, newSepelW):
        self.sepelW = round(newSepelW,1)

    def setPetalL(self, newPetalL):
        self.petalL = round(newPetalL,1)

    def setPetalW(self, newPetalW):
        self.petalW = round(newPetalW,1)

    def setType(self, newType):
        self.type = newType

    def getSepelL(self):
        return self.sepelL
    
    def getSepelW(self):
        return self.sepelW
    
    def getPetalL(self):
        return self.petalL
    
    def getPetalW(self):
        return self.petalW
    
    def getType(self):
        return self.type
    
    def printIris(self):
        petL = self.getPetalL()
        petW = self.getPetalW()
        sepL = self.getSepelL()
        sepW = self.getSepelW()
        type = self.getType()
        return str(sepL) + " " + str(sepW) + " " + str(petL) +" " +str(petW) + " " + type