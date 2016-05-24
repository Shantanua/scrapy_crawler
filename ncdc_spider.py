
# coding: utf-8

# In[ ]:

from __future__ import absolute_import
import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from ncdc.items import NcdcItem


class ncdcSpider(scrapy.Spider):
    name = "ncdc1"
    allowed_domains = ["http://www.ncdc.noaa.gov/"]
    start_urls = ['http://www.ncdc.noaa.gov/qclcd/QCLCD?prior=N']

    def parse(self, response):
        links = Selector(response=response).xpath('//li')
        for link in links:
            item = NcdcItem()
            item['link'] = link.xpath('font/a/@href').extract()
            item['title'] = link.xpath('font/a/text()').extract()
            item['desc'] = link.xpath('font/text()').extract()
            yield item
        