from flask import Flask, render_template, Blueprint, request
from darkweb.modules.crawlerconfig import CrawlerConfig 
from darkweb.modules.irc import IRC
from darkweb.modules.WebCrawler import WebCrawler
import threading 

views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def home():
	return render_template("index.html")

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
	return render_template("index.html", msg=msg)

# run the specified cralwer 
# call do crawl in new thread 
def run_crawl(crawler, args=None):
	t = threading.Thread(target=crawler.doCrawl, args=(args, ))
	t.start()
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



