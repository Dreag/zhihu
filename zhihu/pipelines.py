# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
# import pymysql
import codecs

class ZhihuPipeline(object):
    def process_item(self, item, spider):
        return item

class ShipPipeline(object):
    # 自定义导出json
    def __init__(self):
        self.file = codecs.open('data2.json', 'w', encoding='utf-8')
    
    # 处理结束后关闭文件IO流
    def close_spider(self, spider):
        self.file.close()
    
    # 将Item实例导出到json文件
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item