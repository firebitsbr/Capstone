# Results Class
# Used to store the results of a Crawl
# Edward Mead
import hashlib
import sys
import base64

class Result:
    def __init__(self, crawlerConfig, timeStart = None, timeEnd = None, source = None, referrer = None, data = ""):
        self.crawlerConfig = crawlerConfig  # Crawl Configuration
        self.timeStart = timeStart          # Time of Start (DateTime.Now when Crawl starts)
        self.timeEnd = timeEnd              # Time of Completion (DateTime.Now after results are retrieved)
        self.source = source                # Location
        self.referrer = referrer            # Previous Location
        self.data = data                    # Data from Location
        self.dataBytes = 0                    # Data from Location
        self.dataHash = self.calc_hash(data)     # Hash of Data

    # Calculate Hash of some data
    def calc_hash(self, data):
        if data != None and len(data) > 0:
            h = hashlib.sha256()
            h.update(data)
            return h.hexdigest()

    # Get - Where the data was obtained
    def get_source(self):
        return self.source

    # Set - Where the data was obtained
    # ex: URL, IP, TOR onion address, etc
    def set_source(self, source):
        self.source = source

    # Get - Data obtained from the crawl
    def get_data(self):
        return self.data

    # Set - Data obtained from the crawl
    # Hash is automatically updated
    def set_data(self, data):
        self.data = data
        self.dataHash = self.calc_hash(data)
        self.dataBytes = sys.getsizeof(data)

    # Add - Data obtained from the crawl
    # Hash is automatically updated
    def add_data(self, data):
        self.data += data
        self.dataHash = self.calc_hash(data)

    # Get - Hash of the Data obtained
    def get_dataHash(self):
        return self.dataHash

    # Get - Start time of the crawl
    def get_timeStart(self):
        return self.timeStart

    # Set - Start time of the crawl
    def set_timeStart(self, timeStart):
        self.timeStart = timeStart

    # Get - End time of the crawl
    def get_timeEnd(self):
        return self.timeEnd

    # Set - End time of the crawl
    def set_timeEnd(self, timeEnd):
        self.timeEnd = timeEnd

    # Get - Crawler config used to obtain this data
    def get_crawlerConfig(self):
        return self.crawlerConfig

    # Set - Crawler config used to obtain this data
    def set_crawlerConfig(self, crawlerConfig):
        self.crawlerConfig = crawlerConfig

    # Get - Crawler config of the previous site
    def get_referrer(self):
        return self.referrer

    # Set - Crawler config of the previous site
    def set_referrer(self, referrer):
        self.referrer = referrer
