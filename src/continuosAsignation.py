class ContinuosAsignation:
    def __init__(self, mmu, asignationFit):
        self.mmu = mmu
        self.asignationFit = asignationFit

    def loadProgram(self, aProgram):
        if (aProgram.length() > self.mmu.size()):
            raise NotEnoughMemoryException()
        else:
            if (self.mmu.getFreeSize() > aProgram.length()):
                self.asignationFit.loadProgram(aProgram, self.mmu)

class AsignationFit:
    def loadProgram(self, aProgram, mmu): 
        pass

class WorstFit(AsignationFit):
    def __init__(self):
        AsignationFit.__init__(self)

    def loadProgram(self, aProgram, mmu):
        newBlock = None
        for block in mmu.getFreeBlocks():
            if newBlock = None:
                newBlock = block
            else:
                if block.size() > newBlock.size():
                    newBlock = block
        if newBlock.size() >= aProgram.size():
            mmu.loadProgram(aProgram, newBlock)
        else:
            mmu.compact()
            self.loadProgram(aProgram, mmu)

class FirstFit(AsignationFit):
    def __init__(self):
        AsignationFit.__init__(self)

    def loadProgram(self, aProgram, mmu):
        for block in mmu.getFreeBlocks():
            if block.size() >= aProgram.size():
                mmu.loadProgram(aProgram, block)
                break
        else:
            mmu.compact()
            self.loadProgram(aProgram, mmu)

class BestFit(AsignationFit):
    def __init__(self):
        AsignationFit.__init__(self)

    def loadProgram(self, aProgram, mmu):
        newBlock = None
        for block in mmu.getFreeBlocks():
            if newBlock = None:
                newBlock = block
            else:
                if block.size() >= aProgram.size() && block.size() < newBlock.size():
                    newBlock = block
        if newBlock.size() < aProgram.size():
            mmu.compact()
        else:
            mmu.loadProgram(aProgram, newBlock)

class NotEnoughMemoryException(Exception):
    def __str__(self):
        return "Not enough memory. Program size is bigger than memory size."

