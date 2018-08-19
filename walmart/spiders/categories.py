import scrapy


class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    allowed_domains = ['www.walmart.com']
    start_urls = ['http://www.walmart.com/']

    def parse(self, response):
        pass
