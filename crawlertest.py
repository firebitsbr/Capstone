# TestCrawler
# Unit test for Crawler class
# Edward Mead
from crawler import Crawler
from crawlerconfig import CrawlerConfig
from WebCrawler import WebCrawler

class TestCrawler(Crawler):
    name = "Test Crawler"

    def do_Crawl(self):
        print "Test Crawler - do_Crawl"

    def send_result(self):
        print "Test Crawler - send_result"


conf = CrawlerConfig("http://3g2upl4pq6kufc4m.onion/", "tor", "0", "1", "testCrawl")
t = TestCrawler(conf)
test = WebCrawler(conf)
test.doCrawl()

# Test Gets
print t.get_crawl_config()
print t.get_crawl_location()
print t.get_crawl_protocol()
print t.get_crawl_speed()
print t.get_crawl_maxDepth()
print t.get_crawl_name()
print t.get_crawl_depth()
print t.get_crawl_options()
print t.get_result()
print t.get_result_data()
print t.get_result_dataHash()
print t.get_result_source()
print t.get_result_timeStart()
print t.get_result_timeEnd()
print t.get_result_crawlerConfig()
print t.get_result_referrer()

# Test Sets / Adds / Incs
newconf = CrawlerConfig("some new website", "Some new protocol", "<new Speed>", "<new depth>", "<new Name>")
t.set_crawl_speed(1)
t.set_crawl_maxDepth(1)
t.set_crawl_name("crawl name")
t.set_crawl_depth(1)
t.add_crawl_option("key","value")
t.set_result_source("result source")
t.set_result_data("result data")
t.set_result_timeStart("result timeStart")
t.set_result_timeEnd("result timeEnd")
t.set_result_crawlerConfig(conf)
t.set_result_referrer("result referrer")
t.add_result_data("add result data")
t.inc_crawl_depth()
t.send_result()

# Test Gets (After sets)
print t.get_crawl_config()
print t.get_crawl_location()
print t.get_crawl_protocol()
print t.get_crawl_speed()
print t.get_crawl_maxDepth()
print t.get_crawl_name()
print t.get_crawl_depth()
print t.get_crawl_options()
print t.get_result()
print t.get_result_data()
print t.get_result_dataHash()
print t.get_result_source()
print t.get_result_timeStart()
print t.get_result_timeEnd()
print t.get_result_crawlerConfig()
print t.get_result_referrer()

