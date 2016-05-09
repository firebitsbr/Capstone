from manageTor import manageTor                                                	# only used for Tor
from node import node                                                          	# used to tie referred and max depth to a specific link
from darkweb.modules.base.crawlerconfig import CrawlerConfig    	       	# base configuration class
from darkweb.modules.base.crawler import Crawler                               	# base crawler class
from darkweb.modules.base.result import *				       	# result class to send results to the parser
import robotparser							       	# method to honor robots.txt files
import datetime								       	# method used for cralwer start and end dates
import time                                                                    	# method used to manage delay of the crawler
import re								       	# regex used in web link managing
from urlparse import urljoin						       	# method used to allow for parsing of local links within a web directory



class WebCrawler(Crawler):
        mtor=None								# initializes the tor object for the crawl

	# When the WebCrawler is initialized, it is given a configuration based on the base Crawler class.
	# It also initializes variables for itself and (if robots option is not specified) will always honor robots.txt files
     
	def __init__(self, config, robots="True"):
                self.config = config
                self.links = []							# the "links" list holds all of the node class objects to scrape 
		self.history = []						# the "history" list holds all of the links scraped to ensure the absence of scraping loops
                if "robots" in config.options.keys():				# the "robots" flag allows for the dishonor of robots.txt files if specified
                        self.robots = config.options["robots"]
                else:
                        self.robots = None

	# The "doCrawl" function facilitates the entire crawl. It creates an initial node using the configuration given by the 
	# class call. Every time a new node is created, it is appended onto the "links" list of objects to crawl. New nodes are 
	# created by determining the children of the previous node (children are indicated in the node class) and only if the max 
	# depth specified has not yet been reached. After a new node is created, the function "doScrape" is called which returns a 
	# results object. If this object exists, it will send it to the parser by calling "send_result". When the results object 
	# returned from "doScrape" is NULL (if the web page was not accessible), nothing is sent to the parser. Before each node 
	# is scraped, the delay timer occurs to prevent overloading the network.

        def doCrawl(self):
                initial_node = node(None, self.config.location, 1)
                self.links.append(initial_node)

                results = self.doScrape(initial_node)
                if results != "NULL":
                        self.send_result(results)

                while (self.links[0].get_currentDepth() < int(self.config.maxDepth)):
                        for child in self.links[0].get_children():
                                next_node = node(self.links[0].get_url(), child, self.links[0].get_currentDepth()+1)
                                self.links.append(next_node)
                                time.sleep(float(self.config.speed))
                                results = self.doScrape(next_node)
                                if results != "NULL":
                                        self.send_result(results)
                        dummy = self.links.pop(0)

	# The "doScrape" function scrapes an individual web/tor page. It uses the give node to find it page to scrape. When the is
	# called, "timeStart" is set. If the protocol is tor, a tor proxy is opened. The url is first checked against the history of
	# scraped urls to ensure that loops are not created. Then, "doScrape" will attempt to connect and read the html from the page
	# if it is accessbile. If not, it will fail and return a NULL results value. Once the html has been read, it is placed in a
	# Beautiful Soup object and (as long as max depth is not met) will find all of the links on the page. Due to the different
	# types of links on a page, the "fqlst" list is created and used to create a full link for each of the links on the page.
	# This fixes the issue of local links. Next, if robots.txt files are being honored in the crawl, all of the links in the list
	# will be matched against the corresponding robots.txt files to determine if they are crawlable. If not, these links are removed
	# from the list of links to crawl. Once that is complete, the "timeEnd" variable is set and the result object is compiled and sent
	# back to "doCrawl" for processing.

        def doScrape(self, current_node):
                timeStart=datetime.datetime.now()
                if (self.config.protocol == "tor"):
                        mtor = manageTor()
                        tor = mtor.open()
                        mtor.torProxy()
                #must import after tor is created as sockets are changed
                import urllib2
                from bs4 import BeautifulSoup
		
		if current_node.get_url() not in self.history:
			self.history.append(current_node.get_url())
		else:
			return "NULL"

                try:
                        data = urllib2.urlopen(current_node.get_url()).read()
                except:
                        print "Failed to retrieve " + current_node.get_url()
                        return "NULL"
                finally:
                        if (self.config.protocol == "tor"):     # needs to be verified as the correct variable
                                mtor.close(tor)
                soup = BeautifulSoup(data)

                if(current_node.get_currentDepth() < int(self.config.maxDepth)):

                        lst=[]

                        for a in soup.find_all('a', href=True):
                                lst.append(a['href'])
                        for b in soup.find_all('link', href=True):
                                lst.append(b['href'])
                        fqlst=[]                                                # fully qualified list
                        for n in lst:
                                if not n.startswith("http"):
                                        fqlst.append(urljoin(current_node.get_url(), n))
                                else:
                                        fqlst.append(n)


                        if (self.config.protocol == "tor"):
                                tor = mtor.open()
                                mtor.torProxy()
                                onion=[]
                                for i in fqlst:
                                        if ".onion" in i:
                                                if(self.robots==None):
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
                                mtor.close(tor)
                                current_node.set_children(onion)
                        else:
                                weblist=[]
                                for i in fqlst:
                                        if(self.robots==None):
                                                weblist.append(i)
                                        else:
                                                x=i.split("/")                          # custom regex
                                                k=x[0]+"//"+x[2]+"/robots.txt"          # custom regex
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

                import urllib2
                from bs4 import BeautifulSoup
                timeEnd=datetime.datetime.now()
                result = Result(self.config, timeStart, timeEnd, current_node.get_url(), current_node.get_parent(), data)
                print("Result Created. Type: " + type(result).__name__)
                print("Result Created. Object: " + str(result))
                return result
