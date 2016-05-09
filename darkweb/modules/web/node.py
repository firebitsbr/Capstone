# The node class allows an association to be formed between a url, its parent,
# the depth it has according to the crawl's max depth, and any child links it
# may house. This class contains basic get functions to get any part of the object
as well as one set function to set a list of links to the objects children list.


class node:

	def __init__(self, parent, url, currentDepth):
		self.parent = parent			# the link which houses the url currently be assessed
		self.url = url				# the current url being assessed
		self.currentDepth = currentDepth	# the depth at which the current url is in relation to the entire crawl
		self.children = []			# any links housed in the current urul

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
