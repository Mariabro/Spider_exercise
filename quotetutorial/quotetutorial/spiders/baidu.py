# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def __init__(self, category=None, *args, **kwargs):
        super(BaiduSpider, self).__init__(*args, **kwargs)
        self.category = category  #声明为类里面的全局变量

    # def start_requests(self):
    #     yield  scrapy.Request(url='http://www.baidu.com',callback=self.parse_index)
    #
    # def make_requests_from_url(self, url):
    #     return scrapy.Request(url=url, callback=self.parse_index)

    def parse(self, response):
        # pass
        self.logger.info(self.category)

    def parse_index(self, response):
       # print('Baidu', response.status)
        self.logger.info(response.status)
