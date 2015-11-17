# -*- coding: utf-8 -*-

class ProxyMiddlewar(object):
     
    # overwrite process request
    def process_request(self, request, spider):
        #set the locations request
        request.meta['proxy'] = "http://proxy.tencent.com:8080"