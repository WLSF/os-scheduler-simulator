from block_linked_list import BlockLinkedList
from block import Block
from memory_request import MemoryRequest

class MemoryManager(Thread):
	def __init__(self, mem_size, list_processes):
		Thread.__init__(self)

		block = Block(mem_size, 0)

		self.free_blocks = [block]
		self.busy_blocks = []
		self.blocks = BlockLinkedList(block)
		self.processes = list_processes

	def run(self):
		while len(self.processes) > 0:
			p = self.processes[0]

			if p.has_request:
				mem_req = p.memory_requests.popleft()

				if len(self.free_blocks) > 0:
					pass