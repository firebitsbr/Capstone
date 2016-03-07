import urlparse
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import Spider
BASE_URL = 'http://www.target_site.com/' 
								# Change URL to a new default
								# Could be grabbed from the initialization file
# More details will be put in when all code is available and linking it together is more clear

class MySpider(Spider):
	name = 'spiderName'
	allowed_domains = ['target_site.com']
	start_urls = ['http://www.target_site.com/test1',
		'http://www.target_site.com/test2'] 

def doCrawl(): 					# Crawls

								# base on http://www.devx.com/webdev/build-a-python-web-crawler-with-scrapy.html
								
def setSpeed():					# Speed
								# this can be set here, however, it should just be a method to 
								# grab data from the configuration
def init():						# Configuration
	settings=crawler.settings	# will fill in once I see what items I need to grab from the configuration, preferably passed as a class
	if settings['LOG_ENABLED']
		print "log enabled"		# can add other prints and conditionals based on our settings
								# Based on settings here: http://doc.scrapy.org/en/latest/topics/settings.html
def getStatus():		# Status Printoff
	# will need to see more code to fill the blanks in
def getStatistics():	# Return Status Printoff
	# will need to see more code to fill the blanks in


