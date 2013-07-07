class MMU():
    def __init__(self, aSize):
        self.size = aSize
        self.memory = []
        self.fillBlocks = []

    def loadProgram(self, aProgram, aBlock):
        position = aBlock.getBase()
        for instrc in aProgram.getInstructions():
            self.memory.insert(position, instrc)
            position += 1
        return aBlock.getBase()

    def getInstruction(self, aPCB):
        """aPCB must exist in the system"""
            return self.memory.index(aPCB.getBase() + aPCB.getPc())

    def getFreeBlocks(self):
        freeBlocks = []
        position = 0
        if self.getAmountFillBlocks() = 0:
            freeBlocks.append(Block(position, self.size))
        else:
            for block in self.fillBlocks:
                freeBlocks.append(Block(position, block.getBase() - position))
                position = block.getBase() + block.size() + 1
        return freeBlocks

    def getFreeSize():
        total = 0
        if self.getAmountFillBlocks() = 0:
            total = self.size
        else:
            for block in self.fillBlocks:
                total += block.size()
        return total

    def getFillBlocks(self):
        return self.fillBlocks

    def getAmountFreeBlocks(self):
        return len(self.getFreeBlocks())

    def getAmountFillBlocks(self):
        return len(self.getFillBlocks())

    def compact():
        position = 0
        for block in self.getFillBlocks():
            positionBlock = block.getBase()
            if positionBlock < block.size():
                i = self.memory.index(positionBlock)
                self.memory.insert(position, i)
                position += 1

