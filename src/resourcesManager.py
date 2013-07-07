class ResourcesManager():
    def __init__(self, io, cpu, memory)
        self.io = io
        self.cpu = cpu
        self.memory = memory

    def getNextInstruction(self, aPCB):
        i = self.memory.getInstruction(aPCB)
        if i.isIO() == true:
            self.io.addPCB(aPCB)
            self.cpu.setCurrentProcess(None)
        else:
            return i
 
    def getIOInstruction(self, aPCB):
        i = self.memory.getIntruction(aPCB)
        return i

