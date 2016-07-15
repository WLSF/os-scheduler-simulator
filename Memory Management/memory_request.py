g_WLSF_ID = 0

class MemoryRequest:
	def __init__(self, p_id, mem_size):
		global g_WLSF_ID
		self.id = g_WLSF_ID
		g_WLSF_ID += 1
		self.p_id = p_id
		self.mem_size = mem_size