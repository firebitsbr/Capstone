# Crawler
# Class / Template for all crawlers to inherit
# Edward Mead
from crawlerconfig import CrawlerConfig
from result import Result

class Crawler:
    name = "Default Crawler"

    def __init__(self, config):
        self.config = config
        self.result = Result(config)

    # String
    def __str__(self):
        return self.name

    # Initiate a crawl using a specific crawl config or the one used when initialized
    def do_Crawl(self, config=None):
        if (config == None):
            config = self.config
        print "Not implemented exception. Do not use this class directly. It should be inherited."
        raise

    # Get - Crawl Config object
    def get_crawl_config(self):
        return self.config

    # Get - Crawl location
    def get_crawl_location(self):
        return self.config.get_location()

    # Get - Crawl protocol
    def get_crawl_protocol(self):
        return self.config.get_protocol()

    # Get - Crawl speed
    def get_crawl_speed(self):
        return self.config.get_speed()

    # Get - Crawl max depth
    def get_crawl_maxDepth(self):
        return self.config.get_maxDepth()

    # Get - Crawl name
    def get_crawl_name(self):
        return self.config.get_name()

    # Get - Crawl depth
    def get_crawl_depth(self):
        return self.config.get_depth()

    # Inc - Crawl Depth + 1
    def inc_crawl_depth(self):
        self.config.inc_depth()

    # Set - Crawl speed
    def set_crawl_speed(self, speed):
        self.config.set_speed(speed)

    # Set - Crawl max depth
    def set_crawl_maxDepth(self, maxDepth):
        self.config.set_maxDepth(maxDepth)

    # Set - Crawl name
    def set_crawl_name(self, name):
        self.config.set_name(name)

    # Set - Crawl depth
    def set_crawl_depth(self, depth):
        self.config.set_depth(depth)

    # Get - Crawl Option
    def get_crawl_options(self):
        return self.config.get_options()

    # Add - Crawl Option
    # Option = key value pair <"Option", True/False>
    def add_crawl_option(self, option, value):
        return self.config.add_option(option, value)

    # Get - Result object
    def get_result(self):
        return self.result

    # Get - Result data hash
    # Get the current hash of the data
    def get_result_dataHash(self):
        return self.result.get_dataHash()

    # Get - Result source
    def get_result_source(self):
        return self.result.get_source()

    # Set - Result source
    def set_result_source(self, source):
        self.result.set_source(source)

    # Get - Result data
    def get_result_data(self):
        return self.result.get_data()

    # Set - Result data
    def set_result_data(self, data):
        self.result.set_data(data)

    # Add - Result data
    def add_result_data(self, data):
        self.result.add_data(data)

    # Get - Result time start
    def get_result_timeStart(self):
        return self.result.get_timeStart()

    # Set - Result time start
    def set_result_timeStart(self, timeStart):
        self.result.set_timeStart(timeStart)

    # Get - Result time end
    def get_result_timeEnd(self):
        return self.result.get_timeEnd()

    # Set - Result time end
    def set_result_timeEnd(self, timeEnd):
        self.result.set_timeEnd(timeEnd)

    # Get - Result Crawler Configuration
    def get_result_crawlerConfig(self):
        return self.result.get_crawlerConfig()

    # Set - Result Crawler Configuration
    def set_result_crawlerConfig(self, crawlerConfig):
        self.result.set_crawlerConfig(crawlerConfig)

    # Get - Result Referrer
    def get_result_referrer(self):
        return self.result.get_referrer()

    # Set - Result Referrer
    def set_result_referrer(self, referrer):
        self.result.set_referrer(referrer)

    def send_result(self, result):
        # @todo send results to ELK
        print "send_result - Result: " + result
        print "Not implemented exception. To be added later."
        raise
