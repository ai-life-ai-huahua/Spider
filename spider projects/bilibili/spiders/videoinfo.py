# -*- coding: utf-8 -*-
import scrapy
import json
import time



class VideoinfoSpider(scrapy.Spider):
    name = 'videoinfo'
    allowed_domains = ['bilibili.com']
    # start_urls = ['http://bilibili.com/']
    def start_requests(self):
        for i in range(1,839):
            url = 'https://www.bilibili.com/list/rank-27.html?spm_id_from=333.5.b_646f7567615f6f74686572.28#!page='+str(i)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        print('success')
        for e in json.loads(response.body.decode('utf-8'))["exp_list"]["result"]:
            print(e)
        time.sleep(10)

