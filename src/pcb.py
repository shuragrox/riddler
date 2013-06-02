class PCB():
    def __init__(self, aPid):
        self.pid = aPid
        self.pc = 0

    def getPc(self):
        return self.pc

    def setPc(self, aNumber):
        self.pc = aNumber

    def incPc(self):
        self.pc += 1

    def getID(self):
        return self.pid

    def hasNextInstruction(self):
        return self.pc == processSize ##TODO

class PCBPriority(PCB):
    def __init__(self, aPid, aPriority):
        PCB.__init__(self,aPid)
        self.priority = aPriority
