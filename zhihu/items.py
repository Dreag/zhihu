# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ShipItem(scrapy.Item):
	name = scrapy.Field()
	user_link = scrapy.Field()
	focus_number = scrapy.Field()
		