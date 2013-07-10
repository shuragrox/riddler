class CPU():

    def __init__(self, anIRQ, anIO, aMMU):
        self.currentProcess = None
        self.irq = anIRQ
        self.io = anIO
        self.mmu = aMMU

    def execute(self):
		#Este método necesita ser modificado los pasos a seguir son
		#Si el current no es None le pide al mmu la próxima instruccion
		#Si es de cpu la ejecuta, sino la manda a IO
        """ Executes next instruction of current process """
        if not self.kernel.isKernelMode():
            if self.currentProcess == None:
                self.irq.contextSwitch()
            elif self.currentProcess.hasNextInstruction(self.currentProcess.size):
                currentProcessPC = self.currentProcess.getPc()
                instructionToExec = self.kernel.resourcesManager.getNextInstruction(self.currentProcess)
                if not instructionToExec == None:
                    instructionToExec.execute()
                    self.currentProcess.incPc()
            else:
                self.irq.contextSwitch()
        else:
            self.kernel.shell.run()

    def setCurrentProcess(self, aProcess):
        self.currentProcess = aProcess

    def getCurrentProcess(self):
        return self.currentProcess
