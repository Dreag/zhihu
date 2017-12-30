# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import json
import scrapy
from scrapy import Request
from zhihu.items import ShipItem

class RelationSpider(scrapy.Spider):
	name = "relation"
	# url = 'https://www.zhihu.com/people/ye-jia-zi-yuan/following'
	start_urls = ['http://www.zhihu.com/']
	start_user = "wang-tuan-jie-55"
	allowed_domains = ['www.zhihu.com']

	# 个人主页的json信息的url
	userinfo_url = "https://www.zhihu.com/api/v4/members/{user_name}?include={include_userinfo}"
	# 关注用户的json数据的url
	followees_url = "https://www.zhihu.com/api/v4/members/{user_name}/followees?include={include_follow}&offset={offset}&limit={limit}"
	# 粉丝用户的json数据的ur
	followers_url = "https://www.zhihu.com/api/v4/members/{user_name}/followers?include={include_follow}&offset={offset}&limit={limit}"

	# followee的url中的参数信息
	follow_para = 'data[*].answer_count, articles_count, gender, follower_count, is_followed, is_following, badge[?(type = best_answerer)].topics'
	# userinfo_url中的参数信息
	userinfo_para = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,columns_count,commercial_question_count,favorite_count,favorited_count,logs_count,included_answers_count,included_articles_count,included_text,message_thread_token,account_status,is_active,is_bind_phone,is_force_renamed,is_bind_sina,is_privacy_protected,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,is_org_createpin_white_user,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type = best_answerer)].topics'
	
	def start_requests(self):
		# 解析用户关注用户
		# yield Request(url = self.followees_url.format(user_name = self.start_user,include_follow = self.follow_para,offset = 0,limit = 20),callback = self.followees_parse)
		# 解析用户的粉丝用户
		yield Request(url = self.followers_url.format(user_name = self.start_user,include_follow = self.follow_para,offset = 0,limit = 20),callback = self.followers_parse)

	def followees_parse(self,response):
		item = ShipItem()
		
		followees_data = json.loads(response.text)
		for user in followees_data['data']:
			item['user_name'] = user['headline']
			item['url_token'] = user['url_token']
			yield item
		if "paging" in followees_data.keys() and followees_data["paging"].get("is_start") == False:
			yield Request(url = followees_data["paging"].get("previous"),callback = self.followees_parse)
		if "paging" in followees_data.keys() and followees_data["paging"].get("is_end") == False:
			yield Request(url = followees_data["paging"].get("next"),callback = self.followees_parse)


	def followers_parse(self,response):
		item = ShipItem()

		followers_data = json.loads(response.text)

		for follower in followers_data['data']:
			item['user_name'] = follower['headline']
			item['url_token'] = follower['url_token']
			print(item)
			yield item

		if "paging" in followers_data.keys() and followers_data['paging'].get('is_start') == False:
			yield Request(url = followers_data['paging'].get('previous'),callback = self.followers_parse)
		if "paging" in followers_data.keys() and followers_data['paging'].get('is_end') == False:
			yield Request(url = followers_data['paging'].get('next'),callback = self.followers_parse)