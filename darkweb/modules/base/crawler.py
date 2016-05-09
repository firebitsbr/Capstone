"""
Crawler
Class / Template for all crawlers to inherit
"""
from crawlerconfig import CrawlerConfig
from result import Result
import socket
import jsonpickle

class Crawler:
    name = "Default Crawler"

    """
    __init__
    Initialize config/result.
    """
    def __init__(self, config):
        self.config = config
        self.result = Result(config)

    """
    __str__
    String formatting
    """
    def __str__(self):
        return self.name

    """
    do_Crawl
    Initiate a crawl using a specific crawl config or the one used when initialized
    """
    def do_Crawl(self, config=None):
        if (config == None):
            config = self.config
        print "Not implemented exception. Do not use this class directly. It should be inherited."
        raise

    """
    send_result
    Send a result to the parser.
    Future work: Security/Authentication
    """
    def send_result(self, result):
        #send results to parser
        # @todo test when there is a destination to send data to
        # @todo later goal implement ssl?
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostname = "127.0.0.1"
        port = 4443
        print("Result type: " + str(type(result).__name__))
        if result != None and not isinstance(result, Result):
            raise Exception("Invalid Parameter: Result not Result object.")
        try:
            ser = jsonpickle.encode(result)
        except:
            print("Encode failed..." + str(result))
            return

        try:
            conn.connect((hostname, port))
            data = ser.encode('utf-8')
            conn.sendall(data)
            print("Sent all data.")
        except Exception as e:
            print("Error sending data/connecting. Error: " + str(e))
            return
        conn.close()
