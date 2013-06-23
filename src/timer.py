class Timer():

    def __init__(self, aCPU):

        self.cpu = aCPU
        self.quantum = 3
        self.acc = 0

    def clock(self):

        if self.acc < self.quantum:
            self.acc = self.acc + 1
            self.cpu.execute()
        else:
            self.cpu.contextSwitching()
            self.acc = 0

