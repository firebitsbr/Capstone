import manageTor						# only used for Tor
from node import node								#
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
		#self.results = Result(config)
		self.links = []		

	def doCrawl(self):
		initial_node = node(None, self.config.location, 1)
		self.links.append(initial_node)
		
		results = self.doScrape(initial_node)
		#config.send_result(results)
		print results

		while (self.links[0].get_currentDepth() < int(self.config.maxDepth)):
			for child in self.links[0].get_children():
				next_node = node(self.links[0].get_url(), child, self.links[0].get_currentDepth()+1)
				self.links.append(next_node)
				time.sleep(float(self.config.speed))
				results = self.doScrape(next_node)
				#config.send_results(results)
				print results
			dummy = self.links.pop(0)
		
	def doScrape(self, current_node):
        	timeStart=datetime.datetime.now()
		if (self.config.protocol == "tor"):	# needs to be verified as the correct variable
			tor = manageTor.open()
			manageTor.torProxy()
		#must import after the above two lines are executed
        	import urllib2
        	from bs4 import BeautifulSoup

		try:
			data = urllib2.urlopen(current_node.get_url()).read()
		except:
			print "Failed to retrieve " + current_node.get_url()
			exit()
		finally:
			if (self.config.protocol == "tor"):	# needs to be verified as the correct variable
				manageTor.close(tor)
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
		

		option = "none"
		if (self.config.protocol == "tor"):
			tor = manageTor.open()
			manageTor.torProxy()
			onion=[]
			for i in fqlst:
				if ".onion" in i:
					if(option == "--dishonor_robots.txt"):
						onion.append(i)
					else:
						k = i[:29]
						k+="/robots.txt"
						rp = robotparser.RobotFileParser()
						rp.set_url(k)
						time.sleep(float(self.config.speed))
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
				if(option == "--dishonor_robots.txt"):
					weblist.append(i)
				else:
					x=i.split("/") 				# custom regex
					k=x[0]+"//"+x[2]+"/robots.txt"		# custom regex
					rp = robotparser.RobotFileParser()
					rp.set_url(k)
					time.sleep(float(self.config.speed))
					try:
						rp.read()
					except:
						print "Host unreachable: " + k
					if rp.can_fetch("*", i):
						weblist.append(i)
				
			current_node.set_children(weblist)
		timeEnd=datetime.datetime.now()
		results = [self.config, timeStart, timeEnd, current_node.get_url(), current_node.get_parent(), data]
		return results
