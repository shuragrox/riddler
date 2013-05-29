class CPU():
	
	def __init__(self, aScheduler, aMemory):
		
		self.scheduler = aScheduler
		self.currentProcess = None
		self.memory = aMemory
		
	def execute(self):
		
		"Executes next instruction of current process"
		
		if(self.currentProcess.hasNextInstruction()):
			self.memory.getInstruction(self.currentProcess.getID(), self.currentProcess.getPc()).execute()
		else:
			raise ContextSwitchingException
	
	def getProcess(self):
		
		self.setCurrentProcess(self.scheduler.getProcess())
	
	def setCurrentProcess(self, aProcess):
		
		self.currentProcess = aProcess
		

class PCB():
	
	def __init__(self, aPid):
		
		self.pid = aPid
		self.pc = 0
		
	def getPc(self):
		
		return self.pc
		
	def setPc(self, aNumber):
		
		self.pc = aNumber
		
	def getID(self):
		
		return self.pid

class PCBPriority(PCB):
	
	def __init__(self, aPid, aPriority):
		
		PCB.__init__(self)
		self.priority = aPriority
