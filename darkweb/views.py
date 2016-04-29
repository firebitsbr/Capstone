from flask import Flask, render_template, Blueprint, request
from darkweb.modules.crawlerconfig import CrawlerConfig 
from darkweb.modules.irc import IRC
from darkweb.modules.WebCrawler import WebCrawler
import threading 
import datetime

views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def home():
	result = readSearchFile()
	return render_template("index.html", result=result)

@views.route("/", methods=["POST"])
def createCrawlerConfig():
	searchName = str(request.form['searchName'])
	protocol = str(request.form['protocol']).lower()
	speed = str(request.form['speed'])
	maxDepth = str(request.form['maxDepth'])
	location  = str(request.form['location'])
	options_input = str(request.form['options'])
	options = makeOptionsDict(options_input)
	config = CrawlerConfig(location, protocol, speed, maxDepth, searchName, options)

	msg = "Search \"" + searchName + "\" started."
	crawler = None
	search_params = None
	if searchName == "":
		msg = "Search failed. Search must be given a name."
	elif not speed.isdigit():
		msg = "Search falied. Speed much be an integer."
	elif not maxDepth.isdigit():
		msg = "Search failed. Max Crawl Depth must be an integer."
	elif protocol == "irc":
		crawler = IRC(config)
	elif protocol == "tor" or protocol == "web":
		crawler = WebCrawler(config) 
	else:
		msg = "Search failed invalid protocol.\nMust be TOR, IRC, or web"
	if(crawler):
		run_crawl(crawler)
		search_params = [("Search Name", searchName), ("Protocol", protocol), ("Speed", speed), ("Max Depth", maxDepth), ("Location", location)]
		for label, val in options.iteritems():
			search_params.append((label, val))
	result = readSearchFile()
	return render_template("index.html", msg=msg, search_params=search_params, result=result)

# read from /tmp/searches.txt and return list of lines
def readSearchFile():
	result = []
	with open("/tmp/searches.txt", "r") as f:
		for line in f:
			result.append(line)
	return result

# writes to file in /tmp the datetime a search was started
def writeSearchFile(searchName):
	with open("/tmp/searches.txt", "a") as f:
		out_string = "\"" + searchName + "\": " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n"
		f.write(out_string)
	return 
	
# run the specified cralwer 
# call do crawl in new thread 
def run_crawl(crawler, args=None):
	t = threading.Thread(target=crawler.doCrawl, args=(args, ))
	t.start()
	writeSearchFile(crawler.config.name)
	return 

# format options string from form and create options dict for crawlerconfig
# returns options dict 
def makeOptionsDict(options_input):
	options = {}
	split_input = options_input.split(',')
	for s in split_input:
		s = s.replace(" ", "")
		o = s.split(':')
		if len(o) == 2:
			options[o[0]] = o[1]
	return options



