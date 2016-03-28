class Node:

	def __init__(self, parent, url, currentDepth)
		self.parent = parent
		self.url = url
		self.currentDepth = currentDepth
		self.children = [None]

	def __init__(self, url, currentDepth)
		self.parent = None
		self.url = url
		self.currentDepth = currentDepth

	def get_url():
		return self.url	

	def get_parent():
		return self.parent

	def get_currentDepth():
		return self.currentDepth

	def set_children(children):
		self.children = list(children)

	def get_children():
		return self.children