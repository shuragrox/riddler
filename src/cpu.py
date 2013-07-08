class CPU():

    def __init__(self, aIRQ):
        self.currentProcess = None
        self.kernel= None
        self.irq = aIRQ

    def execute(self):
        """ Executes next instruction of current process """
        if self.kernel.isKernelMode():
            if self.currentProcess == None:
                self.irq.contextSwitch()
            if self.currentProcess.hasNextInstruction(self.currentProcess.size()):
                currentProcessPC = self.currentProcess.getPc()
                instructionToExec = self.kernel.resourcesManager.getInstruction(self.currentProcess)
                instructionToExec.execute()
                self.currentProcess.incPc()
            else:
                self.irq.contextSwitch()

    def setCurrentProcess(self, aProcess):
        self.currentProcess = aProcess

    def setKernel(self, aKernel):
        self.kernel = aKernel

    def canExecute(self):
        return not self.kernel.isKernelMode()

