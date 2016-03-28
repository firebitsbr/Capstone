import node
from crawlerconfig import CrawlerConfig
#import result

class WebCrawler:

	def __init__(self, config):
		self.config = config
		#self.results = Result(config)
		self.links = [None]		

	def doCrawl():
		initial_node = node(config.get_crawl_location(), 1)
		links.append(initial_node)
		
		results = doScrape(initial_node)

		while links[0].get_currentDepth() < config.get_depth():
			for child in links[0].get_children():
				next_node = node(link[0].get_url(), child, link[0].get_currentDepth()+1)
				links.append(next_node)
				results = doScrape(next_node)
				print results
			dummy = links.pop(0)	


	def doScrape(current_node):
		#timeStart=
		
		#must import after the above two lines are executed
		import urllib2
		from bs4 import BeautifulSoup

		try:
			data = urllib2.urlopen(current_node.get_url()).read()
		#finally:
		soup = BeautifulSoup(data)

		lst=[None]

		for a in soup.find_all('a', href=True):
			lst.append(a['href'])
		for b in soup.find_all('link', href=True):
			lst.append(b['href'])

		current_node.set_children(lst)
		#timeEnd=
		results = Results(crawlerconfig, timeStart, timeEnd, current_node.get_url(), current_node.get_parent(), data)
		return results