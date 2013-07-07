import PCB

class Kernel():
    def __init__(self, scheduler, irq, resourcesManager, shell):
        self.scheduler = scheduler
        self.irq = irq
        self.resourcesManager = resourcesManager
        self.shell = shell
        self.kernelMode = false
        self.pid = 0

    def loadProgram(self, aProgram):
        #Loads a program, return baseDir of that program in the memory
        base = self.resourcesManager.loadProgram(aProgram)

        #Builds new pcb to works with       
        newPCB = PCB(self.pid, base, aProgram.length())

        #Adds new pcb to scheduler's rpq
        self.scheduler.addProcess(newPCB)

        #Increments pid for next process 
        self.pid += 1

    def changeKernelMode(self):
        if self.kernelMode == false
            self.setKernelMode(true)
        else:
            self.setKernelMode(false)

    def setKernelMode(self, boolean):
        self.kernelMode = boolean

