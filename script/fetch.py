#! /usr/bin/python
# -*- coding: utf8 -*-

from datetime import datetime
import logging
import os
import pycurl
import json
import re
import sys
from StringIO import StringIO

reload(sys)
sys.setdefaultencoding("utf-8")

_time = datetime.now().strftime("%Y-%m-%d %H:%M");
logging.basicConfig(filename='/var/log/fetch-' + _time + '.log',level=logging.INFO)

logging.info('fetch articles from atavist')

buffer = StringIO()

api = 'https://atavist.com/api/public/library.php?organization_id=60826&paginationLimit=30'
target_folder = '/tmp/twreporters/articles/'

logging.info('api: %s ', api);
replace = [{
            # js & css files
            "orig": "https://twreporter.atavist.com/view/", 
            "new":"https://www.twreporter.org/view/"
        }, {
            # canonical url
            "orig": "<link rel=\"canonical\" href=\"https://twreporter.atavist.com/",
            "new": "<link rel=\"canonical\" href=\"https://www.twreporter.org/a/"
        }, {
            # change domain
            "orig": "<meta property=\"og:image\" content=\"https://twreporter.atavist.com/",
            "new": "<meta property=\"og:image\" content=\"https://www.twreporter.org/"
        }, {
            # change domain
            "orig": "<meta name=\"twitter:image\" content=\"https://twreporter.atavist.com/",
            "new": "<meta name=\"twitter:image\" content=\"https://www.twreporter.org/"
        }] 

c = pycurl.Curl()
cc = pycurl.Curl()
c.setopt(c.URL, api)
c.setopt(c.WRITEDATA, buffer)
c.perform()
result = buffer.getvalue()
records = json.loads(result, encoding="utf-8")

logging.debug('records from api: %s', json.dumps(records));

for i in records['stories']:
    pageBuffer = StringIO()
    fileName = i['slug']
    logging.info('get file: %s', fileName);
    fo = open(target_folder + fileName, "w")
    cc.setopt(cc.URL, i['url'])
    cc.setopt(cc.WRITEDATA, pageBuffer)
    cc.perform()
    body = pageBuffer.getvalue()
    # pre-load the js and css first
    preload = ["style.css", "script.js"]
    for f in preload:
        pattern = "https:\/\/twreporter\.atavist\.com\/view\/twreporter\/" + i['slug'] + "\/" + f + "\?bump\&\d+"
        match = re.search(pattern, body)

        if match:
            assetBuffer = StringIO()
            cc.setopt(cc.URL, match.group(0))
            cc.setopt(cc.WRITEDATA, assetBuffer)
            cc.perform()
            asset = assetBuffer.getvalue()
            filePath = target_folder + i["slug"] + "-" + f
            replace_url = 'https://www.twreporter.org/a/' + i["slug"] + "-" + f
            asset_file = open(target_folder + i["slug"] + "-" + f, "w")
            # we should have the exception handler
            asset_file.write(asset)
            asset_file.close
            #if (os.path.isfile(target_folder + i["slug"] + "-" + f)):
            #    body = body.replace(match.group(0), replace_url)
    # Body is a string in some encoding.
    # In Python 2, we can print it without knowing what the encoding is.
    for str_replace in replace:
        body = body.replace(str_replace['orig'], str_replace['new'])
    
    # append 報導者
    body = re.sub(r'<meta property="og:title" content="(.*?)"', r'<meta property="og:title" content="\1／報導者"' , body)
    body = re.sub(r'<meta name="twitter:title" content="(.*?)"', r'<meta name="twitter:title" content="\1／報導者"' , body)

    fo.write(body)
    fo.close()
    # print(body)

logging.info('fetching completed');
cc.close()
c.close()    
