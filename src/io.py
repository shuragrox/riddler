import clock

class IO:
    
    def __init__(self, aTimer):
        self.clock = Clock(aTimer).run()
        self.kernel = None
        self.readyQueue = []
        self.currentPCB = None

    def setKernel(self, aKernel):
        self.kernel = aKernel

    def addPCB(self, aPCB):
        self.readyQueue.append(aPCB)

    def executeIOInstruction(self):
        if not self.currentPCB and self.readyQueue:
            self.currentPCB = self.readyQueue[0]
            del self.readyQueue[0]

        if ((not self.kernel.isModeKernel()) and bool(self.currentPCB)):
            self.currentPCB.incPC()

        ##TODO if program has finished, notify to kernel.

    def takeCurrentPCB(self):
        """ This take out current PCB, returned and reset currentPCB to None """
        currentPCB = self.currentPCB
        self.reset()
        return currentPCB

    def reset(self)
        self.currentPCB = None

    def isIdle(self):
        return not(self.currentPCB or self.readyQueue)

