import manageTor						# only used for Tor
import node								#
from crawlerconfig import CrawlerConfig	#
from crawler import Crawler				#
#import result

class WebCrawler(Crawler):

	def __init__(self, config):
		self.config = config
		#self.results = Result(config)
		self.links = []		

	def doCrawl(self):
		initial_node = node(config.get_location(), 1)
		links.append(initial_node)
		
		results = self.doScrape(initial_node)

		while (links[0].get_currentDepth() < int(config.get_maxDepth())):
			for child in links[0].get_children():
				next_node = node(links[0].get_url(), child, links[0].get_currentDepth()+1)
				links.append(next_node)
				results = doScrape(next_node)
				print results
			dummy = links.pop(0)
		
	def doScrape(self, current_node):
        #timeStart=0
		if (self.config.protocol == tor)	# needs to be verified as the correct variable
			tor = manageTor.open()
			manageTor.torProxy()
		#must import after the above two lines are executed
        import urllib2
        from bs4 import BeautifulSoup

		try:
			data = urllib2.urlopen(current_node.get_url()).read()
		finally:
		if (self.config.protocol == tor)	# needs to be verified as the correct variable
			manageTor.close(tor)
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