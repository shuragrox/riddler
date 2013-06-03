class CPU():
    def __init__(self, aScheduler, aMemory):
        self.scheduler = aScheduler
        self.currentProcess = None
        self.memory = aMemory

    def execute(self):
        "Executes next instruction of current process"
        currentProcessID = self.currentProcess.getID()
        if self.currentProcess.hasNextInstruction(self.memory.getProgramSize(currentProcessID)):
            currentProcessPC = self.currentProcess.getPc()
            instructionToExec = self.memory.getInstruction(currentProcessID, currentProcessPC)
            instructionToExec.execute()
            self.currentProcess.incPc()
        else:
            raise ContextSwitchingException

    def getProcess(self):
        self.setCurrentProcess(self.scheduler.getProcess())

    def setCurrentProcess(self, aProcess):
        self.currentProcess = aProcess
