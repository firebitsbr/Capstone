import hashlib


class Results:
    def __init__(self, crawlerConfig, timeStart, timeEnd, source, referrer, data):
        self.crawlerConfig = crawlerConfig
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.source = source
        self.referrer = referrer
        self.dataHash = calc_hash(data)

    def calc_hash(data):
        h = hashlib.sha256()
        h.update(data)
        return h.digest()

    " Get - Where the data was obtained"
    def get_source():
        return self.source

    " Set - Where the data was obtained"
    " ex: URL, IP, TOR onion address, etc"
    def set_source(source):
        self.source = source

    " Set - Data obtained from the crawl"
    " Hash is automatically updated"
    def set_data(data):
        self.data = data
        self.dataHash = calc_hash(data)

    " Get - Hash of the Data obtained"
    def get_dataHash():
        return self.dataHash

    " Get - Start time of the crawl"
    def get_timeStart():
        return self.timeStart

    " Set - Start time of the crawl"
    def set_timeStart(timeStart):
        self.timeStart = timeStart

    " Get - End time of the crawl"
    def get_timeEnd():
        return self.timeEnd

    " Set - End time of the crawl"
    def set_timeEnd(timeEnd):
        self.timeEnd = timeEnd

    " Get - Crawler config used to obtain this data"
    def get_crawlerConfig(crawlerConfig):
        return self.crawlerConfig

    " Set - Crawler config used to obtain this data"
    def set_crawlerConfig(crawlerConfig):
        self.crawlerConfig = crawlerConfig

    " Get - Crawler config of the previous site"
    def get_referrer():
        return self.referrer

    " Set - Crawler config of the previous site"
    def set_referrer(referrer):
        self.referrer = referrer
