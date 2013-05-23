#RPQ = Ready Process Queue

import Queue

class Scheduler():
	
	def getProcess(self):
		
		self.rpq.get()	
	
	def addProcess(self, aPCB):

		self.rpq.put(aPCB)


class Fifo(Scheduler):
	
	def __init__(self):
		
		self.rpq = Queue.Queue()


class RoundRobin(Scheduler):

	def __init__(self, aQuantum):

		self.rpq = Queue.Queue()
		self.quantum = aQuantum


class Priority(Scheduler):

	def __init__(self):

		self.rpq = Queue.PriorityQueue()
