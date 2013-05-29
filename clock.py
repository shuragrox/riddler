import threading
import time

class Clock(threading.Thread):
	
	def __init__(self, aCPU):
		
		threading.Thread.__init__(self)
		self.CPU = aCPU
		
	def run(self):
		
		while(True):
			time.sleep(1)
			self.CPU.execute()
			
