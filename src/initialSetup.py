import clock
import continousAsignation
import cpu
import hdd
import io
import irq
import kernel
import mmu
import pcb
import programInstruction
import resourcesManager
import scheduler
import shell
import timer

aScheduler = scheduler.Fifo()
aMMU = mmu.MMU(256)
irq = irq.IRQ()
irqHandler = irq.IRQHandler(irq)
aCpu = cpu.(aMMU)

