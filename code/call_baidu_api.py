# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 16:11:17 2017

@author: liulo
"""

import urllib, urllib2, sys
import ssl


host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=A0nyraL7kGXrDhfDf33UyGvX&client_secret=4IGLoGQqeq8svpocetiBgzTLDlkVfhG1'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)