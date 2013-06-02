class CPU():
    def __init__(self, aScheduler, aMemory):
        self.scheduler = aScheduler
        self.currentProcess = None
        self.memory = aMemory
    
    def execute(self):
        "Executes next instruction of current process"
        if(self.hasNextInstruction()):
            currentProcessID = self.currentProcess.getID()
            currentProcessPC = self.currentProcess.getPc()
            instructionToExec = self.memory.getInstruction(self.currentProcessID, self.currentProcessPC)
            instructionToExec.execute()
        else:
            raise ContextSwitchingException

    def getProcess(self):
        self.setCurrentProcess(self.scheduler.getProcess())

    def setCurrentProcess(self, aProcess):
        self.currentProcess = aProcess
