#RPQ = Ready Process Queue

import Queue

class Scheduler():
""" This is an abstract class, 
    with methods for all subclasses. 
"""

    def getProcess(self):
    """ Returns the next process of the rpq """
        self.rpq.get()	
	
    def addProcess(self, aPCB):
    """ Adds an pcb to the rpq """
        self.rpq.put(aPCB)

class Fifo(Scheduler):
    def __init__(self):
        self.rpq = Queue.Queue()

class RoundRobin(Scheduler):
    def __init__(self, aQuantum):
        self.rpq = Queue.Queue()
        self.quantum = aQuantum

class Priority(Scheduler):
<<<<<<< HEAD

	def __init__(self):

		self.rpq = Queue.PriorityQueue()

	def addProcess(self, aPCB):

		self.rpq.put(aPCB.priority, aPCB.data)
=======
    def __init__(self):
        self.rpq = Queue.PriorityQueue()
>>>>>>> 3855313cbdac3bf62728e7a91322a2e63d7735e3
