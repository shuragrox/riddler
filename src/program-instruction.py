class Program():

    def __init__(self):
        self.instructions = []

    def add(self, aInstruction):
        self.instructions.append(aInstruction)

class Instruction():

    def execute(self):
        pass

class CPUInstruction(Instruction):

    def execute(self):
        print "Instruccion de cpu"

class IOInstruction(Instruction):

    def execute(self):
        print "Instruccion de io"

class EndInstruction(Instruction):

    def execute(self):
        print "Instruccion end"
