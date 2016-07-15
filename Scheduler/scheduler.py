from threading import Thread, BoundedSemaphore
import time

class Scheduler(Thread):
	def __init__(self, list_cores, list_processes):
		Thread.__init__(self)
		self.cores = list_cores
		self.processes = list_processes
		self.semaphore = BoundedSemaphore(len(self.cores))
		self.free_cores = []

	def setup(self):
		for core in self.cores:

			if len(self.processes) == 0:
				break

			process = self.processes.popleft()

			core.set_scheduler_ref(self)
			core.set_semaphore(self.semaphore)
			core.set_process(process)
			core.thread.start()

	def add_process(self):
		self.processes.append(Process())


	def core_finished(self, core):
		process = core.process

		if process.total_time > 0:
			self.processes.append(process)

		self.cores.remove(core)
		self.free_cores.append(core)

	def request_core(self, process):
		core = self.free_cores.pop()
		core.set_process(process)
		self.cores.append(core)
		core.thread.start()


	def run(self):
		while len(self.processes) > 0:

			if len(self.free_cores) > 0:
				if len(self.processes) > 0:
					process = self.processes.popleft()
					self.request_core(process)

