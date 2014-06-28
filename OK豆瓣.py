#!/usr/bin/python
# coding: utf-8
 
import sys
import os
import subprocess
import getopt
import time
import json
import urllib
import urllib2
import getpass
import ConfigParser
from cookielib import CookieJar

def save(filename, content):
     file = open(filename, 'wb')
     file.write(content)
     file.close()

def login(username, password):
     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))
     while True:
         print '正在获取验证码……'
         captcha_id = opener.open(urllib2.Request(
             'http://douban.fm/j/new_captcha')).read().strip('"')
         save(
             '1.jpg',
             opener.open(urllib2.Request(
                 'http://douban.fm/misc/captcha?size=m&id=' + captcha_id
             )).read())
         captcha = raw_input('验证码: ')
         print '正在登录……'
         response = json.loads(opener.open(
             urllib2.Request('http://douban.fm/j/login'),
             urllib.urlencode({
                 'source': 'radio',
                 'alias': username,
                 'form_password': password,
                 'captcha_solution': captcha,
                 'captcha_id': captcha_id,
                 'task': 'sync_channel_list'})).read())
         if 'err_msg' in response.keys():
             print response['err_msg']
         else:
             print 'OK'
             return opener


login('wingerted', 'evil.325118')
