# -*- coding: utf-8 -*-

# Scrapy settings for News_Scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'News_Scrapy'
SPIDER_MODULES = ['News_Scrapy.spiders']
NEWSPIDER_MODULE = 'News_Scrapy.spiders'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'News_Scrapy (+http://www.yourdomain.com)'
ITEM_PIPELINES={
    'News_Scrapy.pipelines.NewsScrapyPipeline':300, # 这个是用来定义调用这个方法的优先级
    #此处可以写多个数据存储的文件，同时这个是一个分布式类似的存储机制
}
# 定义日志存储的级别和形式
LOG_LEVEL='DEBUG'
# 毕竟我们这个是web爬虫，时间长了，会被服务器发现，因此进行一些简单的伪装
# 若想彻底的骗过服务器，需要自己控制一些公网IP地址，进行轮训式抓取
DOWNLOAD_DELAY = 2 
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'python'
MONGODB_COLLECTION = 'test'
BOT_NAME = 'News_Scrapy'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'News_Scrapy (+http://www.yourdomain.com)'
