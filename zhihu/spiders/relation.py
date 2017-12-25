# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

from zhihu.items import ShipItem

class RelationSpider(scrapy.Spider):


	name = "relation"
	url = 'https://www.zhihu.com'
	start_urls = ['https://www.zhihu.com/people/ye-jia-zi-yuan/following']
	# allowed_domains = ['zhihu.com']

	def parse(self,response):
		item = ShipItem()
		selector = scrapy.Selector(response)
		peoples = selector.xpath('//h2[@class="ContentItem-title"]')
		print(peoples)
		for people in peoples:
			# 提取昵称
			name = people.xpath('//a[@class="UserLink-link"]/text()')
			# 提取用户的主页地址
			link = people.xpath('//a[@class="UserLink-link"]/text()')
			item['name'] = name
			item['user_link'] = link
			print(str(name) + "  " + str(link))
		yield item
		# 获取下一页
		nextPage = selector.xpath('div[@class="Pagination"]')
		for pagenum in range(len(nextPage))[2:-1]:
			print(self.start_urls + "?page=" + str(pagenum))
			yield scrapy.Request(self.start_urls + "?page=" + str(pagenum),callback=self.parse)