#!/usr/bin/python

import json
import urllib2
import urllib
import traceback
import threading
from lxml import etree

fan_url = 'https://www.facebook.com/PanSci'
test_url = 'https://www.facebook.com/PanSci/posts/10202281683458386'
fb_url = 'https://www.facebook.com'
Pan_url = ''
RESULT = {}
NOT_FOUND = []

def get_like_id():
	ret = []
	f = urllib2.urlopen(test_url)
	parser = etree.HTMLParser()
	tree = etree.parse(f, parser)
	cells = tree.xpath('//a[@class="_5rwn"]')
    
	for line in cells:
		print("1hello")
		Pan_url = line.xpath('@href').text
		print("2hello")
		print(Pan_url) #http://pansci.tw/archives/56822
	#return Pan_url
    
if __name__ == '__main__':
    get_like_id() 
