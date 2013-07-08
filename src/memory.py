class Memory():
    def __init__(self, aSize):
        self.size = aSize
        self.memory = []

    def loadProgram(self, aProgram, aBlock):
        """aBlock its used to know the base position
                on the memory, where is loaded the first
                      instruc of the program.
        """
        position = aBlock.getBase()
        for instrc in aProgram.getInstructions():
            self.memory.insert(position, instrc)
            position += 1
        return aBlock.getBase()

    def getInstruction(self, aPCB):
        """aPCB must exist in the system"""
            return self.memory.index(aPCB.getBase() + aPCB.getPc())

