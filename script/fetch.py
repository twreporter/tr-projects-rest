#! /usr/bin/python
from datetime import datetime
import logging
import pycurl
import json
from StringIO import StringIO

_time = datetime.now().strftime("%Y-%m-%d %H:%M");
logging.basicConfig(filename='/var/log/fetch-' + _time + '.log',level=logging.INFO)

logging.info('fetch articles from atavist')

buffer = StringIO()

api = 'http://api.twreporter.org/article?max_results=40&sort=-lastPublish'
target_folder = '/tmp/twreporters/articles/'

logging.info('api: %s ', api);
replace = [{
            "orig": "https://twreporter.atavist.com/view/", 
            "new":"https://www.twreporter.org/view/"
        },{
            "orig": "https://twreporter.atavist.com/data/",
            "new":"https://www.twreporter.org/data/"
        },{
            "orig":'href="/data/',
            "new":'href="https://www.twreporter.org/data/'
        },{
            "orig": "atavist.com/data/files/organization/60826/", 
            "new": "www.twreporter.org/data/files/organization/60826/"
        }, {
            "orig": "dh1rvgpokacch.cloudfront.net/atavist/60826", 
            "new": "www.twreporter.org/data/files/organization/60826"
        }, {
            "orig": "src=\"/data/files/organization/60826/image/derivative/cropandscale~64x64~favicon-1450079771-87.png",
            "new": "src=\"https://www.twreporter.org/data/files/organization/60826/data/files/organization/60826/image/derivative/cropandscale~64x64~favicon-1450079771-87.png"
        }] 

c = pycurl.Curl()
cc = pycurl.Curl()
c.setopt(c.URL, api)
c.setopt(c.WRITEDATA, buffer)
c.perform()
result = buffer.getvalue()
records = json.loads(result, encoding="utf-8")

logging.debug('records from api: %s', json.dumps(records));

for i in records['_items']:
    pageBuffer = StringIO()
    fileName = i['slug']
    logging.info('get file: %s', fileName);
    fo = open(target_folder + fileName, "w")
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

logging.info('fetching completed');
cc.close()
c.close()    
