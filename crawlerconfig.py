# Crawler Configuration
# Defines what a crawler should do
# Edward Mead

class CrawlerConfig:

    def __init__(self, location, protocol, speed, maxDepth, name, depth=0):
        self.location = location   # Location to crawl
        self.protocol = protocol   # Protocol used
        self.speed = speed         # Crawls per second
        self.maxDepth = maxDepth   # Max Depth for
        self.name = name           # Name of the crawl
        self.depth = depth         # Current Depth

    # Get Location
    def get_location(self):
        return self.location

    # Get Protocol
    def get_protocol(self):
        return self.protocol

    # Get Speed
    def get_speed(self):
        return self.speed

    # Get Max Depth
    def get_maxDepth(self):
        return self.maxDepth

    # Get Name
    def get_name(self):
        return self.name

    # Get Depth
    def get_depth(self):
        return self.depth

    # Increment Current Depth
    def inc_depth(self):
        self.depth+=1;

    # Set Speed
    def set_speed(self, speed):
        self.speed = speed

    # Set Max Depth
    def set_maxDepth(self, maxDepth):
        self.maxDepth = maxDepth

    # Set Name
    def set_name(self, name):
        self.name = name

    # Set Depth
    def set_depth(self, depth):
        self.depth = depth
