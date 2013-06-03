import clock
import timer
import cpu
import scheduler
import memory
import programInstruction


memory = memory.Memory()
fifo = scheduler.Fifo()
cpu = cpu.CPU(fifo, memory)
timer = timer.Timer(cpu)
clock =  clock.Clock(timer)
program1 = programInstruction.Program()
program2 = programInstruction.Program()
program3 = programInstruction.Program()

