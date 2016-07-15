from random import randint
from memory_request import MemoryRequest

g_WLSF_ID = 0

class Process:
	def __init__(self):
		global g_WLSF_ID
		self.id = g_WLSF_ID
		g_WLSF_ID += 1
		self.total_time = randint(10, 30)
		self.bytes_required = 2 ** randint(5, 10)
		self.memory_requests = deque()
		self.make_request()
		self.has_request = True

	def make_request(self):
		self.memory_requests.append(MemoryRequest(self.id, 2 ** ranint(5, 10)))