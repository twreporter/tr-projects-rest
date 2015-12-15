#! /usr/bin/python

import pycurl
import json
from StringIO import StringIO

buffer = StringIO()

api = 'http://api.twreporter.org/article?max_results=40&sort=-lastPublish'
replace = [{"orig": "https://twreporter.atavist.com/view/", "new":"http://ats-dev.twreporter.org/view/"},{"orig":"https://twreporter.atavist.com/data/","new":"http://ats-dev.twreporter.org/data/"},{"orig":'href="/data/',"new":'href="http://ats-dev.twreporter.org/data/'}] 

c = pycurl.Curl()
cc = pycurl.Curl()
c.setopt(c.URL, api)
c.setopt(c.WRITEDATA, buffer)
c.perform()
result = buffer.getvalue()
records = json.loads(result, encoding="utf-8")
for i in records['_items']:
    pageBuffer = StringIO()
    fileName = i['slug']
    fo = open(fileName, "w")
    cc.setopt(cc.URL, i['url'])
    cc.setopt(cc.WRITEDATA, pageBuffer)
    cc.perform()
    body = pageBuffer.getvalue()
    # Body is a string in some encoding.
    # In Python 2, we can print it without knowing what the encoding is.
    for str_replace in replace:
        body = body.replace(str_replace['orig'], str_replace['new'])
    fo.write(body)
    fo.close()
    # print(body)

cc.close()
c.close()    


