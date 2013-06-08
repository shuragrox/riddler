class Timer():

    def __init__(self, aCPU):

        self.cpu = aCPU
        self.quantum = 5
        self.acc = 0

    def clock(self):

        if self.acc < self.quantum:
            self.acc = self.acc + 1
            try:
                self.cpu.execute()
            except:
                self.cpu.getProcess()
        else:
            self.cpu.getProcess()
            self.acc = 0

