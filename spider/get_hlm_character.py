#!/usr/bin/env python
# coding:utf8

from urllib import request
from urllib.parse import quote
import  string
import time
import json
from bs4 import BeautifulSoup
import codecs
from get_character_array import get_character
import os
if not os.path.exists("./spider/images"):
		os.mkdir("./spider/images")

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

def get_json(character_arr):
	data={}
	for i in set(character_arr):
		print(i)
		url=r'https://baike.baidu.com/item/'+i
		url = quote(url, safe = string.printable)
		req = request.Request(url, headers=headers)
		response = request.urlopen(req, timeout=20)
		
		try:
			html = response.read().decode('utf-8')
			soup = BeautifulSoup(html, 'html.parser', )
			res = soup.find(class_="summary-pic")
			pic_name = str(i) + '.jpg'
			img_src = res.find('img').get('src')
			request.urlretrieve(img_src,pic_name)
		except :
			print("找不到图片")
		res_key=soup.find_all(class_ ="basicInfo-item name")
		res_val=soup.find_all(class_ ="basicInfo-item value")
		key=[ik.get_text().strip().replace("\n","、") for ik in res_key]
		value = [iv.get_text().strip().replace("\n", "、") for iv in res_val]
		item=dict(zip(key,value))
		data[str(i)]=item
	if not os.path.exists("../json"):
		os.mkdir("../json")
	f = codecs.open('../json/data.json','w','utf-8')
	f.write(json.dumps(data,  ensure_ascii=False))
if __name__ == "__main__":
	character_arr=get_character()
	os.chdir(os.path.join(os.getcwd(), './spider/images'))
	get_json(character_arr)
