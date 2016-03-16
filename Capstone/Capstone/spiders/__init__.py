# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import urlparse
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import Spider
BASE_URL = 'http://www.target_site.com/'

class MySpider(Spider):
    name = 'spiderName'
    allowed_domains = ['target_site.com']
    start_urls = ['http://www.target_site.com/test1',
			'http://www.target_site.com/test2']
def parse(self, response):
    sel = Selector(response)
    requests = []
    for link in sel.xpath('//ul/li/a]'):
        name = link.xpath('text()')[0].extract().strip()
        url = link.xpath('@href')[0].extract().strip()
        requests.append(Request(
            url=urlparse.urljoin(BASE_URL, url), callback=parse_subcategory))
        return requests

def parse_items (self, response):
    sel = Selector(response)
    requests = []
    try:
        price = sel.xpath('//ul/li/text()')[0].extract().strip().split(u'€')
        except IndexError:
            price = sel.xpath('//a/text()"]')[0].extract().strip().split(u'€')
    
    item = ProductsItem(
        url= sel.xpath('//a[@class="url"]/@href')[0].extract().strip()[1],
        website=self.name,
        name=sel.xpath('//h1[@class="headline"]/text()')[0].extract().strip(),
        description=sel.xpath('//div[@class="description"]').extract().strip(),
        price=price,
        currency=u'euro',
        images_urls=[urlparse.urljoin(BASE_URL,x.strip()) for x in
            sel.xpath('//div[@id="id"]/img/@src').extract()]
        )
    return [item] 