#!/usr/bin/env python
# coding=utf-8
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from News_Scrapy.items import NewsScrapyItem
class NetEaseSpider(CrawlSpider):
    name = "News_Scrapy"
    allowed_domains = ["www.thepaper.cn"]
    start_urls = ["http://www.thepaper.cn/"]
    rules = [
        Rule(SgmlLinkExtractor(allow=(r'http://www.thepaper.cn/channel_2595[0-9]'))),
        Rule(SgmlLinkExtractor(allow=(r'http://www.thepaper.cn/newsDetail_forward_[0-9]+')),callback="parse_item"),
    ]
    def parse_item(self,response):
        sel_resp = Selector(response)
        news_item = NewsScrapyItem()
        news_item["news_type"] = sel_resp.xpath('//*[@id="select"]/text()').extract()
        news_item["news_title"] = sel_resp.xpath('/html/body/div[3]/div[1]/div[1]/h1/text()').extract()
        news_item["news_date"] = sel_resp.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/p[2]').re(r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}')
        news_item["news_source"] = sel_resp.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/p[2]/a/text()').extract()
        news_item["news_content"] = sel_resp.xpath('/html/body/div[3]/div[1]/div[1]/div[4]/text()').extract()
        return news_item
