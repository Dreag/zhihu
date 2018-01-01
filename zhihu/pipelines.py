# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
import codecs

class ZhihuPipeline(object):
    def process_item(self, item, spider):
        return item

class ShipPipeline(object):
    # 自定义导出json
    def __init__(self):
        self.file = codecs.open('relation.json', 'w', encoding='utf-8')
    
    # 处理结束后关闭文件IO流
    def close_spider(self, spider):
        self.file.close()
    
    # 将Item实例导出到json文件
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item



class DatabasePipeline(object):
    """docstring for DatabasePipeline"""
    def __init__(self):
        self.conn = pymysql.connect(host = 'localhost',port = 3306,user = 'root',passwd = 'passwd',db = 'zhihu',charset = 'utf8')
        self.cursor = self.conn.cursor()
        # truncate为数据库删除操作
        # self.cursor.execute("truncate table people_inform")
        print("连接成功")
        self.conn.commit()


    def process_item(self, item, spider):
        sql = 'insert into people_inform(id,name,url_token,user_type,answer_count,articles_count,follower_count) values (%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql,(item['id'],item['name'],item['url_token'],item['user_type'],item['answer_count'],item['articles_count'],item['follower_count']))
            self.conn.commit()
        except pymysql.Error:
            print("error,DatabasePipeline.")
        return item