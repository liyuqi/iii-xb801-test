#!/usr/bin/env python
#coding=utf-8

import csv,json
import urllib, urllib2
import traceback
import threading
import sys,re,os
from lxml import etree

def read_file_FBurl():
    
    #中文版 windows python2.7 '取csv網址'
    fileReader_name = raw_input()#'2013-07-post.csv'#.decode('utf-8')
    f = open(fileReader_name,'rb')
    fileWriter_name = fileReader_name+'.txt'
    w = csv.writer(open(fileWriter_name, "wb"))

    print 'start'
    for row in csv.DictReader(f):
        
        if(row['類型']=='連結'):
            FB_ID  = row['文章編號']
            FB_url = row['靜態連結']
            Pan_url = get_post_url(FB_url)
            Pan_tag = store_post_tags(Pan_url)
            #print FB_url
            try:
                cat_text = ','.join(Pan_tag[0])
                #tag_text = ','.join(Pan_tag[1])
                #print FB_uri,'\t',Pan_uri,'\t',cat_text.encode('utf8'),'\t',tag_text.encode('utf8'),'\n'
                w.writerow([FB_ID,FB_url,Pan_url,cat_text.encode('utf8')])#,tag_text.encode('utf8')
                #w.writerow([FB_uri,Pan_uri,cat_text,tag_text])#no encode() 亂碼
            except:
                pass #找不到url,tag

def get_post_url(FB_url):
        #print 'mapping網址 re版'
        content = urllib2.urlopen(FB_url).read()
        #print content
        pattern = re.compile('<a class="_5rwn".*?.*?>')
        atag = re.findall(pattern, content)
        text = urllib.unquote(str(atag)).decode('utf8')
        #print text
        urls = re.findall(r'href=[\'"]?([^\'" >]+archives/.{5})', text)
        text2=urllib.unquote(str(urls))

        #print text2[35:len(text2)-2]
        return text2[35:len(text2)-2]#FB parse PanSci 網址

def store_post_tags(FB_href):
    try:
        f = urllib2.urlopen(FB_href)
        
        parser = etree.HTMLParser()
        tree = etree.parse(f, parser)
        cells = tree.xpath('//ul[@class="post-categories"]/li/a')#cat分類xpath
        cells2 = tree.xpath('//ul[@class="post-tags"]/li/a')#tag標籤xpath
        cat = []
        tag = []
        post = [cat,tag]
        for line in cells:
                tag_text = line.text
                cat.append(tag_text) #人體解析 植物王國 生命奧祕
        for line2 in cells2:
                tag_text2 = line2.text
                tag.append(tag_text2)
        return post
    except:
        return ''

def code_test():
    msg = u'今天天氣真好'
    encoded = msg.encode('utf8')
    print repr(encoded)
    print encoded
    print encoded.decode('utf8')
    
if __name__ == '__main__':
    #dic_test()
    #code_test()
    read_file_FBurl()
    print 'done'


    
    
