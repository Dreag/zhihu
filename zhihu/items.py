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
	id = scrapy.Field()
	name = scrapy.Field()
	url_token = scrapy.Field()
	user_type = scrapy.Field()
	answer_count = scrapy.Field()
	articles_count = scrapy.Field()
	follower_count = scrapy.Field()