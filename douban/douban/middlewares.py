#!/usr/bin/env python
#coding:utf-8

import random
import base64
from scrapy.conf import settings
from douban.settings import USER_AGENTS
from douban.settings import PROXIES

#随机的User-Agent
class RandomUserAgent(object):
    def process_request(self,request,spider):
        useragent = random.choice(USER_AGENTS)
        #proxy = random.choice(PROXIES)
        request.headers.setdefault("User-Agent",useragent)

    def RandomProxy(self,request,spider):
        proxy = random.choice(PROXIES)

        if proxy['user_passwd'] is None:
            # 没有代理账户验证的代理使用方式
            request.meta['proxy'] = "http://" + proxy['ip_port']

        else:
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
            request.headers['proxy-Authorization'] = 'Basic' + base64_userpasswd
            request.meta['proxy'] = "http://" + proxy['ip_port']
