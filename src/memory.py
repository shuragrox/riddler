class Memory():
    def __init__(self):
        self.memory = dict()

    def loadProgram(self, aProgram, anID):
        if not self.existsID(anID):
            self.memory[anID] = aProgram
        else:
            raise ExistentIDException

    def getInstruction(self, anID, aPC):
        if(self.existsID(anID)):
            return self.memory[anID].getInstruction(aPC)
        else:
            raise NonExistentIDException

    def existsID(self, anID):
        return anID in self.memory

    def getProgramSize(self, anID):
        return self.memory[anID].length()

