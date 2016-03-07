import manageTor
#import crawlerconfig
#import results

#crawlerConfig = CrawlerConfig(location, TOR, speed, maxDepth, name)

tor = manageTor.open()

manageTor.torProxy()

import urllib2
from bs4 import BeautifulSoup

source = "http://thehiddenwiki.org"
#url = "http://3g2upl4pq6kufc4m.onion"

try:
	data = urllib2.urlopen(source).read()
finally:
	manageTor.close(tor)
soup = BeautifulSoup(data)

for a in soup.find_all('a', href=True):
	print(a['href'])
for link in soup.find_all('link', href=True):
	print(link['href'])

#report = Results(crawlerConfig, timeStart, timeEnd, source, referrer, data)
