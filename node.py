class treeNode():
    def __init__(self, attribute, threshold, leftChild, rightChild):
        self.setAttr(attribute)
        self.setThreshold(threshold)
        self.setLeftChild(leftChild)
        self.setRightChild(rightChild)

    def setAttr(self, attrIndx):
        self.irisAttribute = attrIndx

    def setThreshold(self, threshold):
        self.threshold = threshold

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def setRightChild(self, rightChild):
        self.rightChild = rightChild

    def getAttr(self):
        return self.irisAttribute
    
    def getThreshold(self):
        return self.threshold
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
class leafNode():
    def __init__(self, assignedClass):
        self.setAssignedClass(assignedClass)

    def setAssignedClass(self, assignedClass):
        self.assignedClass = assignedClass

    def getAssignedClass(self):
        return self.assignedClass