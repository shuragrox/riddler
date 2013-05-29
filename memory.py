class Memory():
	
	def __init__(self):
		
		self.memory = dict()
		
	def loadProgram(self, aProgram, anID)
	
		if(self.notExistentID(anID)):
			self.memory[anID] = aProgram
		else:
			raise ExistentIDException
			
	def getInstruction(self, anID, aPC):
		
		return self.memory[anID] [aPC]
			
	def nonExistentID(self, anID):
		
		return anID in self.memory
