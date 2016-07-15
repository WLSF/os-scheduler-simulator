class BlockLinkedList:
	def __init__(self):
		self.size = 0
		self.header = None
		self.trailer = None


	def addbh(self, block):
		if self.size == 0:
			self.trailer = block
		else:
			block.set_next(self.header)
			self.header.set_previous(block)
		
		self.header = block
		self.size += 1

	def addbt(self, block):
		if self.size == 0:
			self.header = block
		else:
			block.set_previous(self.trailer)
			self.trailer.set_next(block)

		self.trailer = block
		self.size += 1


	def rembh(self):
		if self.size == 0:
			return None
		else:
			self.size -= 1
			b = self.header
			self.header = self.header.get_next()


	def rembt(self):
		if self.size == 0:
			return None
		else:
			self.size -= 1
			b = self.trailer
			self.trailer = self.trailer.get_previous()