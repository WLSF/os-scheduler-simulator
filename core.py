import time
from threading import Thread, BoundedSemaphore

g_WLSF_ID = 0

class Core:
	def __init__(self, quantum):
		global g_WLSF_ID
		self.id = g_WLSF_ID
		g_WLSF_ID += 1
		self.quantum = quantum

	def set_scheduler_ref(self, scheduler):
		self.scheduler = scheduler

	def set_semaphore(self, semaphore):
		self.semaphore = semaphore

	def set_process(self, process):
		self.thread = Thread(target=self.run)
		self.process = process

	def execute(self):
		for i in range(self.quantum):
			time.sleep(1)

			if self.process.total_time > 0:
				self.process.total_time -= 1
			else:
				break

	def run(self):
		self.semaphore.acquire()
		
		self.execute()

		self.semaphore.release()

		self.scheduler.core_finished(self)