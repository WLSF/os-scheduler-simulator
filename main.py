from core import Core
from process import Process

from scheduler import Scheduler

from collections import deque

def main():
	print 'Welcome to WLSF-OS, made in Python by Capy Solutions'
	n_cores = int(raw_input('Enter the amount of cores you gonna use: '))
	quantum = int(raw_input('Enter the quantum time for the cores(Round-Robin preemptive): '))
	n_processes = int(raw_input('Enter the amount of process you wanna create: '))

	cores = [Core(quantum) for i in range(n_cores)]
	processes = deque(Process() for i in range(n_processes))

	scheduler = Scheduler(cores, processes)
	scheduler.setup()

	scheduler.start()

	scheduler.join()

'''
	print 'Thanks god, ala, buda, sloth, all the processes has finished.'
'''

main()