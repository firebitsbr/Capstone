import manageTor						# only used for Tor
import node								#
from crawlerconfig import CrawlerConfig	#
from crawler import Crawler				#
import result
import robotparser
import datetime
import time
import re

class WebCrawler(Crawler):

	def __init__(self, config):
		self.config = config
		self.results = Result(config)
		self.links = []		

	def doCrawl(self):
		initial_node = node(config.location, 1)
		links.append(initial_node)
		
		results = self.doScrape(initial_node)
		config.send_result(results)

		while (links[0].get_currentDepth() < int(config.maxDepth)):
			for child in links[0].get_children():
				next_node = node(links[0].get_url(), child, links[0].get_currentDepth()+1)
				links.append(next_node)
				time.sleep(config.speed)
				results = self.doScrape(next_node)
				config.send_results(results)
				#print results
			dummy = links.pop(0)
		
	def doScrape(self, current_node):
        	timeStart=datetime.datetime.now()
		if (config.protocol == tor):	# needs to be verified as the correct variable
			tor = manageTor.open()
			manageTor.torProxy()
		#must import after the above two lines are executed
        	import urllib2
        	from bs4 import BeautifulSoup

		try:
			data = urllib2.urlopen(current_node.get_url()).read()
		finally:
			if (config.protocol == tor):	# needs to be verified as the correct variable
				manageTor.close(tor)
		except:
			print "Failled to retrieve " + current_node.get_url()
			exit()
		soup = BeautifulSoup(data)

		lst=[]

		for a in soup.find_all('a', href=True):
			lst.append(a['href'])
		for b in soup.find_all('link', href=True):
			lst.append(b['href'])
		fqlst=[]						# fully qualified list
		for n in lst:
			if not n.startswith("http"):
				fqlst.append(current_node.get_url() + n)
			else:
				fqlst.append(n)
		if (config.protocol == tor):
			tor = manageTor.open()
			manageTor.torProxy()
			onion=[]
			for i in fqlst:
				if ".onion" in i:
					k = i[:29]
					k+="/robots.txt"
					rp = robotparser.RobotFileParser()
					rp.set_url(k)
					time.sleep(config.speed)
					try:
						rp.read()
					except:
						print "Host unreachable: " + k
					if rp.can_fetch("*", i):
						onion.append(i)
			manageTor.close(tor)
			current_node.set_children(onion)
		else:
			weblist=[]
			for i in fqlst:
				x=i.split("\") 				# custom regex
				k=x[0]+"//"+x[2]+"/robots.txt"		# custom regex
				rp = robotparser.RobotFileParser()
				rp.set_url(k)
				time.sleep(config.speed)
				try:
					rp.read()
				except:
					print "Host unreachable: " + k
				if rp.can_fetch("*", i):
					weblist.append(i)
				# following robots yet to be implemented
				current_node.set_children(weblist)
		timeEnd=datetime.datetime.now()
		results = Results(crawlerconfig, timeStart, timeEnd, current_node.get_url(), current_node.get_parent(), data)
		return results
