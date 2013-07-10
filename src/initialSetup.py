import clock
import continousAsignation
import cpu
import hdd
import io
import irq
import kernel
import memory
import pcb
import programInstruction
import scheduler
import shell
import timer
import mmu
import logging

##Set up for logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

logging.info("Hi.. Let's start up the system..")
logging.info(' ')
logging.info('==========Loading resources modules...==========')
logging.info(' ')
aScheduler = scheduler.Fifo()
logging.info('=======Scheduler load [OK]')
aMemory = memory.Memory(50)
logging.info('=======Fisical memory load [OK]')
aFit = continousAsignation.FirstFit()
anAsignation = continousAsignation.ContinousAsignation(aMemory, aFit)
logging.info('=======Memory Asignation set [OK]')
aMMU = mmu.MMU(anAsignation)
logging.info('=======MMU Loaded load [OK]')
anIRQ = irq.IRQ()
anIRQHandler = irq.IRQHandler(anIRQ)
logging.info('=======IRQ set [OK]')
anIO = io.IO(anIRQ)
aCPU = cpu.CPU(anIRQ, anIO)
logging.info('=======IO & CPU founded [OK]')
aTimer = timer.Timer(anIO, aCPU, 3)
aClock = clock.Clock(aTimer)
aShell = shell.Shell()
logging.info('=======Shell interface load [OK]')

aKernel = kernel.Kernel(aScheduler, anIRQ, aResourcesManager, aShell, aCPU, aMMU)
logging.info('=======Kernel load [OK]')

program1 = programInstruction.Program()
program2 = programInstruction.Program()
program3 = programInstruction.Program()
instruccion1 = programInstruction.IOInstruction()
instruccion2 = programInstruction.CPUInstruction()
instruccion3 = programInstruction.EndInstruction()

"""Matching up programs with instructions"""

program1.add(instruccion2)
program1.add(instruccion2)
program1.add(instruccion2)
program1.add(instruccion1)
program1.add(instruccion1)
program1.add(instruccion3)
program2.add(instruccion1)
program2.add(instruccion1)
program2.add(instruccion1)
program2.add(instruccion2)
program2.add(instruccion2)
program2.add(instruccion3)
program3.add(instruccion1)
program3.add(instruccion2)
program3.add(instruccion1)
program3.add(instruccion2)
program3.add(instruccion1)
program3.add(instruccion3)
logging.info('=======Programs on system load [OK]')

#aShell.addProgram(program1)
#aShell.addProgram(program2)
#aShell.addProgram(program3)

aKernel.loadProgram(program1)
aKernel.loadProgram(program2)
aKernel.loadProgram(program3)

logging.info(' ')
logging.info('===============Welcome to SO Riddler v0.2===============') 
aClock.run()
#aShell.run()

