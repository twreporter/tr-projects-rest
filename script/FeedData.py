#! /usr/bin/python

import json
import urllib2
import subprocess
from sys import argv

if __name__ == '__main__':
  if len(argv) < 3:
    print 'usage: %s [url] [key]' % argv[0]
    exit()

  url = argv[1]
  key = argv[2]
  data = json.load(urllib2.urlopen(url))[key]

  for record in data:
    _id = str(record['id'])
    pre = '0' * (24 - len(_id)) # used as mongo _id
    cmd = '''
    curl -d '%s' -X PUT -H 'Content-Type: application/json' http://localhost:8080/article/%s
    ''' % (json.dumps(record), pre+_id)
    subprocess.Popen(cmd, shell=True)
