import scrapy
from scrapy.selector import Selector


class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    start_urls = ['https://www.walmart.com/sitemap_category.xml']

    def parse(self, response):
    	response = Selector(text=response.body)

        urls = response.xpath('//url')

        for url in urls:
        	location = url.xpath('./loc/text()').extract_first()
        	last_modified = url.xpath('./lastmod/text()').extract_first()

        	yield {
        		'url': location,
        		'last_modified': last_modified,
        	}
