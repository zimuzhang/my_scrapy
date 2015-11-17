# -*- coding: utf-8 -*-
import scrapy

class DoubanScrapy(scrapy.Spider):
    name = 'DoubanScrapy'
    allowed_domains = ['douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, reponse):
        with open('test.txt', 'wb') as f:
            f.write(reponse.body)