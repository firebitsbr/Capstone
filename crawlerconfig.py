# Crawler Configuration
# Defines what a crawler should do
# Edward Mead

class CrawlerConfig:

    def __init__(self, location, protocol, speed, maxDepth, name, options=dict(), depth=0):
        self.location = location   # Location to crawl
        self.protocol = protocol   # Protocol used
        self.speed = speed         # Crawls per second
        self.maxDepth = maxDepth   # Max Depth for
        self.name = name           # Name of the crawl
        self.options = options     # Crawler Specific options
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

    # Set Speed
    def set_speed(self, speed):
        self.speed = speed

    # Get Max Depth
    def get_maxDepth(self):
        return self.maxDepth

    # Set Max Depth
    def set_maxDepth(self, maxDepth):
        self.maxDepth = maxDepth

    # Get Name
    def get_name(self):
        return self.name

    # Set Name
    def set_name(self, name):
        self.name = name

    # Get Options
    def get_options(self):
        return self.options

    # Set Options
    def set_options(self, options):
        self.options = options

    # Add Option
    def add_option(self, option, value):
        self.options[option] = value

    # Get Depth
    def get_depth(self):
        return self.depth

    # Set Depth
    def set_depth(self, depth):
        self.depth = depth

    # Increment Current Depth
    def inc_depth(self):
        self.depth+=1;
