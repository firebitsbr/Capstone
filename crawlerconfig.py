" Class for Configuring Crawlers "
" Edward Mead "

class CrawlerConfig:

    def __init__(self, location, protocol, speed, maxDepth, name):
        self.location = location
        self.protocol = protocol
        self.speed = speed
        self.maxDepth = maxDepth
        self.name = name

    def get_location():
        return self.location

    def get_protocol():
        return self.protocol

    def get_speed():
        return self.speed

    def get_maxDepth():
        return self.maxDepth

    def get_name():
        return self.name

    def set_speed(speed):
        self.speed = speed

    def set_maxDepth(maxDepth):
        self.maxDepth = maxDepth

    def set_name(name):
        self.name = name
