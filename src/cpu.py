class CPU():
    def __init__(self, aMemory, aIRQ):
        self.currentProcess = None
        self.memory = aMemory
        self.irq = aIRQ

    def execute(self):
        """ Executes next instruction of current process """
        if self.currentProcess == None:
            self.irq.contextSwitch()
        if self.currentProcess.hasNextInstruction(self.currentProcess.size()):
            currentProcessPC = self.currentProcess.getPc()
            instructionToExec = self.memory.getInstruction(self.currentProcess)
            instructionToExec.execute()
            self.currentProcess.incPc()
        else:
            self.irq.contextSwitch()

    def setCurrentProcess(self, aProcess):
        self.currentProcess = aProcess

