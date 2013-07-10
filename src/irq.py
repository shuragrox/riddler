class IRQHandler():
    def __init__(self, irq):
        self.irq = irq
        self.irq.setHandler(self)

    def contextSwitch(self):
        #Change to kernel, to kernel mode.
        self.irq.kernel.changeKernelMode()

        #Get current process from cpu, added to the scheduler rpq.
        current = self.irq.kernel.resourcesManager.cpu.getCurrentProcess()
        self.irq.kernel.scheduler.addProcess(current)

        #Ask for next process to the scheduler
        newProcess = self.irq.kernel.scheduler.getProcess()
        self.irq.kernel.cpu.setCurrentProcess(newProcess)

        #Change kernel, to user mode again.
        self.irq.kernel.changeKernelMode()

    def contextSwitchIO(self):
		#No debería pasar el kernel a modo kernel?
        pcb = self.irq.kernel.cpu.io.getCurrentPCB()
        self.irq.kernel.scheduler.addProcess(pcb)
        self.irq.kernel.cpu.io.reset()

    def timeOut(self):
        self.contextSwitch()
        
    #Faltaría que la asignación continua lance una interrupción
    #de que necesita compactarse. Mientras eso sucede que el kernel
    #se pase a modo kernel.

class IRQ():
    def __init__(self):
        self.handler = None
        self.kernel = None

    def setKernel(self, aKernel):
        self.kernel = aKernel

    def setHandler(self, anIRQHandler):
        self.handler = anIRQHandler()

    def contextSwitch(self):
        self.handler.contextSwitch()

    def contextSwitchIO(self):
        self.handler.contextSwitchIO()

    def timeout(self):
        self.handler.timeOut()

