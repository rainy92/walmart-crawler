import json
import scrapy


class ListingSpider(scrapy.Spider):
	name = 'listing'
	start_urls = ['https://www.walmart.com/search/api/preso?cat_id=4171_14521&prg=desktop']

	def parse(self, response):
		data = json.loads(response.body)

		items = data['items']
		
		if not response.meta.get('is_pagination_done', False):
			total_pages = data['requestContext']['itemCount']['total'] / data['requestContext']['itemCount']['currentSize']

			for page in range(2, total_pages + 1):
				yield scrapy.Request(
					'https://www.walmart.com/search/api/preso?cat_id=4171_14521&prg=desktop&page=%s' % page, 
					meta={ 'is_pagination_done': True })

		for item in items:
			yield item
