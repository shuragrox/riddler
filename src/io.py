import clock

class IO:
    
    def __init__(self, irq):
        self.readyQueue = []
        self.currentPCB = None
        self.irq = irq

    def addPCB(self, aPCB):
        self.readyQueue.append(aPCB)

    def execute(self):
        if currentPCB == None && not len(self.readyQueue) == 0:
            self.readyQueue.reverse()
            self.currentPCB = self.readyQueue.pop()
            self.readyQueue.reverse()

            i = self.resourcesManager.getIOInstruction(aPCB)   
            i.execute() 
            self.currentPCB.incPc()
            self.irq.contextSwitchIO()
    
     def reset(self):
         self.currentPCB = None

