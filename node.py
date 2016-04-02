class Node:

	def __init__(self, parent, url, currentDepth):
		self.parent = parent
		self.url = url
		self.currentDepth = currentDepth
		self.children = []

	def get_url(self):
		return self.url	

	def get_parent(self):
		return self.parent

	def get_currentDepth(self):
		return self.currentDepth

	def set_children(self, children):
		self.children = list(children)

	def get_children(self):
		return self.children
