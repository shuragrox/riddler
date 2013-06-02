from threading import threading
import time

class Clock(Thread):

    def __init__(self, aCPU):
		Thread.__init__(self)
		self.CPU = aCPU
		
    def run(self):
    """Sleeps one second, and then execute an instruction on the CPU."""
        while(True):
     	    time.sleep(1)
            self.CPU.execute()
