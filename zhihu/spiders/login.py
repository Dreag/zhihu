# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from bs4 import BeautifulSoup
import requests
import time
from http import cookiejar
from pytesseract import *
from PIL import Image

from zhihu.items import ShipItem

class RelationSpider(scrapy.Spider):
	name = "relation"

		# 使用登录cookie信息
	session = requests.session()
	session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
	try:
	    print(session.cookies)
	    session.cookies.load(ignore_discard=True)
	except:
	    print("还没有cookie信息")

	#获取xsrf
	def get_xsrf():
	    response = session.get("https://www.zhihu.com", headers=headers)
	    soup = BeautifulSoup(response.content, "html.parser")
	    xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
	    return xsrf

	#获取验证码
	def get_captcha():

	    """
	    把验证码图片保存到当前目录，手动识别验证码
	    :return:
	    """
	    t = str(int(time.time() * 1000))
	    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
	    r = session.get(captcha_url, headers=headers)
	    with open('captcha.jpg', 'wb') as f:
	        f.write(r.content)
	    # im = Image.open("captcha.jpg")
	    # captcha = image_to_string(im)
	    # print(captcha)
	    captcha = input("验证码：")
	    return captcha


	def login(phone_num, password):
	    login_url = 'https://www.zhihu.com/login/phone_num'
	    data = {
	        'phone_num': phone_num,
	        'password': password,
	        '_xsrf': get_xsrf(),
	        "captcha": get_captcha(),
	        'remember_me': 'true'
	        }
	    response = session.post(login_url, data=data, headers=headers)
	    login_code = response.json()
	    print(login_code['msg'])
	    #for i in session.cookies:
	     #   print(i)
	    session.cookies.save()


	if __name__ == '__main__':
	    phone_num = "15237107089"
	    password = "gy.970802..zh"
	    login(phone_num, password)