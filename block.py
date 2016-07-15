g_WLSF_ID = 0

class Block:
	def __init__(self, size, total_alloc):
		global g_WLSF_ID
		self.id = g_WLSF_ID
		g_WLSF_ID += 1
		self.size = size
		self.total_alloc = total_alloc
		self.next_block = None
		self.prev_block = None

	def set_next(self, next_block):
		self.next_block = next_block

	def sext_previous(self, prev_block):
		self.prev_block = prev_block


	def get_next(self):
		return self.next_block

	def get_previous(self):
		return self.prev_block