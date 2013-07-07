class PCB():
    def __init__(self, aPid, aBase, aSize):
        self.pid = aPid
        self.pc = 0
        self.base = aBase
        self.size = aSize

    def getPc(self):
        return self.pc

    def size():
        return this.size

    def getSize():
        return this.size

    def incPc(self):
        """"Increases the pc by 1"""
        self.pc += 1

    def getID(selflf):
        return self.pid

    def getBase(self):
        return self.base

    def hasNextInstruction(self, aSize):
        return (self.pc < aSize) and (self.pc != aSize)

class PCBPriority(PCB):
    def __init__(self, aPid, aBase, aPriority):
        PCB.__init__(self, aPid, aBase)
        self.priority = aPriority

