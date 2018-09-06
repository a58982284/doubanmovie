# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['doubanmovie.com']
    start_urls = ['http://doubanmovie.com/']

    def parse(self, response):
        pass
