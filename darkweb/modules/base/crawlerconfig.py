"""
crawlerconfig.py
Defines what a crawler should do
"""

class CrawlerConfig:

    def __init__(self, location, protocol, speed, maxDepth, name, options=dict(), depth=0):
        self.location = location   # Location to crawl
        self.protocol = protocol   # Protocol used
        self.speed = speed         # Crawls per second
        self.maxDepth = maxDepth   # Max Depth for
        self.name = name           # Name of the crawl
        self.options = options     # Crawler Specific options
        self.depth = depth         # Current Depth

    # Increment Current Depth
    def inc_depth(self):
        self.depth+=1;
