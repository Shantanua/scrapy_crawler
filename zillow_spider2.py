
# coding: utf-8

# In[ ]:




# In[ ]:

from __future__ import absolute_import
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from zillow.items import zillowItem


class nzillowpider(CrawlSpider):
    name = "zillow_s2"
    allowed_domains = ["www.zillow.com"]
    start_urls = ['http://www.zillow.com/homedetails/855-Peachtree-St-NE-UNIT-2712-Atlanta-GA-30308/92192336_zpid']
    x = 0
#zsg-list_square zsg-lg-1-3 zsg-md-1-2 zsg-sm-1-1

    def parse(self, response):
        #links1 = Selector(response=response).xpath('//ul[@class = "zsg-list_square zsg-lg-1-3 zsg-md-1-2 zsg-sm-1-1"]')
        links2 = Selector(response=response).xpath('//div[@id="hdp-tax-history"]')
        print 'Jamba Juice!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        #print links
        """for link in links1:
            #print response
            item = zillowItem()
            item['link'] = link.xpath('@href').extract()
            item['title'] = link.xpath('li/text()').extract()
            item['z_id'] = link.xpath('@id').extract()
            #print item['link'], item['title']
            yield item"""
        print links2
        for link in links2:
            print link
            #print response
            item = zillowItem()
            item['link'] = link.xpath('@href').extract()
            item['title'] = link.xpath('/section').extract()
            item['z_id'] = link.xpath('@id').extract()
            print item['link'], item['title']
            yield item
            
        print 'Jamba Juice!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    
