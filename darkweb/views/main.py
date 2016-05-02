#from flask import Flask, render_template, Blueprint, request, g
from flask import Flask, render_template, request, g
from darkweb.modules.base.crawlerconfig import CrawlerConfig
from darkweb.modules.irc.irc import IRC
from darkweb.modules.web.WebCrawler import WebCrawler
from darkweb.modules.parser.parser import parser
import SocketServer
import threading
import datetime
import sys
from threading import Thread
from darkweb import app
#views = Blueprint("views", __name__)

@app.before_first_request
def before_first():
    print("views.py - init start")
    HOST, PORT = "0.0.0.0", 4443
    sserver = SocketServer.ThreadingTCPServer((HOST, PORT), parser)
    Thread(target=sserver.serve_forever).start()
    print("views.py - init end")

@app.route("/addParams", methods=["POST"])
def addParams():
    # add new param
    if request.form['addST']:
        print("Adding searchterm")
        # add new search term
    if request.form['addRE']:
        print("Adding regularexpression")
        # add new regex
    result = readSearchFile()
    msg = "Successfull added search parameters"
    return render_template("index.html", result=result)

@app.route("/clearParams", methods=["POST"])
def clearParams():
    # clear all params
    result = readSearchFile()
    msg = "Successfull cleared search parameters"
    return render_template("index.html", result=result)

@app.route("/", methods=["GET"])
def home():
    result = readSearchFile()
    return render_template("index.html", result=result)

@app.route("/", methods=["POST"])
def createCrawlerConfig():
    print(str(request.form))
    print("Post recieved.")
    searchName = str(request.form['searchName'])
    protocol = str(request.form['protocol']).lower()
    print("Post parameters parsed.")
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
    elif location == "":
        msg = "Search failed. Must give a search location."
    elif protocol == "irc":
        crawler = IRC(config)
    elif protocol == "tor" or protocol == "web":
        if not speed.isdigit():
            msg = "Search falied. Speed much be an integer."
        elif not maxDepth.isdigit():
            msg = "Search failed. Max Crawl Depth must be an integer."
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

# read from /tmp/searches.txt and return list of 5 lines
def readSearchFile():
    result = []
    i = 0
    with open("/tmp/searches.txt", "r") as f:
        for line in f:
            if(i >= 5):
                break
            result.append(line)
            i += 1
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
    #t = threading.Thread(target=crawler.doCrawl, args=(args, ))
    t = threading.Thread(target=crawler.doCrawl)
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



